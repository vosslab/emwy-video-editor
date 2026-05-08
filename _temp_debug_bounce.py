#!/usr/bin/env python3
"""Debug scale bounce in first 2 seconds of IMG_3702.

Traces the crop-height pipeline stage by stage:
  raw torso h -> desired crop h -> smoothed h -> constrained h -> final crop h

Reports where oscillation enters.
"""

# Standard Library
import os
import sys
import math
import subprocess

# PIP3 modules
import numpy
import json

REPO_ROOT = subprocess.run(
	["git", "rev-parse", "--show-toplevel"],
	capture_output=True, text=True, check=True,
).stdout.strip()

sys.path.insert(0, os.path.join(REPO_ROOT, "emwy_tools", "track_runner"))
sys.path.insert(0, os.path.join(REPO_ROOT, "emwy_tools"))

# local repo modules
import state_io
import tr_config
import tr_crop
import interval_solver


#============================================
def load_trajectory(video_name: str, data_dir: str, video_info: dict) -> list:
	"""Load and reconstruct trajectory for a video."""
	prefix = os.path.join(data_dir, video_name + ".track_runner")
	intervals_path = prefix + ".intervals.json"
	seeds_path = prefix + ".seeds.json"
	intervals_file = state_io.load_intervals(intervals_path)
	solved = intervals_file.get("solved_intervals", {})
	interval_results = sorted(
		solved.values(), key=lambda r: int(r["start_frame"]),
	)
	trajectory = interval_solver.stitch_trajectories(interval_results)
	all_seeds = []
	if os.path.isfile(seeds_path):
		seeds_data = state_io.load_seeds(seeds_path)
		all_seeds = seeds_data.get("seeds", [])
		trajectory = interval_solver.anchor_to_seeds(trajectory, all_seeds)
		fps = video_info["fps"]
		trajectory = interval_solver._apply_trajectory_erasure(
			trajectory, all_seeds, fps,
		)
	return trajectory


#============================================
def main() -> None:
	"""Debug the first 2 seconds of IMG_3702 crop pipeline."""
	video_name = "Hononega-Orion_600m-IMG_3702.mkv"
	data_dir = os.path.join(REPO_ROOT, "tr_config")
	# video info (known from prior probe)
	frame_width = 2816
	frame_height = 1584
	fps = 60.0
	video_info = {
		"width": frame_width, "height": frame_height,
		"fps": fps, "frame_count": 5536,
	}
	# load trajectory
	trajectory = load_trajectory(video_name, data_dir, video_info)
	print(f"trajectory length: {len(trajectory)}")
	# count None entries
	none_count = sum(1 for t in trajectory if t is None)
	print(f"None entries: {none_count}")

	# load config
	config_path = os.path.join(
		data_dir, video_name + ".track_runner.config.yaml",
	)
	if os.path.isfile(config_path):
		cfg = tr_config.load_config(config_path)
	else:
		cfg = tr_config.default_config()

	processing = cfg.get("processing", {})
	fill_ratio = float(processing.get("crop_fill_ratio", 0.30))
	max_hc = float(processing.get("crop_max_height_change", 0.005))
	alpha_size = float(processing.get("crop_post_smooth_size_strength", 0.0))
	print(f"\nConfig: fill_ratio={fill_ratio}, max_height_change={max_hc}")
	print(f"  alpha_size={alpha_size}")
	print(f"  crop_aspect={processing.get('crop_aspect', '1:1')}")
	print(f"  containment_radius={processing.get('crop_containment_radius', 0.20)}")

	# first 120 frames (~2 seconds at 60fps)
	n_inspect = 120
	print(f"\n{'='*80}")
	print(f"FIRST {n_inspect} FRAMES: raw torso height")
	print(f"{'='*80}")

	# extract raw heights
	raw_h = []
	for i in range(min(n_inspect, len(trajectory))):
		t = trajectory[i]
		if t is not None:
			raw_h.append(t["h"])
		else:
			raw_h.append(None)

	# print raw h with frame-to-frame deltas
	print(f"\n{'frame':>5} {'raw_h':>8} {'delta':>8} {'pct':>6} {'source':>12}")
	print("-" * 50)
	prev_h = None
	for i in range(len(raw_h)):
		h = raw_h[i]
		if h is None:
			print(f"{i:5d} {'None':>8}")
			continue
		if prev_h is not None and prev_h > 0:
			delta = h - prev_h
			pct = delta / prev_h * 100
			src = trajectory[i]["source"] if trajectory[i] else "?"
			print(f"{i:5d} {h:8.1f} {delta:8.1f} {pct:+5.1f}% {src:>12}")
		else:
			src = trajectory[i]["source"] if trajectory[i] else "?"
			print(f"{i:5d} {h:8.1f} {'---':>8} {'---':>6} {src:>12}")
		prev_h = h

	# height distribution for full trajectory
	all_h = [t["h"] for t in trajectory if t is not None]
	arr_h = numpy.array(all_h)
	print(f"\n{'='*80}")
	print("FULL TRAJECTORY: height distribution")
	print(f"{'='*80}")
	print(f"  count: {len(arr_h)}")
	print(f"  min:   {arr_h.min():.1f}")
	print(f"  p05:   {numpy.percentile(arr_h, 5):.1f}")
	print(f"  p25:   {numpy.percentile(arr_h, 25):.1f}")
	print(f"  median:{numpy.median(arr_h):.1f}")
	print(f"  p75:   {numpy.percentile(arr_h, 75):.1f}")
	print(f"  p95:   {numpy.percentile(arr_h, 95):.1f}")
	print(f"  max:   {arr_h.max():.1f}")
	print(f"  std:   {arr_h.std():.1f}")
	print(f"  CV:    {arr_h.std()/arr_h.mean():.3f}")

	# desired crop height = h / fill_ratio
	desired_ch = arr_h / fill_ratio
	print(f"\n  desired crop h from fill_ratio={fill_ratio}:")
	print(f"    median: {numpy.median(desired_ch):.0f}")
	print(f"    p75:    {numpy.percentile(desired_ch, 75):.0f}")
	print(f"    p95:    {numpy.percentile(desired_ch, 95):.0f}")
	print(f"    max:    {desired_ch.max():.0f}")
	print(f"    frame_height: {frame_height}")
	# how many frames have desired crop > frame height?
	oversized = numpy.sum(desired_ch > frame_height)
	print(f"    frames where desired crop > frame: {oversized} ({oversized/len(desired_ch)*100:.1f}%)")

	# now run the actual pipeline and extract intermediate signals
	print(f"\n{'='*80}")
	print(f"PIPELINE: first {n_inspect} frames")
	print(f"{'='*80}")

	# run direct_center to get final crop rects
	# gap-fill trajectory first (same as trajectory_to_crop_rects)
	full_traj = []
	last_known = None
	for i in range(video_info["frame_count"]):
		if i < len(trajectory) and trajectory[i] is not None:
			full_traj.append(trajectory[i])
			last_known = trajectory[i]
		elif last_known is not None:
			hold_state = {
				"cx": last_known["cx"], "cy": last_known["cy"],
				"w": last_known["w"], "h": last_known["h"],
				"conf": 0.15, "source": "hold_last",
			}
			full_traj.append(hold_state)
		else:
			fallback = {
				"cx": frame_width / 2.0, "cy": frame_height / 2.0,
				"w": float(frame_width) * 0.3, "h": float(frame_height) * 0.5,
				"conf": 0.1, "source": "fallback",
			}
			full_traj.append(fallback)

	# get final crop rects
	crop_rects = tr_crop.direct_center_crop_trajectory(
		full_traj, frame_width, frame_height, cfg,
	)

	# also compute intermediate signals manually to trace the pipeline
	aspect_str = processing.get("crop_aspect", "1:1")
	aspect_ratio = tr_crop.parse_aspect_ratio(aspect_str)
	alpha_pos = float(processing.get("crop_post_smooth_strength", 0.0))
	min_crop_size = int(processing.get("crop_min_size", 200))

	n = len(full_traj)
	raw_cx = numpy.empty(n, dtype=float)
	raw_cy = numpy.empty(n, dtype=float)
	raw_h_full = numpy.empty(n, dtype=float)
	for i in range(n):
		raw_cx[i] = full_traj[i]["cx"]
		raw_cy[i] = full_traj[i]["cy"]
		raw_h_full[i] = full_traj[i]["h"]

	desired_crop_h_full = raw_h_full / fill_ratio

	# step 2: EMA
	if alpha_size > 0:
		smoothed_h = tr_crop._forward_backward_ema(desired_crop_h_full, alpha_size)
	else:
		smoothed_h = desired_crop_h_full.copy()

	# step 2.5: zoom constraint
	constrained_h = smoothed_h.copy()
	if max_hc > 0:
		for i in range(1, n):
			delta = constrained_h[i] - constrained_h[i - 1]
			max_delta = max_hc * constrained_h[i - 1]
			if abs(delta) > max_delta:
				constrained_h[i] = constrained_h[i - 1] + math.copysign(max_delta, delta)

	# print pipeline stages for first n_inspect frames
	print(f"\n{'frame':>5} {'raw_h':>7} {'des_ch':>7} {'smo_h':>7} "
		+ f"{'con_h':>7} {'fin_h':>7} {'d_raw':>7} {'d_fin':>7}")
	print("-" * 75)
	for i in range(min(n_inspect, n)):
		rh = raw_h_full[i]
		dch = desired_crop_h_full[i]
		sh = smoothed_h[i]
		ch = constrained_h[i]
		fh = crop_rects[i][3] if i < len(crop_rects) else 0
		if i > 0:
			d_raw = raw_h_full[i] - raw_h_full[i - 1]
			d_fin = (crop_rects[i][3] - crop_rects[i - 1][3]) if i < len(crop_rects) else 0
		else:
			d_raw = 0
			d_fin = 0
		print(f"{i:5d} {rh:7.1f} {dch:7.0f} {sh:7.0f} "
			+ f"{ch:7.0f} {fh:7d} {d_raw:+7.1f} {d_fin:+7d}")

	# count direction changes in final crop height (bounce detection)
	print(f"\n{'='*80}")
	print("BOUNCE DETECTION: direction changes in final crop height")
	print(f"{'='*80}")
	direction_changes = 0
	change_frames = []
	for i in range(2, min(n_inspect, len(crop_rects))):
		prev_d = crop_rects[i - 1][3] - crop_rects[i - 2][3]
		curr_d = crop_rects[i][3] - crop_rects[i - 1][3]
		if prev_d * curr_d < 0 and abs(prev_d) > 0 and abs(curr_d) > 0:
			direction_changes += 1
			change_frames.append(i)
	print(f"  direction changes in first {n_inspect} frames: {direction_changes}")
	if change_frames:
		print(f"  at frames: {change_frames[:20]}")

	# same for raw h
	raw_bounces = 0
	raw_bounce_frames = []
	valid_h = [(i, raw_h_full[i]) for i in range(min(n_inspect, n))]
	for idx in range(2, len(valid_h)):
		i2, h2 = valid_h[idx]
		i1, h1 = valid_h[idx - 1]
		i0, h0 = valid_h[idx - 2]
		d_prev = h1 - h0
		d_curr = h2 - h1
		if d_prev * d_curr < 0 and abs(d_prev) > 1.0 and abs(d_curr) > 1.0:
			raw_bounces += 1
			raw_bounce_frames.append(i2)
	print(f"  direction changes in raw h: {raw_bounces}")
	if raw_bounce_frames:
		print(f"  at frames: {raw_bounce_frames[:20]}")


#============================================
if __name__ == "__main__":
	main()
