## Transcribe Segmented Parts  

We employed Tarteel ASR [tarteel_whisper_ar_quran] (Whisper fine-tuned on Quranic recitations [radford2023robust]). To handle its 30-second limit, we used sliding window truncation (10-second windows), with verification in the next step. We used vlLM libarary becuase it is really fast thanks to Employing Paged Attension [kwon2023efficient].

