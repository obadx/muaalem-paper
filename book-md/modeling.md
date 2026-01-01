# Modeling  

Our Quran Phonetic Script produces two types of outputs: `phonemes` and `sifat` (which comprises 10 distinct attributes). We model this task as follows: Imagine processing an input speech utterance and simultaneously generating transcripts in multiple languages, such as Arabic, English, French, and German. Similarly, we implement a speech encoder with a separate linear output layer for each of our 11 levels (one for `phonemes` and 10 for the `sifat` attributes), resulting in 11 parallel transcription heads. We employ the Connectionist Temporal Classification (CTC) loss [graves2006ctc] without a language model, as our objective is to transcribe the actual pronunciation rather than the intended utterance. We refer to this architecture as **Multi-level CTC**.  

The total loss is computed as a weighted average of the CTC losses across all 11 levels. The `phonemes` level is assigned a weight of 0.4 due to its larger vocabulary size (43 symbols), while the remaining levels are weighted proportionally lower:

$$ \text{loss} = \sum_{i} \left( \text{level\_weight}_i \cdot \text{CTC\_level}_i \right) $$

[equation_multilevel_ctc]
We used a weight of 0.4 for the `phonemes` level, 0.0605 for both `shidda_or_rakhawa` and `tafkheem_or_taqeeq`, and 0.059875 for each of the remaining levels.

![Multi-level CTC architecture with 11 output heads, each computing a CTC loss, combined via weighted average](./figures/multi-level-ctc.png)  

We fine-tuned Facebook's Wav2Vec2-Bert model [barrault2023seamless] for a single epoch using a constant learning rate of `5e-5`. Data augmentations were applied using the `audiomentations` library [Audiomentations], mirroring the augmentations used in Silero VAD [Silero VAD], with additional augmentations including `TimeStretch` and `GainTransition`. Samples longer than 30 seconds were filtered out to optimize GPU memory utilization—this resulted in the exclusion of only 3k samples from the 250k training set.  

![Distribution of recitation lengths (in seconds) across the dataset](./figures/audio-lens.png)  

Training was conducted on a single H200 GPU with 141 GB of memory and completed in approximately 7 hours.

## Resources and Reproducibility  

We release inference code, trained checkpoints, and configuration at https://obadx.github.io/quran-muaalem/en/. The Quran Phonetic Script implementation and phoneticization tools are available at https://github.com/obadx/quran-transcript. Dataset preparation and segmentation tools are released at https://github.com/obadx/prepare-quran-dataset and https://github.com/obadx/recitations-segmenter, while the final datasets are hosted on Hugging Face (https://huggingface.co/datasets/obadx/quran-muaalem and https://huggingface.co/datasets/obadx/qdat_bench).  
