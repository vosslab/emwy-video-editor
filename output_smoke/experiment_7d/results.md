# Encode experiment results

Generated: 2026-03-20 12:39

## Variants

- **A_baseline_dc**: Current direct_center: no size smoothing, no zoom stabilization
  - `crop_mode: direct_center`
  - `crop_aspect: 16:9`
  - `crop_fill_ratio: 0.3`
  - `crop_torso_anchor: 0.5`
  - `crop_post_smooth_size_strength: 0.0`
  - `crop_zoom_stabilization: False`
  - `video_codec: libx264`
  - `crf: 18`
  - `encode_filters: ['bilateral', 'auto_levels', 'hqdn3d']`
- **B_size_smooth**: Size smoothing only: forward-backward EMA alpha=0.05 on height
  - `crop_mode: direct_center`
  - `crop_aspect: 16:9`
  - `crop_fill_ratio: 0.3`
  - `crop_torso_anchor: 0.5`
  - `crop_post_smooth_size_strength: 0.05`
  - `crop_zoom_stabilization: False`
  - `video_codec: libx264`
  - `crf: 18`
  - `encode_filters: ['bilateral', 'auto_levels', 'hqdn3d']`
- **C_zoom_stab**: Zoom stabilization only: 3-mode constraint, no size smoothing
  - `crop_mode: direct_center`
  - `crop_aspect: 16:9`
  - `crop_fill_ratio: 0.3`
  - `crop_torso_anchor: 0.5`
  - `crop_post_smooth_size_strength: 0.0`
  - `crop_zoom_stabilization: True`
  - `video_codec: libx264`
  - `crf: 18`
  - `encode_filters: ['bilateral', 'auto_levels', 'hqdn3d']`
- **D_smooth_zoom**: Size smoothing + zoom stabilization combined
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
| canon_60d_600m_zo... | A_baseline_dc | 3.606 | 4.0 | 0.0966 | 6.5 | 19.1 | 2.37 | 32 | lateral_jitter_dominated | 13 |
| canon_60d_600m_zo... | B_size_smooth | 3.64 | 1.0 | 0.0966 | 8.0 | 19.1 | 2.34 | 32 | lateral_jitter_dominated | 12 |
| canon_60d_600m_zo... | C_zoom_stab | 3.64 | 1.0 | 0.0755 | 6.8 | 19.1 | 2.37 | 32 | lateral_jitter_dominated | 12 |
| canon_60d_600m_zo... | D_smooth_zoom | 3.808 | 1.0 | 0.083 | 8.6 | 19.1 | 2.31 | 29 | lateral_jitter_dominated | 13 |
| Hononega-Orion_60... | A_baseline_dc | 4.031 | 5.0 | 0.324 | 17.9 | 27.9 | 10.01 | 70 | lateral_jitter_dominated | 65 |
| Hononega-Orion_60... | B_size_smooth | 4.031 | 1.0 | 0.3241 | 18.0 | 27.9 | 9.8 | 72 | lateral_jitter_dominated | 67 |
| Hononega-Orion_60... | C_zoom_stab | 4.031 | 1.0 | 0.3248 | 17.1 | 27.9 | 11.33 | 80 | lateral_jitter_dominated | 58 |
| Hononega-Orion_60... | D_smooth_zoom | 4.031 | 1.0 | 0.3112 | 16.9 | 27.9 | 11.01 | 81 | lateral_jitter_dominated | 59 |
| Hononega-Varsity_... | A_baseline_dc | 8.139 | 4.0 | 0.3065 | 17.2 | 35.0 | 24.02 | 254 | lateral_jitter_dominated | 158 |
| Hononega-Varsity_... | B_size_smooth | 8.246 | 1.0 | 0.321 | 17.7 | 35.0 | 23.65 | 267 | lateral_jitter_dominated | 163 |
| Hononega-Varsity_... | C_zoom_stab | 8.062 | 1.0 | 0.28 | 16.9 | 35.0 | 26.07 | 276 | lateral_jitter_dominated | 156 |
| Hononega-Varsity_... | D_smooth_zoom | 8.139 | 1.0 | 0.2872 | 16.2 | 35.0 | 25.11 | 266 | lateral_jitter_dominated | 160 |
| IMG_3627.MOV | A_baseline_dc | 2.693 | 1.0 | 0.3789 | 28.4 | 76.5 | 62.9 | 111 | low_confidence_drift_dominated | 51 |
| IMG_3627.MOV | B_size_smooth | 2.693 | 1.0 | 0.3771 | 36.5 | 76.5 | 63.43 | 103 | low_confidence_drift_dominated | 51 |
| IMG_3627.MOV | C_zoom_stab | 2.693 | 1.0 | 0.331 | 38.8 | 76.5 | 63.69 | 101 | low_confidence_drift_dominated | 51 |
| IMG_3627.MOV | D_smooth_zoom | 2.693 | 1.0 | 0.3273 | 44.2 | 76.5 | 61.14 | 92 | low_confidence_drift_dominated | 52 |
| IMG_3629.mkv | A_baseline_dc | 4.924 | 1.0 | 0.6787 | 22.1 | 59.6 | 40.88 | 232 | low_confidence_drift_dominated | 121 |
| IMG_3629.mkv | B_size_smooth | 5.0 | 1.0 | 0.6687 | 26.3 | 59.6 | 39.52 | 223 | low_confidence_drift_dominated | 123 |
| IMG_3629.mkv | C_zoom_stab | 4.61 | 1.0 | 0.676 | 26.2 | 59.6 | 41.02 | 216 | low_confidence_drift_dominated | 117 |
| IMG_3629.mkv | D_smooth_zoom | 5.0 | 1.0 | 0.6307 | 29.6 | 59.6 | 38.37 | 222 | low_confidence_drift_dominated | 122 |
| IMG_3823.MP4 | A_baseline_dc | 2.0 | 0.0 | 0.0422 | 7.6 | 18.8 | 1.55 | 48 | lateral_jitter_dominated | 11 |
| IMG_3823.MP4 | B_size_smooth | 2.0 | 0.0 | 0.0492 | 7.5 | 18.8 | 1.55 | 47 | lateral_jitter_dominated | 11 |
| IMG_3823.MP4 | C_zoom_stab | 2.0 | 0.0 | 0.0692 | 7.3 | 18.8 | 1.55 | 46 | lateral_jitter_dominated | 11 |
| IMG_3823.MP4 | D_smooth_zoom | 2.0 | 0.0 | 0.0581 | 7.6 | 18.8 | 1.55 | 47 | lateral_jitter_dominated | 11 |
| IMG_3830.MP4 | A_baseline_dc | 2.236 | 1.0 | 0.2828 | 11.6 | 23.5 | 1.28 | 53 | low_confidence_drift_dominated | 12 |
| IMG_3830.MP4 | B_size_smooth | 2.236 | 1.0 | 0.2928 | 11.1 | 23.5 | 1.28 | 51 | low_confidence_drift_dominated | 12 |
| IMG_3830.MP4 | C_zoom_stab | 2.236 | 1.0 | 0.1059 | 10.7 | 23.5 | 1.28 | 60 | low_confidence_drift_dominated | 12 |
| IMG_3830.MP4 | D_smooth_zoom | 2.236 | 1.0 | 0.1707 | 12.7 | 23.5 | 1.28 | 55 | low_confidence_drift_dominated | 12 |

## Composition quality comparison

| Video | Variant | CtrOff p95 | EdgeTouch | BadFr% | BadCtr% | BadEdg% | BadZm% | BadRun |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| canon_60d_600m_zo... | A_baseline_dc | 0.0521 | 2 | 0.1 | 0.0 | 0.1 | 0.0 | 3 |
| canon_60d_600m_zo... | B_size_smooth | 0.0505 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| canon_60d_600m_zo... | C_zoom_stab | 0.0524 | 3 | 0.2 | 0.0 | 0.2 | 0.0 | 4 |
| canon_60d_600m_zo... | D_smooth_zoom | 0.0504 | 1 | 0.1 | 0.0 | 0.1 | 0.0 | 3 |
| Hononega-Orion_60... | A_baseline_dc | 0.0356 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| Hononega-Orion_60... | B_size_smooth | 0.0331 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| Hononega-Orion_60... | C_zoom_stab | 0.0393 | 13 | 0.6 | 0.0 | 0.6 | 0.0 | 16 |
| Hononega-Orion_60... | D_smooth_zoom | 0.0378 | 2 | 0.5 | 0.0 | 0.5 | 0.0 | 13 |
| Hononega-Varsity_... | A_baseline_dc | 0.0727 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| Hononega-Varsity_... | B_size_smooth | 0.0703 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| Hononega-Varsity_... | C_zoom_stab | 0.0807 | 13 | 0.1 | 0.0 | 0.1 | 0.0 | 14 |
| Hononega-Varsity_... | D_smooth_zoom | 0.0759 | 6 | 0.1 | 0.0 | 0.1 | 0.0 | 6 |
| IMG_3627.MOV | A_baseline_dc | 0.0488 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3627.MOV | B_size_smooth | 0.048 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3627.MOV | C_zoom_stab | 0.0478 | 3 | 0.1 | 0.0 | 0.1 | 0.0 | 7 |
| IMG_3627.MOV | D_smooth_zoom | 0.0463 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3629.mkv | A_baseline_dc | 0.0827 | 99 | 1.2 | 0.5 | 1.0 | 0.0 | 91 |
| IMG_3629.mkv | B_size_smooth | 0.0773 | 60 | 0.8 | 0.4 | 0.7 | 0.0 | 76 |
| IMG_3629.mkv | C_zoom_stab | 0.1184 | 494 | 4.4 | 1.1 | 3.7 | 0.0 | 240 |
| IMG_3629.mkv | D_smooth_zoom | 0.0815 | 290 | 2.6 | 0.4 | 2.4 | 0.0 | 172 |
| IMG_3823.MP4 | A_baseline_dc | 0.0332 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3823.MP4 | B_size_smooth | 0.0329 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3823.MP4 | C_zoom_stab | 0.0327 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3823.MP4 | D_smooth_zoom | 0.0329 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3830.MP4 | A_baseline_dc | 0.0336 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3830.MP4 | B_size_smooth | 0.0329 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3830.MP4 | C_zoom_stab | 0.0369 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3830.MP4 | D_smooth_zoom | 0.036 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |

## Zoom stabilization diagnostics

| Video | Variant | ZoomBlocks | Trans% | Settle% | Normal% | CropHVar | Size |
| --- | --- | --- | --- | --- | --- | --- | --- |
| canon_60d_600m_zo... | A_baseline_dc | 40 | 3.8 | 49.0 | 47.2 | 1129.9 | 616x346 |
| canon_60d_600m_zo... | B_size_smooth | 40 | 3.8 | 49.0 | 47.2 | 1157.0 | 624x350 |
| canon_60d_600m_zo... | C_zoom_stab | 40 | 3.8 | 49.0 | 47.2 | 675.5 | 614x346 |
| canon_60d_600m_zo... | D_smooth_zoom | 40 | 3.8 | 49.0 | 47.2 | 860.8 | 630x354 |
| Hononega-Orion_60... | A_baseline_dc | 42 | 3.7 | 21.7 | 74.6 | 33458.3 | 994x558 |
| Hononega-Orion_60... | B_size_smooth | 42 | 3.7 | 21.7 | 74.6 | 34946.9 | 1016x572 |
| Hononega-Orion_60... | C_zoom_stab | 42 | 3.7 | 21.7 | 74.6 | 28604.1 | 878x494 |
| Hononega-Orion_60... | D_smooth_zoom | 42 | 3.7 | 21.7 | 74.6 | 27108.2 | 904x508 |
| Hononega-Varsity_... | A_baseline_dc | 133 | 3.0 | 28.8 | 68.2 | 26683.4 | 916x516 |
| Hononega-Varsity_... | B_size_smooth | 133 | 3.0 | 28.8 | 68.2 | 30758.1 | 930x524 |
| Hononega-Varsity_... | C_zoom_stab | 133 | 3.0 | 28.8 | 68.2 | 19607.3 | 844x474 |
| Hononega-Varsity_... | D_smooth_zoom | 133 | 3.0 | 28.8 | 68.2 | 22136.6 | 876x492 |
| IMG_3627.MOV | A_baseline_dc | 28 | 1.2 | 19.5 | 79.3 | 14431.6 | 484x272 |
| IMG_3627.MOV | B_size_smooth | 28 | 1.2 | 19.5 | 79.3 | 14269.5 | 480x270 |
| IMG_3627.MOV | C_zoom_stab | 28 | 1.2 | 19.5 | 79.3 | 10161.5 | 478x268 |
| IMG_3627.MOV | D_smooth_zoom | 28 | 1.2 | 19.5 | 79.3 | 10570.4 | 498x280 |
| IMG_3629.mkv | A_baseline_dc | 81 | 1.9 | 20.5 | 77.6 | 88382.7 | 580x326 |
| IMG_3629.mkv | B_size_smooth | 81 | 1.9 | 20.5 | 77.6 | 88730.1 | 600x338 |
| IMG_3629.mkv | C_zoom_stab | 81 | 1.9 | 20.5 | 77.6 | 79746.2 | 578x324 |
| IMG_3629.mkv | D_smooth_zoom | 81 | 1.9 | 20.5 | 77.6 | 73961.0 | 618x348 |
| IMG_3823.MP4 | A_baseline_dc | 29 | 3.7 | 18.4 | 77.9 | 72.4 | 356x200 |
| IMG_3823.MP4 | B_size_smooth | 29 | 3.7 | 18.4 | 77.9 | 98.5 | 356x200 |
| IMG_3823.MP4 | C_zoom_stab | 29 | 3.7 | 18.4 | 77.9 | 198.0 | 356x200 |
| IMG_3823.MP4 | D_smooth_zoom | 29 | 3.7 | 18.4 | 77.9 | 139.4 | 356x200 |
| IMG_3830.MP4 | A_baseline_dc | 82 | 9.2 | 52.9 | 37.8 | 4044.2 | 356x200 |
| IMG_3830.MP4 | B_size_smooth | 82 | 9.2 | 52.9 | 37.8 | 4405.0 | 356x200 |
| IMG_3830.MP4 | C_zoom_stab | 82 | 9.2 | 52.9 | 37.8 | 492.9 | 356x200 |
| IMG_3830.MP4 | D_smooth_zoom | 82 | 9.2 | 52.9 | 37.8 | 1398.5 | 356x200 |

## Torso composition diagnostics

| Video | Variant | TorsoMed | TorsoP95 | Upper% |
| --- | --- | --- | --- | --- |
| canon_60d_600m_zo... | A_baseline_dc | 0.499 | 0.531 | 0.3 |
| canon_60d_600m_zo... | B_size_smooth | 0.499 | 0.531 | 0.2 |
| canon_60d_600m_zo... | C_zoom_stab | 0.499 | 0.531 | 0.2 |
| canon_60d_600m_zo... | D_smooth_zoom | 0.499 | 0.53 | 0.3 |
| Hononega-Orion_60... | A_baseline_dc | 0.5 | 0.513 | 0.1 |
| Hononega-Orion_60... | B_size_smooth | 0.5 | 0.513 | 0.0 |
| Hononega-Orion_60... | C_zoom_stab | 0.5 | 0.516 | 0.1 |
| Hononega-Orion_60... | D_smooth_zoom | 0.5 | 0.515 | 0.1 |
| Hononega-Varsity_... | A_baseline_dc | 0.5 | 0.515 | 0.1 |
| Hononega-Varsity_... | B_size_smooth | 0.5 | 0.514 | 0.1 |
| Hononega-Varsity_... | C_zoom_stab | 0.5 | 0.516 | 0.2 |
| Hononega-Varsity_... | D_smooth_zoom | 0.5 | 0.515 | 0.1 |
| IMG_3627.MOV | A_baseline_dc | 0.5 | 0.511 | 0.1 |
| IMG_3627.MOV | B_size_smooth | 0.5 | 0.511 | 0.1 |
| IMG_3627.MOV | C_zoom_stab | 0.5 | 0.511 | 0.1 |
| IMG_3627.MOV | D_smooth_zoom | 0.5 | 0.511 | 0.1 |
| IMG_3629.mkv | A_baseline_dc | 0.5 | 0.515 | 0.2 |
| IMG_3629.mkv | B_size_smooth | 0.5 | 0.514 | 0.2 |
| IMG_3629.mkv | C_zoom_stab | 0.5 | 0.524 | 0.3 |
| IMG_3629.mkv | D_smooth_zoom | 0.5 | 0.516 | 0.2 |
| IMG_3823.MP4 | A_baseline_dc | 0.5 | 0.517 | 0.0 |
| IMG_3823.MP4 | B_size_smooth | 0.5 | 0.517 | 0.0 |
| IMG_3823.MP4 | C_zoom_stab | 0.5 | 0.516 | 0.0 |
| IMG_3823.MP4 | D_smooth_zoom | 0.5 | 0.516 | 0.0 |
| IMG_3830.MP4 | A_baseline_dc | 0.5 | 0.516 | 0.0 |
| IMG_3830.MP4 | B_size_smooth | 0.5 | 0.516 | 0.0 |
| IMG_3830.MP4 | C_zoom_stab | 0.5 | 0.517 | 0.0 |
| IMG_3830.MP4 | D_smooth_zoom | 0.5 | 0.517 | 0.0 |

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
