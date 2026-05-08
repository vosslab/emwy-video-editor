# Encode experiment results

Generated: 2026-03-20 21:24

## Variants

- **B_baseline**: EMA smoothing only (reproduces best 7d result as reference)
  - `crop_mode: direct_center`
  - `crop_aspect: 16:9`
  - `crop_fill_ratio: 0.3`
  - `crop_torso_anchor: 0.5`
  - `crop_post_smooth_size_strength: 0.05`
  - `crop_zoom_stabilization: False`
  - `video_codec: libx264`
  - `crf: 18`
  - `encode_filters: ['bilateral', 'auto_levels', 'hqdn3d']`
- **D_gated**: Same config as 7d D (EMA + zoom_stab + limiter), code gate active
  - `crop_mode: direct_center`
  - `crop_aspect: 16:9`
  - `crop_fill_ratio: 0.3`
  - `crop_torso_anchor: 0.5`
  - `crop_post_smooth_size_strength: 0.05`
  - `crop_zoom_stabilization: True`
  - `video_codec: libx264`
  - `crf: 18`
  - `encode_filters: ['bilateral', 'auto_levels', 'hqdn3d']`

## Motion stability comparison

| Video | Variant | CJerk p95 | HJerk p95 | SizeCV | Chatter% | LowConf% | Conv/W% | Regions | Symptom | Time(s) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| canon_60d_600m_zo... | B_baseline | 3.64 | 1.0 | 0.1054 | 8.0 | 19.1 | 2.34 | 32 | lateral_jitter_dominated | 13 |
| canon_60d_600m_zo... | D_gated | 3.64 | 1.0 | 0.1054 | 8.0 | 19.1 | 2.34 | 32 | lateral_jitter_dominated | 12 |
| Hononega-Orion_60... | B_baseline | 4.031 | 1.0 | 0.3422 | 18.8 | 27.9 | 9.81 | 70 | lateral_jitter_dominated | 64 |
| Hononega-Orion_60... | D_gated | 4.031 | 1.0 | 0.3422 | 18.8 | 27.9 | 9.81 | 70 | lateral_jitter_dominated | 64 |
| Hononega-Varsity_... | B_baseline | 8.382 | 1.0 | 0.3548 | 17.5 | 35.0 | 24.12 | 269 | lateral_jitter_dominated | 150 |
| Hononega-Varsity_... | D_gated | 8.382 | 1.0 | 0.3548 | 17.5 | 35.0 | 24.12 | 269 | lateral_jitter_dominated | 149 |
| IMG_3627.MOV | B_baseline | 2.693 | 1.0 | 0.3835 | 36.6 | 76.5 | 63.43 | 107 | low_confidence_drift_dominated | 50 |
| IMG_3627.MOV | D_gated | 2.693 | 1.0 | 0.3835 | 36.6 | 76.5 | 63.43 | 107 | low_confidence_drift_dominated | 50 |
| IMG_3629.mkv | B_baseline | 5.025 | 1.0 | 0.7308 | 25.1 | 59.6 | 41.02 | 216 | low_confidence_drift_dominated | 118 |
| IMG_3629.mkv | D_gated | 5.025 | 1.0 | 0.7308 | 25.1 | 59.6 | 41.02 | 216 | low_confidence_drift_dominated | 122 |
| IMG_3823.MP4 | B_baseline | 2.121 | 0.0 | 0.051 | 7.7 | 18.8 | 1.55 | 47 | lateral_jitter_dominated | 11 |
| IMG_3823.MP4 | D_gated | 2.121 | 0.0 | 0.051 | 7.7 | 18.8 | 1.55 | 47 | lateral_jitter_dominated | 11 |
| IMG_3830.MP4 | B_baseline | 2.236 | 1.0 | 0.2986 | 11.1 | 23.5 | 1.28 | 50 | low_confidence_drift_dominated | 12 |
| IMG_3830.MP4 | D_gated | 2.236 | 1.0 | 0.2986 | 11.1 | 23.5 | 1.28 | 50 | low_confidence_drift_dominated | 13 |

## Composition quality comparison

| Video | Variant | CtrOff p95 | EdgeTouch | BadFr% | BadCtr% | BadEdg% | BadZm% | BadRun |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| canon_60d_600m_zo... | B_baseline | 0.0505 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| canon_60d_600m_zo... | D_gated | 0.0505 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| Hononega-Orion_60... | B_baseline | 0.0337 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| Hononega-Orion_60... | D_gated | 0.0337 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| Hononega-Varsity_... | B_baseline | 0.0697 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| Hononega-Varsity_... | D_gated | 0.0697 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3627.MOV | B_baseline | 0.0479 | 0 | 0.1 | 0.0 | 0.0 | 0.1 | 4 |
| IMG_3627.MOV | D_gated | 0.0479 | 0 | 0.1 | 0.0 | 0.0 | 0.1 | 4 |
| IMG_3629.mkv | B_baseline | 0.0921 | 0 | 2.9 | 1.1 | 0.9 | 1.9 | 184 |
| IMG_3629.mkv | D_gated | 0.0921 | 0 | 2.9 | 1.1 | 0.9 | 1.9 | 184 |
| IMG_3823.MP4 | B_baseline | 0.0327 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3823.MP4 | D_gated | 0.0327 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3830.MP4 | B_baseline | 0.0326 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3830.MP4 | D_gated | 0.0326 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |

## Zoom stabilization diagnostics

| Video | Variant | ZoomBlocks | Trans% | Settle% | Normal% | CropHVar | Size |
| --- | --- | --- | --- | --- | --- | --- | --- |
| canon_60d_600m_zo... | B_baseline | 40 | 3.8 | 49.0 | 47.2 | 1388.7 | 624x350 |
| canon_60d_600m_zo... | D_gated | 40 | 3.8 | 49.0 | 47.2 | 1388.7 | 624x350 |
| Hononega-Orion_60... | B_baseline | 42 | 3.7 | 21.7 | 74.6 | 38773.1 | 1014x570 |
| Hononega-Orion_60... | D_gated | 42 | 3.7 | 21.7 | 74.6 | 38773.1 | 1014x570 |
| Hononega-Varsity_... | B_baseline | 133 | 3.0 | 28.8 | 68.2 | 37536.0 | 912x512 |
| Hononega-Varsity_... | D_gated | 133 | 3.0 | 28.8 | 68.2 | 37536.0 | 912x512 |
| IMG_3627.MOV | B_baseline | 28 | 1.2 | 19.5 | 79.3 | 14844.4 | 480x270 |
| IMG_3627.MOV | D_gated | 28 | 1.2 | 19.5 | 79.3 | 14844.4 | 480x270 |
| IMG_3629.mkv | B_baseline | 81 | 1.9 | 20.5 | 77.6 | 104972.2 | 578x324 |
| IMG_3629.mkv | D_gated | 81 | 1.9 | 20.5 | 77.6 | 104972.2 | 578x324 |
| IMG_3823.MP4 | B_baseline | 29 | 3.7 | 18.4 | 77.9 | 105.8 | 356x200 |
| IMG_3823.MP4 | D_gated | 29 | 3.7 | 18.4 | 77.9 | 105.8 | 356x200 |
| IMG_3830.MP4 | B_baseline | 82 | 9.2 | 52.9 | 37.8 | 4502.2 | 356x200 |
| IMG_3830.MP4 | D_gated | 82 | 9.2 | 52.9 | 37.8 | 4502.2 | 356x200 |

## Torso composition diagnostics

| Video | Variant | TorsoMed | TorsoP95 | Upper% |
| --- | --- | --- | --- | --- |
| canon_60d_600m_zo... | B_baseline | 0.499 | 0.531 | 0.2 |
| canon_60d_600m_zo... | D_gated | 0.499 | 0.531 | 0.2 |
| Hononega-Orion_60... | B_baseline | 0.5 | 0.513 | 0.0 |
| Hononega-Orion_60... | D_gated | 0.5 | 0.513 | 0.0 |
| Hononega-Varsity_... | B_baseline | 0.5 | 0.514 | 0.1 |
| Hononega-Varsity_... | D_gated | 0.5 | 0.514 | 0.1 |
| IMG_3627.MOV | B_baseline | 0.5 | 0.511 | 0.1 |
| IMG_3627.MOV | D_gated | 0.5 | 0.511 | 0.1 |
| IMG_3629.mkv | B_baseline | 0.5 | 0.517 | 0.2 |
| IMG_3629.mkv | D_gated | 0.5 | 0.517 | 0.2 |
| IMG_3823.MP4 | B_baseline | 0.5 | 0.517 | 0.0 |
| IMG_3823.MP4 | D_gated | 0.5 | 0.517 | 0.0 |
| IMG_3830.MP4 | B_baseline | 0.5 | 0.516 | 0.0 |
| IMG_3830.MP4 | D_gated | 0.5 | 0.516 | 0.0 |

## Pass criteria

- B reduces `crop_h_var` and `height_jerk_p95` vs A on all videos
- B reduces visible zoom bounce on IMG_3707
- B does not regress on canon_60d
- C reduces `height_jerk_p95` on IMG_3702 vs A (zoom transitions)
- D combines both improvements without regression
- `bad_frame_fraction < 0.05` (< 5%)
- `height_jerk_p95 < 5.0`

## How to review

1. Watch the `_clip*.mkv` files side by side
2. Rate each 0-3 for: jitter, zoom pumping, drift, shake
3. Compare your ratings against the metrics in the table
4. Full encodes are available for promising variants
