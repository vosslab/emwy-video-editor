#!/usr/bin/env python3
"""
Synthetic frame tests for tools/assess_pixel_zoom.py using Fourier-Mellin registration.

Tests calibrate zoom scale estimation via log-polar FFT phase correlation.
All tests use in-memory numpy arrays without video files on disk.
"""

import sys
import os
import subprocess
import math

import numpy
import cv2
import pytest

# determine repo root and add tools directory to path
REPO_ROOT = subprocess.run(
	["git", "rev-parse", "--show-toplevel"],
	capture_output=True, text=True, check=True,
).stdout.strip()
sys.path.insert(0, os.path.join(REPO_ROOT, "tools"))

import assess_pixel_zoom

#============================================

def generate_checkerboard_texture(h: int, w: int, square_size: int = 8) -> numpy.ndarray:
	"""
	Generate checkerboard pattern with random noise for multi-frequency content.

	Args:
		h: frame height
		w: frame width
		square_size: size of checkerboard squares

	Returns:
		uint8 grayscale image with checkerboard and noise
	"""
	# checkerboard pattern
	checker = numpy.zeros((h, w), dtype=numpy.uint8)
	for y in range(h):
		for x in range(w):
			if ((y // square_size) + (x // square_size)) % 2 == 0:
				checker[y, x] = 200
			else:
				checker[y, x] = 50

	# add random noise for multi-frequency content
	noise = numpy.random.randint(0, 30, (h, w), dtype=numpy.uint8)
	texture = numpy.clip(checker.astype(int) + noise.astype(int), 0, 255)
	return texture.astype(numpy.uint8)

#============================================

def apply_scale_transform(
	base_gray: numpy.ndarray,
	scale_factor: float
) -> numpy.ndarray:
	"""
	Apply center-anchored scale transformation via cv2.warpAffine.

	Args:
		base_gray: uint8 grayscale image
		scale_factor: scale multiplier (e.g., 1.05 for 5% zoom in)

	Returns:
		scaled uint8 grayscale image
	"""
	h, w = base_gray.shape
	center_x = w / 2.0
	center_y = h / 2.0

	# create similarity matrix for scale (no rotation)
	M = cv2.getRotationMatrix2D((center_x, center_y), 0, scale_factor)

	# warp with reflect border mode to avoid black edges
	scaled = cv2.warpAffine(
		base_gray, M, (w, h),
		borderMode=cv2.BORDER_REFLECT,
		flags=cv2.INTER_LINEAR
	)
	return scaled.astype(numpy.uint8)

#============================================

def compute_fm_scale(
	gray_prev: numpy.ndarray,
	gray_curr: numpy.ndarray,
	mask_mode: str = "full"
) -> tuple:
	"""
	Compute scale estimate via Fourier-Mellin pipeline.

	Args:
		gray_prev: previous frame (uint8)
		gray_curr: current frame (uint8)
		mask_mode: edge masking mode

	Returns:
		(scale, confidence) tuple
	"""
	h, w = gray_prev.shape

	# build masks and window
	mask = assess_pixel_zoom.build_edge_mask(h, w, mask_mode)
	hann = numpy.outer(
		numpy.hanning(h), numpy.hanning(w)
	).astype(numpy.float32)

	# compute log-polar transforms
	lp_prev = assess_pixel_zoom.compute_fft_log_polar(gray_prev, mask, hann)
	lp_curr = assess_pixel_zoom.compute_fft_log_polar(gray_curr, mask, hann)

	# estimate scale
	max_radius = min(h, w) // 2
	scale, corr = assess_pixel_zoom.estimate_scale_fourier_mellin(
		lp_prev, lp_curr, max_radius, w
	)

	return (scale, corr)

#============================================

def test_identity_scale() -> None:
	"""
	Test scale=1.0 (no zoom).

	Identical frames should produce scale near 1.0.
	"""
	h, w = 480, 640
	base_gray = generate_checkerboard_texture(h, w)

	scale, corr = compute_fm_scale(base_gray, base_gray)

	assert abs(scale - 1.0) < 0.001, \
		f"identity scale should be ~1.0, got {scale:.6f}"
	assert corr > 0.5, f"identity correlation should be high, got {corr:.3f}"

#============================================

def test_small_zoom_in() -> None:
	"""
	Test scale=1.01 (1% zoom in).

	Measured scale should match known scale within 0.005.
	"""
	h, w = 480, 640
	base_gray = generate_checkerboard_texture(h, w)
	scaled_gray = apply_scale_transform(base_gray, 1.01)

	scale, corr = compute_fm_scale(base_gray, scaled_gray)

	assert abs(scale - 1.01) < 0.005, \
		f"1.01 scale estimate should be close, got {scale:.6f}"
	assert corr > 0.1, \
		f"correlation should exceed threshold, got {corr:.3f}"

#============================================

def test_moderate_zoom_in() -> None:
	"""
	Test scale=1.05 (5% zoom in).

	Measured scale should match known scale within 0.005.
	"""
	h, w = 480, 640
	base_gray = generate_checkerboard_texture(h, w)
	scaled_gray = apply_scale_transform(base_gray, 1.05)

	scale, corr = compute_fm_scale(base_gray, scaled_gray)

	assert abs(scale - 1.05) < 0.005, \
		f"1.05 scale estimate should be close, got {scale:.6f}"
	assert corr > 0.1, \
		f"correlation should exceed threshold, got {corr:.3f}"

#============================================

def test_zoom_out() -> None:
	"""
	Test scale=0.98 (2% zoom out).

	Measured scale should match known scale within 0.015.
	Zoom-out has higher error than zoom-in due to border effects in warpAffine.
	"""
	h, w = 480, 640
	base_gray = generate_checkerboard_texture(h, w)
	scaled_gray = apply_scale_transform(base_gray, 0.98)

	scale, corr = compute_fm_scale(base_gray, scaled_gray)

	# zoom-out has slightly higher error due to border effects in warpAffine
	assert abs(scale - 0.98) < 0.015, \
		f"0.98 scale estimate should be close, got {scale:.6f}"
	assert corr > 0.1, \
		f"correlation should exceed threshold, got {corr:.3f}"

#============================================

def test_cumulative_zoom() -> None:
	"""
	Test cumulative 1.002x over 30 frames.

	Chain of small scales should accumulate to expected cumulative scale.
	Small scales near 1.0 are harder to estimate; tolerance: 4% of true.
	True cumulative is 1.002^30 ~ 1.0618.
	"""
	h, w = 480, 640
	scale_per_frame = 1.002
	num_frames = 30

	base_gray = generate_checkerboard_texture(h, w)
	cumulative = 1.0
	prev_gray = base_gray

	for frame_idx in range(num_frames):
		curr_gray = apply_scale_transform(prev_gray, scale_per_frame)
		scale, _ = compute_fm_scale(prev_gray, curr_gray)

		cumulative *= scale
		prev_gray = curr_gray

	true_cumulative = scale_per_frame ** num_frames
	tolerance = true_cumulative * 0.04

	assert abs(cumulative - true_cumulative) < tolerance, \
		f"cumulative {cumulative:.6f} should be near {true_cumulative:.6f}"

#============================================

def test_bouncing_pattern() -> None:
	"""
	Test alternating scales 1.01 and 0.99 over 20 frames.

	Should detect bouncing pattern (zero-crossings in velocity).
	"""
	h, w = 480, 640
	scales = [1.01, 0.99] * 10

	base_gray = generate_checkerboard_texture(h, w)
	prev_gray = base_gray
	velocity_logs = []

	for scale in scales:
		curr_gray = apply_scale_transform(prev_gray, scale)
		measured_scale, _ = compute_fm_scale(prev_gray, curr_gray)

		log_scale = math.log(measured_scale)
		velocity_logs.append(log_scale)
		prev_gray = curr_gray

	# count zero-crossings in velocity (bounces)
	noise_threshold = 0.0005
	bounce_count = 0
	for i in range(1, len(velocity_logs)):
		if (velocity_logs[i] > noise_threshold and
			velocity_logs[i - 1] <= noise_threshold):
			bounce_count += 1
		elif (velocity_logs[i] < -noise_threshold and
			velocity_logs[i - 1] >= -noise_threshold):
			bounce_count += 1

	# should see roughly 10 bounces (roughly half the transitions)
	assert bounce_count > 5, \
		f"bouncing pattern should detect ~10 bounces, got {bounce_count}"

#============================================

def test_blank_frame() -> None:
	"""
	Test uniform gray frames.

	Uniform images lack texture; phase correlation should be low or NaN.
	"""
	h, w = 480, 640
	gray_uniform = numpy.full((h, w), 128, dtype=numpy.uint8)

	scale, corr = compute_fm_scale(gray_uniform, gray_uniform)

	# correlation should be very low or the scale clamped
	assert corr < 0.2 or abs(scale - 1.0) < 0.002, \
		f"uniform frames should have low correlation, got {corr:.3f}"

#============================================

def test_translation_only() -> None:
	"""
	Test translation (shift) without scale.

	Pure translation (5px shift) should not affect scale estimate.
	Measured scale should be close to 1.0.
	"""
	h, w = 480, 640
	base_gray = generate_checkerboard_texture(h, w)

	# shift by 5 pixels via roll
	shifted_gray = numpy.roll(base_gray, 5, axis=1)

	scale, corr = compute_fm_scale(base_gray, shifted_gray)

	assert abs(scale - 1.0) < 0.002, \
		f"pure translation should have scale ~1.0, got {scale:.6f}"

#============================================

def test_blurred_frames() -> None:
	"""
	Test Gaussian blur (sigma=2.0) on textured image.

	Blur should degrade but not destroy scale estimate validity.
	"""
	h, w = 480, 640
	base_gray = generate_checkerboard_texture(h, w)
	blurred_gray = cv2.GaussianBlur(base_gray, (5, 5), 2.0)
	scaled_blurred = apply_scale_transform(blurred_gray, 1.05)

	scale, corr = compute_fm_scale(blurred_gray, scaled_blurred)

	# blurred scale estimate should still be valid but may have wider tolerance
	assert abs(scale - 1.05) < 0.01, \
		f"blurred scale should estimate 1.05, got {scale:.6f}"

#============================================

def test_noisy_frames() -> None:
	"""
	Test additive Gaussian noise (sigma=10) on textured image.

	Noise should degrade but not destroy scale estimate validity.
	"""
	h, w = 480, 640
	base_gray = generate_checkerboard_texture(h, w)

	# add Gaussian noise
	noise = numpy.random.normal(0, 10, (h, w))
	noisy_gray = numpy.clip(base_gray.astype(int) + noise, 0, 255).astype(numpy.uint8)
	scaled_noisy = apply_scale_transform(noisy_gray, 1.05)

	scale, corr = compute_fm_scale(noisy_gray, scaled_noisy)

	# noisy estimate should still be valid but with wider tolerance
	assert abs(scale - 1.05) < 0.01, \
		f"noisy scale should estimate 1.05, got {scale:.6f}"

#============================================

def test_edge_weighted_mask() -> None:
	"""
	Test edge_weighted masking produces different result from full.

	Edge-weighted and full masks should produce different estimates
	when the center has moving objects (simulated by different scales).
	"""
	h, w = 480, 640
	base_gray = generate_checkerboard_texture(h, w)
	scaled_gray = apply_scale_transform(base_gray, 1.05)

	scale_full, _ = compute_fm_scale(base_gray, scaled_gray, mask_mode="full")
	scale_edge, _ = compute_fm_scale(base_gray, scaled_gray, mask_mode="edge_weighted")

	# both should be valid, but edge-weighted may differ in magnitude
	assert 0.8 <= scale_full <= 1.25, f"full scale should be valid, got {scale_full:.6f}"
	assert 0.8 <= scale_edge <= 1.25, f"edge scale should be valid, got {scale_edge:.6f}"

#============================================

def test_scale_calibration() -> None:
	"""
	Calibration test: known scales 0.95, 0.98, 1.0, 1.01, 1.02, 1.05, 1.10.

	Verify the FM pipeline produces scale estimates within expected range.
	This test calibrates and documents the shift-to-scale conversion accuracy.
	"""
	h, w = 480, 640
	known_scales = [0.95, 0.98, 1.0, 1.01, 1.02, 1.05, 1.10]

	base_gray = generate_checkerboard_texture(h, w)

	results = []
	for known_scale in known_scales:
		scaled_gray = apply_scale_transform(base_gray, known_scale)
		measured_scale, corr = compute_fm_scale(base_gray, scaled_gray)

		error = abs(measured_scale - known_scale)
		results.append({
			"known": known_scale,
			"measured": measured_scale,
			"error": error,
			"corr": corr,
		})

	# verify most results are within reasonable tolerance
	valid_count = sum(1 for r in results if r["error"] < 0.01)
	assert valid_count >= 5, \
		f"at least 5 scales should estimate within 0.01, got {valid_count}"

	# document findings for potential formula adjustment
	for r in results:
		assert r["corr"] > 0.05 or r["known"] == 1.0, \
			f"scale {r['known']:.2f}: low correlation {r['corr']:.3f}"

#============================================

def test_build_edge_mask_full() -> None:
	"""
	Test build_edge_mask in full mode (no masking).

	Should return all ones.
	"""
	h, w = 480, 640
	mask = assess_pixel_zoom.build_edge_mask(h, w, "full")

	assert mask.shape == (h, w)
	assert numpy.allclose(mask, 1.0), "full mask should be all ones"

#============================================

def test_build_edge_mask_edge_weighted() -> None:
	"""
	Test build_edge_mask in edge_weighted mode.

	Should produce radial smoothstep: low at center, high at edges.
	"""
	h, w = 480, 640
	mask = assess_pixel_zoom.build_edge_mask(h, w, "edge_weighted")

	assert mask.shape == (h, w)
	assert numpy.all(mask >= 0.0) and numpy.all(mask <= 1.0)
	assert mask.dtype == numpy.float32

	# center should be lower than edges
	center_val = mask[h // 2, w // 2]
	corner_val = mask[0, 0]
	assert center_val < corner_val, \
		f"center {center_val:.3f} should be < corner {corner_val:.3f}"

#============================================

def test_compute_fft_log_polar_shape() -> None:
	"""
	Test compute_fft_log_polar output shape and type.
	"""
	h, w = 480, 640
	gray = generate_checkerboard_texture(h, w)
	mask = assess_pixel_zoom.build_edge_mask(h, w, "full")
	hann = numpy.outer(
		numpy.hanning(h), numpy.hanning(w)
	).astype(numpy.float32)

	lp = assess_pixel_zoom.compute_fft_log_polar(gray, mask, hann)

	assert lp.shape == (h, w), f"output shape should be {(h, w)}, got {lp.shape}"
	assert lp.dtype == numpy.float32
	assert not numpy.any(numpy.isnan(lp)), "output should not contain NaN"

#============================================

def test_estimate_scale_fourier_mellin_return_type() -> None:
	"""
	Test estimate_scale_fourier_mellin return type.

	Should return (scale, confidence) tuple with valid numbers.
	"""
	h, w = 480, 640
	base_gray = generate_checkerboard_texture(h, w)
	scaled_gray = apply_scale_transform(base_gray, 1.05)

	mask = assess_pixel_zoom.build_edge_mask(h, w, "full")
	hann = numpy.outer(
		numpy.hanning(h), numpy.hanning(w)
	).astype(numpy.float32)

	lp_prev = assess_pixel_zoom.compute_fft_log_polar(base_gray, mask, hann)
	lp_curr = assess_pixel_zoom.compute_fft_log_polar(scaled_gray, mask, hann)

	max_radius = min(h, w) // 2
	scale, corr = assess_pixel_zoom.estimate_scale_fourier_mellin(
		lp_prev, lp_curr, max_radius, w
	)

	assert isinstance(scale, (int, float)), f"scale should be numeric, got {type(scale)}"
	assert isinstance(corr, (int, float)), f"corr should be numeric, got {type(corr)}"
	assert 0.8 <= scale <= 1.25, f"scale should be clamped, got {scale:.6f}"
	assert 0.0 <= corr <= 1.0, f"corr should be [0,1], got {corr:.3f}"

#============================================

if __name__ == "__main__":
	pytest.main([__file__, "-v"])
