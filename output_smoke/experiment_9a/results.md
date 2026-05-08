# Encode experiment results

Generated: 2026-03-20 22:08

## Variants

- **A_current**: Current baseline (torso_anchor=0.50, centered)
  - `crop_mode: direct_center`
  - `crop_aspect: 16:9`
  - `crop_fill_ratio: 0.3`
  - `crop_torso_anchor: 0.5`
  - `crop_post_smooth_size_strength: 0.05`
  - `crop_post_smooth_strength: 0.0`
  - `crop_zoom_stabilization: False`
  - `crop_containment_radius: 0.2`
  - `video_codec: libx264`
  - `crf: 18`
  - `encode_filters: ['bilateral', 'auto_levels', 'hqdn3d']`
- **B_anchor**: Composition fix only (torso_anchor=0.38, subject higher in frame)
  - `crop_mode: direct_center`
  - `crop_aspect: 16:9`
  - `crop_fill_ratio: 0.3`
  - `crop_torso_anchor: 0.38`
  - `crop_post_smooth_size_strength: 0.05`
  - `crop_post_smooth_strength: 0.0`
  - `crop_zoom_stabilization: False`
  - `crop_containment_radius: 0.2`
  - `video_codec: libx264`
  - `crf: 18`
  - `encode_filters: ['bilateral', 'auto_levels', 'hqdn3d']`

## Motion stability comparison

| Video | Variant | CJerk p95 | HJerk p95 | SizeCV | Chatter% | LowConf% | Conv/W% | Regions | Symptom | Time(s) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| canon_60d_600m_zo... | A_current | 3.64 | 1.0 | 0.1054 | 8.0 | 19.1 | 2.34 | 32 | lateral_jitter_dominated | 12 |
| canon_60d_600m_zo... | B_anchor | 3.64 | 1.0 | 0.1054 | 7.3 | 19.1 | 2.34 | 31 | lateral_jitter_dominated | 12 |
| Hononega-Orion_60... | A_current | 4.031 | 1.0 | 0.3422 | 18.8 | 27.9 | 9.81 | 70 | lateral_jitter_dominated | 63 |
| Hononega-Orion_60... | B_anchor | 4.031 | 1.0 | 0.3422 | 17.2 | 27.9 | 9.81 | 69 | lateral_jitter_dominated | 64 |
| Hononega-Varsity_... | A_current | 8.382 | 1.0 | 0.3548 | 17.5 | 35.0 | 24.12 | 269 | lateral_jitter_dominated | 148 |
| Hononega-Varsity_... | B_anchor | 8.062 | 1.0 | 0.3548 | 17.5 | 35.0 | 24.12 | 257 | lateral_jitter_dominated | 147 |
| IMG_3627.MOV | A_current | 2.693 | 1.0 | 0.3835 | 36.6 | 76.5 | 63.43 | 107 | low_confidence_drift_dominated | 49 |
| IMG_3627.MOV | B_anchor | 2.693 | 1.0 | 0.3835 | 36.4 | 76.5 | 63.43 | 111 | low_confidence_drift_dominated | 49 |
| IMG_3629.mkv | A_current | 5.025 | 1.0 | 0.7308 | 25.1 | 59.6 | 41.02 | 216 | low_confidence_drift_dominated | 115 |
| IMG_3629.mkv | B_anchor | 5.0 | 1.0 | 0.7308 | 23.7 | 59.6 | 41.02 | 204 | low_confidence_drift_dominated | 116 |
| IMG_3823.MP4 | A_current | 2.121 | 0.0 | 0.051 | 7.7 | 18.8 | 1.55 | 47 | lateral_jitter_dominated | 11 |
| IMG_3823.MP4 | B_anchor | 2.121 | 0.0 | 0.051 | 6.8 | 18.8 | 1.55 | 45 | lateral_jitter_dominated | 11 |
| IMG_3830.MP4 | A_current | 2.236 | 1.0 | 0.2986 | 11.1 | 23.5 | 1.28 | 50 | low_confidence_drift_dominated | 12 |
| IMG_3830.MP4 | B_anchor | 2.121 | 1.0 | 0.2986 | 11.2 | 23.5 | 1.28 | 63 | low_confidence_drift_dominated | 12 |

## Composition quality comparison

| Video | Variant | CtrOff p95 | EdgeTouch | BadFr% | BadCtr% | BadEdg% | BadZm% | BadRun |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| canon_60d_600m_zo... | A_current | 0.0505 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| canon_60d_600m_zo... | B_anchor | 0.1521 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| Hononega-Orion_60... | A_current | 0.0337 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| Hononega-Orion_60... | B_anchor | 0.1326 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| Hononega-Varsity_... | A_current | 0.0697 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| Hononega-Varsity_... | B_anchor | 0.1442 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3627.MOV | A_current | 0.0479 | 0 | 0.1 | 0.0 | 0.0 | 0.1 | 4 |
| IMG_3627.MOV | B_anchor | 0.135 | 0 | 0.1 | 0.0 | 0.0 | 0.1 | 4 |
| IMG_3629.mkv | A_current | 0.0921 | 0 | 2.9 | 1.1 | 0.9 | 1.9 | 184 |
| IMG_3629.mkv | B_anchor | 0.1498 | 0 | 2.6 | 0.8 | 0.0 | 1.9 | 133 |
| IMG_3823.MP4 | A_current | 0.0327 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3823.MP4 | B_anchor | 0.1225 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3830.MP4 | A_current | 0.0326 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3830.MP4 | B_anchor | 0.1302 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |

## Zoom stabilization diagnostics

| Video | Variant | ZoomBlocks | Trans% | Settle% | Normal% | CropHVar | Size |
| --- | --- | --- | --- | --- | --- | --- | --- |
| canon_60d_600m_zo... | A_current | 40 | 3.8 | 49.0 | 47.2 | 1388.7 | 624x350 |
| canon_60d_600m_zo... | B_anchor | 40 | 3.8 | 49.0 | 47.2 | 1388.7 | 624x350 |
| Hononega-Orion_60... | A_current | 42 | 3.7 | 21.7 | 74.6 | 38773.1 | 1014x570 |
| Hononega-Orion_60... | B_anchor | 42 | 3.7 | 21.7 | 74.6 | 38773.1 | 1014x570 |
| Hononega-Varsity_... | A_current | 133 | 3.0 | 28.8 | 68.2 | 37536.0 | 912x512 |
| Hononega-Varsity_... | B_anchor | 133 | 3.0 | 28.8 | 68.2 | 37536.0 | 912x512 |
| IMG_3627.MOV | A_current | 28 | 1.2 | 19.5 | 79.3 | 14844.4 | 480x270 |
| IMG_3627.MOV | B_anchor | 28 | 1.2 | 19.5 | 79.3 | 14844.4 | 480x270 |
| IMG_3629.mkv | A_current | 81 | 1.9 | 20.5 | 77.6 | 104972.2 | 578x324 |
| IMG_3629.mkv | B_anchor | 81 | 1.9 | 20.5 | 77.6 | 104972.2 | 578x324 |
| IMG_3823.MP4 | A_current | 29 | 3.7 | 18.4 | 77.9 | 105.8 | 356x200 |
| IMG_3823.MP4 | B_anchor | 29 | 3.7 | 18.4 | 77.9 | 105.8 | 356x200 |
| IMG_3830.MP4 | A_current | 82 | 9.2 | 52.9 | 37.8 | 4502.2 | 356x200 |
| IMG_3830.MP4 | B_anchor | 82 | 9.2 | 52.9 | 37.8 | 4502.2 | 356x200 |

## Torso composition diagnostics

| Video | Variant | TorsoMed | TorsoP95 | Upper% |
| --- | --- | --- | --- | --- |
| canon_60d_600m_zo... | A_current | 0.499 | 0.531 | 0.2 |
| canon_60d_600m_zo... | B_anchor | 0.379 | 0.411 | 97.5 |
| Hononega-Orion_60... | A_current | 0.5 | 0.513 | 0.0 |
| Hononega-Orion_60... | B_anchor | 0.38 | 0.393 | 99.8 |
| Hononega-Varsity_... | A_current | 0.5 | 0.514 | 0.1 |
| Hononega-Varsity_... | B_anchor | 0.38 | 0.394 | 99.2 |
| IMG_3627.MOV | A_current | 0.5 | 0.511 | 0.1 |
| IMG_3627.MOV | B_anchor | 0.38 | 0.426 | 92.6 |
| IMG_3629.mkv | A_current | 0.5 | 0.517 | 0.2 |
| IMG_3629.mkv | B_anchor | 0.38 | 0.413 | 95.9 |
| IMG_3823.MP4 | A_current | 0.5 | 0.517 | 0.0 |
| IMG_3823.MP4 | B_anchor | 0.442 | 0.462 | 21.1 |
| IMG_3830.MP4 | A_current | 0.5 | 0.516 | 0.0 |
| IMG_3830.MP4 | B_anchor | 0.425 | 0.449 | 42.8 |

## Pass criteria (Experiment 9A: composition)

- B_anchor `torso_pos_median` lower than A_current (torso higher in frame)
- B_anchor `torso_upper_frac` increases vs A_current
- Visual: feet visible, less headroom on B vs A
- `height_jerk_p95` within 10% of A (no zoom bounce regression)
- `edge_touch_count` does not increase on B vs A
- `bad_frame_pct` does not increase on B vs A
- canon_60d and IMG_3830 do not regress on any stability metric

## Decision fork

- YES: B improves framing across all/most videos -> lock anchor, proceed to 9B
- NO: B works on some but breaks others -> stop, move to phase-dependent anchor
- Single fallback: try 0.42 if 0.38 regresses. No further sweeps.

## How to review

1. Watch the `_clip*.mkv` files side by side
2. Rate each 0-3 for: jitter, zoom pumping, drift, shake
3. Compare your ratings against the metrics in the table
4. Full encodes are available for promising variants
