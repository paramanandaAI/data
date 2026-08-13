# Nepali Music Video Annotation Dataset

## Overview

A dataset of Nepali music video clips with bounding-box-level annotations describing visual content in Nepali (Devanagari script) and English translations. The dataset is designed for training vision-language models on Nepali cultural content.

## Dataset Statistics

| Metric | Value |
|---|---|
| Source YouTube videos | 79 |
| Total video clips | 3,114 |
| Annotated clips | 256 |
| Total annotations | 256 |
| Unique annotators | 6 |
| Clip duration range | 3.0s – 10.0s |
| Average clip duration | 5.02s |
| Annotation period | May 29 – Jul 11, 2026 |

## Files

| File | Description |
|---|---|
| `db.sqlite3` | Original SQLite database (Django backend) |
| `videos_definition.csv` | All 3,114 video clips with source video metadata |
| `annotations_by_clip.csv` | 256 annotations in original Nepali (Romanized + Devanagari) |
| `annotations_nepali.csv` | 256 annotations transliterated to Devanagari script |
| `annotations_english.csv` | 256 annotations translated to English |
| `annotations_nepali_mimo_latest.csv` | 256 annotations in Devanagari script (MIMO generation) |
| `annotations_nepali_deepseek.csv` | 256 annotations in Devanagari script (DeepSeek generation) |
| `annotations_english_deepseek.csv` | 256 annotations translated to English (DeepSeek generation) |
| `id_mappings.json` | Anonymized ID mapping: real clip/annotation UUIDs → `clip_1`…`clip_256` / `annotation_1`…`annotation_256` |
| `annotated_videos_definition.csv` | Only the 256 annotated clips from `videos_definition.csv`, with `clip_id` renamed per `id_mappings.json` |

## CSV Schema

### videos_definition.csv / annotated_videos_definition.csv

| Column | Type | Description |
|---|---|---|
| `clip_id` | string | Clip identifier (UUID in `videos_definition.csv`; `clip_1`…`clip_256` in `annotated_videos_definition.csv`) |
| `start_time` | float | Clip start time in seconds |
| `end_time` | float | Clip end time in seconds |
| `duration` | float | Clip duration in seconds |
| `scene_index` | int | Scene index within source video |
| `annotation_count` | int | Number of annotations for this clip |
| `is_active` | bool | Whether clip is active |
| `clip_created_at` | datetime | Clip creation timestamp |
| `source_video_id` | string | Parent video identifier |
| `youtube_url` | string | YouTube video URL |
| `youtube_video_id` | string | YouTube video ID |
| `title` | string | Video title |
| `status` | string | Processing status (`done`) |
| `source_created_at` | datetime | Source video import timestamp |
| `processed_at` | datetime | Processing completion timestamp |

### annotations_nepali_*.csv / annotations_english_*.csv

| Column | Type | Description |
|---|---|---|
| `clip_id` | string | Clip identifier |
| `annotation_id` | string | Annotation identifier (UUID) |
| `subject_nepali` / `subject_english` | string | Who/what is in the scene |
| `action_nepali` / `action_english` | string | What is happening |
| `background_object_nepali` / `background_object_english` | string | Scene background/description |
| `note_nepali` / `note_english` | string | Additional notes |
| `submitted_at` | datetime | Annotation submission timestamp |
| `user_id` | int | Annotator user ID |
| `task_id` | string | Annotation task identifier |

## Annotation Fields

Each annotation contains three main fields:

- **Subject** – Describes the main people/objects visible (e.g., "A girl in traditional Tharu dress")
- **Action** – Describes what is happening (e.g., "Dancing with a lamp in hand")
- **Background** – Describes the scene setting (e.g., "Green hills with a village in the background")

## Source Videos

The 79 source videos are Nepali music videos and movie songs, including:

- Ekdev Limbu - Chameli
- Sayau Juni - Jagdish Samal & Rajina Rimal
- B-8EIGHT - Maichyang
- Bihanima - Sunil Bardewa
- PHOOL HOINA (ROSE Movie Song)
- Phool Pati Bhakera (BHAROSA Movie Song)
- Chari Ko Ghar Gudaima Bhaye (HAMI TEEN BHAI Movie Song)
- Dhankutako - Bhanu Oli
- And 71 more Nepali songs

## Language

- **Original annotations**: Mix of Romanized Nepali and Devanagari script
- **Nepali CSV**: All text transliterated to Devanagari script
- **English CSV**: Machine-translated from Nepali to English

## Database Schema (Django)

The source `db.sqlite3` is a Django database with the following relevant tables:

- `videos_sourcevideo` – Source YouTube video metadata (84 records)
- `videos_videoclip` – Extracted video clips (3,114 records)
- `videos_processingjoblog` – Clip extraction logs (84 records)
- `annotations_annotationtask` – Annotation task assignments (792 records)
- `annotations_annotation` – Completed annotations (256 records)
- `annotations_labeloption` – Label options (0 records)
- `accounts_userprofile` – Annotator profiles (6 records)

## ID Mapping & Anonymization

`id_mappings.json` provides deterministic, sequential aliases for the dataset IDs so the public release doesn't leak internal database UUIDs:

- `clip_id_mappings`: 256 real clip UUIDs → `clip_1` … `clip_256` (in annotation order)
- `annotation_id_mappings`: 256 real annotation UUIDs → `annotation_1` … `annotation_256`

Use the mapping when joining annotations to clips in the released files, e.g. rename `clip_id` in the annotation CSVs with `clip_id_mappings` so they link to `annotated_videos_definition.csv`.

## Usage

```python
import json
import pandas as pd

# Load annotated clip definitions (only annotated clips, renamed clip ids)
clips = pd.read_csv("annotated_videos_definition.csv")
print(clips["clip_id"].head())

# Map real ids to anonymized ids
with open("id_mappings.json", encoding="utf-8") as f:
    mapping = json.load(f)
clips["clip_id"] = clips["clip_id"].map(mapping["clip_id_mappings"])

# Load English annotations
df = pd.read_csv("annotations_english.csv")
print(df.head())
```

## Notes

- Each annotated clip has exactly one annotation
- Annotations describe visual content in natural language
- The dataset covers diverse Nepali cultural scenes: traditional dances, festivals, landscapes, attire, and daily life
- All clips are between 3 and 10 seconds in duration

## License

Dataset source: `D:\paramananda\db.sqlite3` (Django application database)
