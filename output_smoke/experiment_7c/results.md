# Encode experiment results

Generated: 2026-03-19 11:18

## Variants

- **A_baseline_dc**: Current direct_center: centered torso, scalar zoom constraint
  - `crop_mode: direct_center`
  - `crop_aspect: 16:9`
  - `crop_fill_ratio: 0.3`
  - `crop_torso_anchor: 0.5`
  - `crop_zoom_stabilization: False`
  - `video_codec: libx264`
  - `crf: 18`
  - `encode_filters: ['bilateral', 'auto_levels', 'hqdn3d']`
- **B_torso_38**: Composition offset only: torso at 38% from top
  - `crop_mode: direct_center`
  - `crop_aspect: 16:9`
  - `crop_fill_ratio: 0.3`
  - `crop_torso_anchor: 0.38`
  - `crop_zoom_stabilization: False`
  - `video_codec: libx264`
  - `crf: 18`
  - `encode_filters: ['bilateral', 'auto_levels', 'hqdn3d']`
- **C_zoom_stabilized**: Piecewise zoom stabilization only, centered torso
  - `crop_mode: direct_center`
  - `crop_aspect: 16:9`
  - `crop_fill_ratio: 0.3`
  - `crop_torso_anchor: 0.5`
  - `crop_zoom_stabilization: True`
  - `video_codec: libx264`
  - `crf: 18`
  - `encode_filters: ['bilateral', 'auto_levels', 'hqdn3d']`
- **D_zoom_stabilized_torso_38**: Piecewise zoom stabilization + torso at 38% from top
  - `crop_mode: direct_center`
  - `crop_aspect: 16:9`
  - `crop_fill_ratio: 0.3`
  - `crop_torso_anchor: 0.38`
  - `crop_zoom_stabilization: True`
  - `video_codec: libx264`
  - `crf: 18`
  - `encode_filters: ['bilateral', 'auto_levels', 'hqdn3d']`

## Motion stability comparison

| Video | Variant | CJerk p95 | HJerk p95 | SizeCV | Chatter% | LowConf% | Conv/W% | Regions | Symptom | Time(s) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| canon_60d_600m_zo... | A_baseline_dc | 3.606 | 4.0 | 0.0966 | 6.5 | 19.1 | 2.37 | 32 | lateral_jitter_dominated | 12 |
| canon_60d_600m_zo... | B_torso_38 | 3.808 | 4.0 | 0.0966 | 5.7 | 19.1 | 2.37 | 35 | lateral_jitter_dominated | 12 |
| canon_60d_600m_zo... | C_zoom_stabilized | 3.64 | 1.0 | 0.0755 | 6.8 | 19.1 | 2.37 | 32 | lateral_jitter_dominated | 12 |
| canon_60d_600m_zo... | D_zoom_stabilized_torso_38 | 3.808 | 1.0 | 0.0755 | 6.8 | 19.1 | 2.37 | 35 | lateral_jitter_dominated | 12 |
| Hononega-Orion_60... | A_baseline_dc | 4.031 | 5.0 | 0.324 | 17.9 | 27.9 | 10.01 | 70 | lateral_jitter_dominated | 61 |
| Hononega-Orion_60... | B_torso_38 | 4.272 | 5.0 | 0.324 | 16.4 | 27.9 | 10.01 | 79 | lateral_jitter_dominated | 61 |
| Hononega-Orion_60... | C_zoom_stabilized | 4.031 | 1.0 | 0.3248 | 17.1 | 27.9 | 11.33 | 80 | lateral_jitter_dominated | 53 |
| Hononega-Orion_60... | D_zoom_stabilized_torso_38 | 5.0 | 1.0 | 0.3248 | 16.3 | 27.9 | 11.33 | 87 | lateral_jitter_dominated | 53 |
| Hononega-Varsity_... | A_baseline_dc | 8.139 | 4.0 | 0.3065 | 17.2 | 35.0 | 24.02 | 254 | lateral_jitter_dominated | 147 |
| Hononega-Varsity_... | B_torso_38 | 8.139 | 4.0 | 0.3065 | 16.3 | 35.0 | 24.02 | 251 | lateral_jitter_dominated | 148 |
| Hononega-Varsity_... | C_zoom_stabilized | 8.062 | 1.0 | 0.28 | 16.9 | 35.0 | 26.07 | 276 | lateral_jitter_dominated | 135 |
| Hononega-Varsity_... | D_zoom_stabilized_torso_38 | 8.5 | 1.0 | 0.28 | 16.0 | 35.0 | 26.07 | 285 | lateral_jitter_dominated | 135 |
| IMG_3627.MOV | A_baseline_dc | 2.693 | 1.0 | 0.3789 | 28.4 | 76.5 | 62.9 | 111 | low_confidence_drift_dominated | 49 |
| IMG_3627.MOV | B_torso_38 | 2.693 | 1.0 | 0.3789 | 28.3 | 76.5 | 62.9 | 127 | low_confidence_drift_dominated | 49 |
| IMG_3627.MOV | C_zoom_stabilized | 2.693 | 1.0 | 0.331 | 38.8 | 76.5 | 63.69 | 101 | low_confidence_drift_dominated | 48 |
| IMG_3627.MOV | D_zoom_stabilized_torso_38 | 2.693 | 1.0 | 0.331 | 37.2 | 76.5 | 63.69 | 95 | low_confidence_drift_dominated | 49 |
| IMG_3629.mkv | A_baseline_dc | 4.924 | 1.0 | 0.6787 | 22.1 | 59.6 | 40.88 | 232 | low_confidence_drift_dominated | 115 |
| IMG_3629.mkv | B_torso_38 | 4.528 | 1.0 | 0.6787 | 21.3 | 59.6 | 40.88 | 215 | low_confidence_drift_dominated | 115 |
| IMG_3629.mkv | C_zoom_stabilized | 4.61 | 1.0 | 0.676 | 26.2 | 59.6 | 41.02 | 216 | low_confidence_drift_dominated | 115 |
| IMG_3629.mkv | D_zoom_stabilized_torso_38 | 4.528 | 1.0 | 0.676 | 26.0 | 59.6 | 41.02 | 212 | low_confidence_drift_dominated | 115 |
| IMG_3823.MP4 | A_baseline_dc | 2.0 | 0.0 | 0.0422 | 7.6 | 18.8 | 1.55 | 48 | lateral_jitter_dominated | 11 |
| IMG_3823.MP4 | B_torso_38 | 2.236 | 0.0 | 0.0422 | 7.8 | 18.8 | 1.55 | 51 | lateral_jitter_dominated | 11 |
| IMG_3823.MP4 | C_zoom_stabilized | 2.0 | 0.0 | 0.0692 | 7.3 | 18.8 | 1.55 | 46 | lateral_jitter_dominated | 11 |
| IMG_3823.MP4 | D_zoom_stabilized_torso_38 | 2.236 | 0.0 | 0.0692 | 7.5 | 18.8 | 1.55 | 50 | lateral_jitter_dominated | 11 |
| IMG_3830.MP4 | A_baseline_dc | 2.236 | 1.0 | 0.2828 | 11.6 | 23.5 | 1.28 | 53 | low_confidence_drift_dominated | 12 |
| IMG_3830.MP4 | B_torso_38 | 2.236 | 1.0 | 0.2828 | 13.8 | 23.5 | 1.28 | 60 | low_confidence_drift_dominated | 12 |
| IMG_3830.MP4 | C_zoom_stabilized | 2.236 | 1.0 | 0.1059 | 10.7 | 23.5 | 1.28 | 60 | low_confidence_drift_dominated | 12 |
| IMG_3830.MP4 | D_zoom_stabilized_torso_38 | 2.5 | 1.0 | 0.1059 | 13.9 | 23.5 | 1.28 | 65 | lateral_jitter_dominated | 12 |

## Composition quality comparison

| Video | Variant | CtrOff p95 | EdgeTouch | BadFr% | BadCtr% | BadEdg% | BadZm% | BadRun |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| canon_60d_600m_zo... | A_baseline_dc | 0.0521 | 2 | 0.1 | 0.0 | 0.1 | 0.0 | 3 |
| canon_60d_600m_zo... | B_torso_38 | 0.1629 | 12 | 0.5 | 0.0 | 0.5 | 0.0 | 12 |
| canon_60d_600m_zo... | C_zoom_stabilized | 0.0524 | 3 | 0.2 | 0.0 | 0.2 | 0.0 | 4 |
| canon_60d_600m_zo... | D_zoom_stabilized_torso_38 | 0.1671 | 14 | 0.6 | 0.0 | 0.6 | 0.0 | 12 |
| Hononega-Orion_60... | A_baseline_dc | 0.0356 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| Hononega-Orion_60... | B_torso_38 | 0.1739 | 37 | 2.3 | 0.0 | 2.3 | 0.0 | 42 |
| Hononega-Orion_60... | C_zoom_stabilized | 0.0393 | 13 | 0.6 | 0.0 | 0.6 | 0.0 | 16 |
| Hononega-Orion_60... | D_zoom_stabilized_torso_38 | 0.1995 | 264 | 9.1 | 0.0 | 9.1 | 0.0 | 144 |
| Hononega-Varsity_... | A_baseline_dc | 0.0727 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| Hononega-Varsity_... | B_torso_38 | 0.1844 | 21 | 1.7 | 0.0 | 1.7 | 0.0 | 42 |
| Hononega-Varsity_... | C_zoom_stabilized | 0.0807 | 13 | 0.1 | 0.0 | 0.1 | 0.0 | 14 |
| Hononega-Varsity_... | D_zoom_stabilized_torso_38 | 0.1995 | 439 | 6.4 | 0.0 | 6.4 | 0.0 | 134 |
| IMG_3627.MOV | A_baseline_dc | 0.0488 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3627.MOV | B_torso_38 | 0.1676 | 57 | 1.1 | 0.0 | 1.1 | 0.0 | 66 |
| IMG_3627.MOV | C_zoom_stabilized | 0.0478 | 3 | 0.1 | 0.0 | 0.1 | 0.0 | 7 |
| IMG_3627.MOV | D_zoom_stabilized_torso_38 | 0.199 | 261 | 5.1 | 0.0 | 5.1 | 0.0 | 219 |
| IMG_3629.mkv | A_baseline_dc | 0.0827 | 99 | 1.2 | 0.5 | 1.0 | 0.0 | 91 |
| IMG_3629.mkv | B_torso_38 | 0.1977 | 334 | 3.3 | 0.4 | 2.9 | 0.0 | 78 |
| IMG_3629.mkv | C_zoom_stabilized | 0.1184 | 494 | 4.4 | 1.1 | 3.7 | 0.0 | 240 |
| IMG_3629.mkv | D_zoom_stabilized_torso_38 | 0.2002 | 1179 | 10.5 | 0.9 | 9.6 | 0.0 | 382 |
| IMG_3823.MP4 | A_baseline_dc | 0.0332 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3823.MP4 | B_torso_38 | 0.1269 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3823.MP4 | C_zoom_stabilized | 0.0327 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3823.MP4 | D_zoom_stabilized_torso_38 | 0.123 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3830.MP4 | A_baseline_dc | 0.0336 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3830.MP4 | B_torso_38 | 0.1508 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3830.MP4 | C_zoom_stabilized | 0.0369 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| IMG_3830.MP4 | D_zoom_stabilized_torso_38 | 0.1907 | 179 | 5.9 | 0.0 | 5.9 | 0.0 | 68 |

## Zoom stabilization diagnostics

| Video | Variant | ZoomBlocks | Trans% | Settle% | Normal% | CropHVar | Size |
| --- | --- | --- | --- | --- | --- | --- | --- |
| canon_60d_600m_zo... | A_baseline_dc | 40 | 3.8 | 49.0 | 47.2 | 1129.9 | 616x346 |
| canon_60d_600m_zo... | B_torso_38 | 40 | 3.8 | 49.0 | 47.2 | 1129.9 | 616x346 |
| canon_60d_600m_zo... | C_zoom_stabilized | 40 | 3.8 | 49.0 | 47.2 | 675.5 | 614x346 |
| canon_60d_600m_zo... | D_zoom_stabilized_torso_38 | 40 | 3.8 | 49.0 | 47.2 | 675.5 | 614x346 |
| Hononega-Orion_60... | A_baseline_dc | 42 | 3.7 | 21.7 | 74.6 | 33458.3 | 994x558 |
| Hononega-Orion_60... | B_torso_38 | 42 | 3.7 | 21.7 | 74.6 | 33458.3 | 994x558 |
| Hononega-Orion_60... | C_zoom_stabilized | 42 | 3.7 | 21.7 | 74.6 | 28604.1 | 878x494 |
| Hononega-Orion_60... | D_zoom_stabilized_torso_38 | 42 | 3.7 | 21.7 | 74.6 | 28604.1 | 878x494 |
| Hononega-Varsity_... | A_baseline_dc | 133 | 3.0 | 28.8 | 68.2 | 26683.4 | 916x516 |
| Hononega-Varsity_... | B_torso_38 | 133 | 3.0 | 28.8 | 68.2 | 26683.4 | 916x516 |
| Hononega-Varsity_... | C_zoom_stabilized | 133 | 3.0 | 28.8 | 68.2 | 19607.3 | 844x474 |
| Hononega-Varsity_... | D_zoom_stabilized_torso_38 | 133 | 3.0 | 28.8 | 68.2 | 19607.3 | 844x474 |
| IMG_3627.MOV | A_baseline_dc | 28 | 1.2 | 19.5 | 79.3 | 14431.6 | 484x272 |
| IMG_3627.MOV | B_torso_38 | 28 | 1.2 | 19.5 | 79.3 | 14431.6 | 484x272 |
| IMG_3627.MOV | C_zoom_stabilized | 28 | 1.2 | 19.5 | 79.3 | 10161.5 | 478x268 |
| IMG_3627.MOV | D_zoom_stabilized_torso_38 | 28 | 1.2 | 19.5 | 79.3 | 10161.5 | 478x268 |
| IMG_3629.mkv | A_baseline_dc | 81 | 1.9 | 20.5 | 77.6 | 88382.7 | 580x326 |
| IMG_3629.mkv | B_torso_38 | 81 | 1.9 | 20.5 | 77.6 | 88382.7 | 580x326 |
| IMG_3629.mkv | C_zoom_stabilized | 81 | 1.9 | 20.5 | 77.6 | 79746.2 | 578x324 |
| IMG_3629.mkv | D_zoom_stabilized_torso_38 | 81 | 1.9 | 20.5 | 77.6 | 79746.2 | 578x324 |
| IMG_3823.MP4 | A_baseline_dc | 29 | 3.7 | 18.4 | 77.9 | 72.4 | 356x200 |
| IMG_3823.MP4 | B_torso_38 | 29 | 3.7 | 18.4 | 77.9 | 72.4 | 356x200 |
| IMG_3823.MP4 | C_zoom_stabilized | 29 | 3.7 | 18.4 | 77.9 | 198.0 | 356x200 |
| IMG_3823.MP4 | D_zoom_stabilized_torso_38 | 29 | 3.7 | 18.4 | 77.9 | 198.0 | 356x200 |
| IMG_3830.MP4 | A_baseline_dc | 82 | 9.2 | 52.9 | 37.8 | 4044.2 | 356x200 |
| IMG_3830.MP4 | B_torso_38 | 82 | 9.2 | 52.9 | 37.8 | 4044.2 | 356x200 |
| IMG_3830.MP4 | C_zoom_stabilized | 82 | 9.2 | 52.9 | 37.8 | 492.9 | 356x200 |
| IMG_3830.MP4 | D_zoom_stabilized_torso_38 | 82 | 9.2 | 52.9 | 37.8 | 492.9 | 356x200 |

## Torso composition diagnostics

| Video | Variant | TorsoMed | TorsoP95 | Upper% |
| --- | --- | --- | --- | --- |
| canon_60d_600m_zo... | A_baseline_dc | 0.499 | 0.531 | 0.3 |
| canon_60d_600m_zo... | B_torso_38 | 0.379 | 0.417 | 96.4 |
| canon_60d_600m_zo... | C_zoom_stabilized | 0.499 | 0.531 | 0.2 |
| canon_60d_600m_zo... | D_zoom_stabilized_torso_38 | 0.378 | 0.416 | 96.1 |
| Hononega-Orion_60... | A_baseline_dc | 0.5 | 0.513 | 0.1 |
| Hononega-Orion_60... | B_torso_38 | 0.379 | 0.418 | 95.8 |
| Hononega-Orion_60... | C_zoom_stabilized | 0.5 | 0.516 | 0.1 |
| Hononega-Orion_60... | D_zoom_stabilized_torso_38 | 0.376 | 0.42 | 94.9 |
| Hononega-Varsity_... | A_baseline_dc | 0.5 | 0.515 | 0.1 |
| Hononega-Varsity_... | B_torso_38 | 0.38 | 0.42 | 94.8 |
| Hononega-Varsity_... | C_zoom_stabilized | 0.5 | 0.516 | 0.2 |
| Hononega-Varsity_... | D_zoom_stabilized_torso_38 | 0.377 | 0.421 | 94.4 |
| IMG_3627.MOV | A_baseline_dc | 0.5 | 0.511 | 0.1 |
| IMG_3627.MOV | B_torso_38 | 0.381 | 0.43 | 90.7 |
| IMG_3627.MOV | C_zoom_stabilized | 0.5 | 0.511 | 0.1 |
| IMG_3627.MOV | D_zoom_stabilized_torso_38 | 0.381 | 0.433 | 82.7 |
| IMG_3629.mkv | A_baseline_dc | 0.5 | 0.515 | 0.2 |
| IMG_3629.mkv | B_torso_38 | 0.381 | 0.443 | 87.7 |
| IMG_3629.mkv | C_zoom_stabilized | 0.5 | 0.524 | 0.3 |
| IMG_3629.mkv | D_zoom_stabilized_torso_38 | 0.381 | 0.469 | 83.7 |
| IMG_3823.MP4 | A_baseline_dc | 0.5 | 0.517 | 0.0 |
| IMG_3823.MP4 | B_torso_38 | 0.443 | 0.462 | 20.4 |
| IMG_3823.MP4 | C_zoom_stabilized | 0.5 | 0.516 | 0.0 |
| IMG_3823.MP4 | D_zoom_stabilized_torso_38 | 0.443 | 0.462 | 19.1 |
| IMG_3830.MP4 | A_baseline_dc | 0.5 | 0.516 | 0.0 |
| IMG_3830.MP4 | B_torso_38 | 0.427 | 0.452 | 38.2 |
| IMG_3830.MP4 | C_zoom_stabilized | 0.5 | 0.517 | 0.0 |
| IMG_3830.MP4 | D_zoom_stabilized_torso_38 | 0.427 | 0.452 | 36.9 |

## Pass criteria

- C reduces `height_jerk_p95` on IMG_3702 vs A
- C produces smaller output resolution on multimodal videos (IMG_3702, IMG_3629)
- C does not regress on canon_60d
- B places torso measurably higher in frame than A
- D combines both improvements without regression
- `bad_frame_fraction < 0.05` (< 5%)
- `height_jerk_p95 < 5.0`

## How to review

1. Watch the `_clip*.mkv` files side by side
2. Rate each 0-3 for: jitter, zoom pumping, drift, shake
3. Compare your ratings against the metrics in the table
4. Full encodes are available for promising variants
