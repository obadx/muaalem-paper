## Segmentation of Recitations

Accurate segmentation is a critical preprocessing step, as Tajweed rules are directly influenced by pause points (وقف). To address this, we initially evaluated open-source Voice Activity Detection (VAD) models, including SileroVAD [Silero VAD] and PyAnnotate [Plaquet23]. However, their performance on Quranic recitations was unsatisfactory due to the unique acoustic and prosodic characteristics of Tilawah.

Consequently, we developed a custom segmentation model by fine-tuning the Wav2Vec2-BERT architecture [barrault2023seamless] for frame-level classification, specifically optimized for Quranic audio.

### Preparation of Segmenter Training Data

To create a training dataset, we selected *Masahif* from the [EveryAyah](https://everyayah.com/) database that were compatible with SileroVAD v4. This source provided pre-segmented recitations at the verse (ayah) level, which served as our ground truth.

For each Moshaf, we tuned the following segmentation parameters to optimize alignment with the ground truth:
- **Threshold:** Detection confidence level.
- **Minimum Silence Duration:** Durations below this value trigger segment merging.
- **Minimum Speech Duration:** Segments shorter than this value are discarded.
- **Padding:** Duration added to the beginning and end of each detected segment.

The resulting dataset, comprising eight complete *Masahif*, is summarized in Table [table_segmenter_data].

| Reciter Name (Arabic) | ID | URL | Window Size (Samples) | Threshold | Min Silence (ms) | Min Speech (ms) | Pad (ms) |
| :--- | :--: | :--- | :---: | :---: | :---: | :---: | :---: |
| محمود خليل الحصري | 0 | [Download](https://everyayah.com/data/Husary_128kbps/000_versebyverse.zip) | 1536 | 0.3 | 500 | 1000 | 40 |
| محمد صديق المنشاوي | 1 | [Download](https://everyayah.com/data/Minshawy_Murattal_128kbps/000_versebyverse.zip) | 1536 | 0.3 | 400 | 1000 | 20 |
| عبد الباسط عبد الصمد | 2 | [Download](https://everyayah.com/data/Abdul_Basit_Murattal_192kbps/000_versebyverse.zip) | 1536 | 0.3 | 400 | 700 | 20 |
| محمود علي البنا | 3 | [Download](https://everyayah.com/data/mahmoud_ali_al_banna_32kbps/000_versebyverse.zip) | 1536 | 0.3 | 400 | 700 | 20 |
| على الحذيفي | 5 | [Download](https://everyayah.com/data/Hudhaify_128kbps/000_versebyverse.zip) | 1536 | 0.3 | 350 | 700 | 5 |
| أيمن رشدي سويد | 6 | [Download](https://everyayah.com/data/Ayman_Sowaid_64kbps/000_versebyverse.zip) | 1536 | 0.3 | 500 | 1000 | 10 |
| محمد أيوب | 7 | [Download](https://everyayah.com/data/Muhammad_Ayyoub_128kbps/000_versebyverse.zip) | 1536 | 0.3 | 400 | 1000 | 10 |
| إبراهيم الأخضر | 8 | [Download](https://everyayah.com/data/Ibrahim_Akhdar_32kbps/000_versebyverse.zip) | 1536 | 0.3 | 390 | 700 | 30 |
[table_segmenter_data]
*Table : Dataset used for training the custom segmenter, consisting of eight complete Masahif with tuned parameters.*

#### Data Augmentation

To improve model robustness and generalize across various recording conditions, we employed data augmentation using the [Audiomentations] library. The augmentation strategy replicated SileroVAD's noise profile and was applied to 40% of the samples. With additional:
* `TimeStretch` (0.8x-1.5x) to simulate recitation speeds  
* Sliding window truncation (1-second windows) for long samples instead of exclusion  

### Segmenter Training

The Wav2Vec2BERT model was fine-tuned for frame-level classification over a single epoch. The architecture of our VAD model compared to standard streaming models is illustrated in the figure below.


![Architectural comparison of our VAD model versus standard streaming models](../figures/vad-arch.png)
*Figure 9: Architecture of the fine-tuned Wav2Vec2-BERT model for frame classification, compared to a standard streaming model.*

The model's performance on unseen *Masahif* demonstrated high accuracy, as shown in Table [table_vad_results].

| Metric | Value |
| :--- | :---: |
| Test Loss | 0.0277 |
| Test Accuracy | 0.9935 |
| Test F1 Score | 0.99476 |
[table_vad_results]
*Evaluation results of the segmentation model on a held-out test set of Masahif, showing superior performance. The quality of the segmenter was validated by processing our entire dataset, where it maintained this high level of performance. The only exceptions were edge cases involving extremely fast recitation (*Hadr*), which is an expected limitation.*

### Python API

To make this tool accessible to the research community, we packaged the trained segmenter and published it as the open-source Python library **[recitations-segmenter](https://github.com/obadx/recitations-segmenter)**.

#### Library Installation

##### System Requirements
The library requires the following system dependencies:
*   [ffmpeg](https://ffmpeg.org/download.html)
*   [libsoundfile](https://github.com/libsndfile/libsndfile/releases)

###### Linux
```bash
sudo apt-get update
sudo apt-get install -y ffmpeg libsndfile1 portaudio19-dev
```

###### Windows & macOS
These dependencies can be installed via the Conda package manager:
```bash
conda create -n segment python=3.12
conda activate segment
conda install -c conda-forge ffmpeg libsndfile
```

###### Installing the Python Package
The library can be installed using `pip`:
```bash
pip install recitations-segmenter
```
Or using the modern `uv` package manager:
```bash
uv add recitations-segmenter
```

#### API Usage

The library provides a straightforward Python API. A complete usage example is provided below and is also available as a [Google Colab notebook][https://colab.research.google.com/drive/1-RuRQOj4l2MA_SG2p4m-afR7MAsT5I22?usp=sharing].


```python
from pathlib import Path
from recitations_segmenter import segment_recitations, read_audio, clean_speech_intervals
from transformers import AutoFeatureExtractor, AutoModelForAudioFrameClassification
import torch

if __name__ == '__main__':
    device = torch.device('cuda')
    dtype = torch.bfloat16

    # Load the pre-trained model and processor
    processor = AutoFeatureExtractor.from_pretrained("obadx/recitation-segmenter-v2")
    model = AutoModelForAudioFrameClassification.from_pretrained("obadx/recitation-segmenter-v2")
    model.to(device, dtype=dtype)

    # Load audio files
    file_paths = ['./assets/dussary_002282.mp3', './assets/hussary_053001.mp3']
    waves = [read_audio(p) for p in file_paths]

    # Perform segmentation
    sampled_outputs = segment_recitations(
        waves,
        model,
        processor,
        device=device,
        dtype=dtype,
        batch_size=8,
    )

    # Clean and print the results
    for out, path in zip(sampled_outputs, file_paths):
        clean_out = clean_speech_intervals(
            out.speech_intervals,
            out.is_complete,
            min_silence_duration_ms=30,
            min_speech_duration_ms=30,
            pad_duration_ms=30,
            return_seconds=True,
        )
        print(f'Speech Intervals of: {Path(path).name}: ')
        print(clean_out.clean_speech_intervals)
        print(f'Is Recitation Complete: {clean_out.is_complete}')
        print('-' * 40)
```

#### Command Line Interface

The library also features a Command Line Interface (CLI) for direct use without writing code. After installation, it can be run on any supported audio file:

```bash
# Using uvx without permanent installation
uvx recitations-segmenter alfateha.mp3

# Using the installed package
recitations-segmenter alfateha.mp3
```

The CLI extracts timestamps for pauses (Waqf) and outputs the results in two formats:
1.  A human-readable table in the terminal.
2.  A detailed JSON file written to `output/speech_intervals_<filename>.json`.

The JSON output contains the following structure:
```json
{
    "clean_speech_intervals": [[0.73, 5.29], ...],
    "speech_intervals": [[0.76, 5.26], ...],
    "is_complete": true
}
```
*   `clean_speech_intervals`: Refined start/end timestamps (in seconds) for each segment.
*   `speech_intervals`: Raw detected segments before cleaning.
*   `is_complete`: A boolean indicating if the recitation contains a complete final pause.

For a full description of CLI options and parameters, users can run `recitations-segmenter --help`.

#### Library Documentation (API Reference)

The core functions of the library are:

##### `segment_recitations(...)`
Segments a list of audio waveforms into speech intervals using the fine-tuned Wav2Vec2-BERT model.

**Key Arguments:**
*   `waves (list[torch.FloatTensor])`: List of audio waveforms.
*   `model`: Loaded Wav2Vec2BertForAudioFrameClassification model.
*   `processor`: Feature extractor for the model.
*   `batch_size (int)`: Number of samples processed simultaneously.
*   `device (torch.device)`: Processing device ('cuda' or 'cpu').
*   `dtype (torch.dtype)`: Data type for model computation (e.g., `torch.bfloat16`).

**Returns:**
*   `list[W2vBSegmentationOutput]`: A list of named tuples containing the raw `speech_intervals` (in samples) and a flag indicating if processing `is_complete`.

##### `clean_speech_intervals(...)`
Applies post-processing to the raw model output to refine the segments.

**Key Arguments:**
*   `speech_intervals (torch.LongTensor)`: Raw intervals output by the model.
*   `is_complete (bool)`: Completion flag from the model output.
*   `min_silence_duration_ms (int)`: Silence periods shorter than this are merged.
*   `min_speech_duration_ms (int)`: Speech segments shorter than this are removed.
*   `pad_duration_ms (int)`: Padding added to each segment's start and end.
*   `return_seconds (bool)`: If `True`, returns intervals in seconds instead of samples.

**Returns:**
*   `W2vBSegmentationOutput`: A named tuple containing the final `clean_speech_intervals`, the original `speech_intervals`, and the `is_complete` flag.

**Raises:**
*   `NoSpeechIntervals`: If no speech segments are detected.
*   `TooHighMinSpeechDuration`: If the filtering parameters remove all segments.
