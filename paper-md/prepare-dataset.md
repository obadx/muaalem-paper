## Data Preparation  

To prepare the data, we first defined selection criteria. We aimed to collect recitations from the best reciters worldwide to serve as references for judging Quran learners. In our study, we considered only *Hafs* riwayah (رواية حفص) as it's the most popular recitation method globally. Recognizing that manual data annotation requires significant effort and time, we created a 98% automated pipeline for data collection. The steps are:  
(1) Choose a digitized Quran script as the project foundation  
(2) Define criteria for *Hafs* methodology  
(3) Collect expert recitations  
(4) Segment recitations at pause points (وقف)  
(5) Transcribe segments  
(6) Validate data through *Tasmee* (تسميع) Algrithm
(7) Develop Quran Phonetic Script  

We define a *Moshaf* as a complete Quran recitation (chapters 1-114) by a specific reciter. Statistics are summarized below:  

| Moshaf ID | Hours         | Length |
|-----------|---------------|--------|
| 0.0       | 28.47721296   | 9133   |
| 0.1       | 40.31257093   | 10764  |
| 0.2       | 49.46541671   | 9971   |
| 0.3       | 37.18758118   | 12604  |
| 1.0       | 28.40784367   | 10939  |
| 2.0       | 51.04665234   | 9942   |
| 2.1       | 30.02847051   | 10394  |
| 3.0       | 25.19377593   | 10444  |
| 4.0       | 29.12333379   | 10994  |
| 5.0       | 28.01777693   | 11482  |
| 6.0       | 39.38568468   | 12435  |
| 7.0       | 28.25627201   | 9907   |
| 8.0       | 30.85935158   | 10330  |
| 9.0       | 27.95178738   | 10642  |
| 11.0      | 24.00685052   | 10363  |
| 12.0      | 33.42429862   | 9880   |
| 13.0      | 33.99108879   | 9377   |
| 19.0      | 30.11410843   | 11278  |
| 22.0      | 28.10947704   | 10332  |
| 24.0      | 28.51243509   | 9868   |
| 25.0      | 16.92910042   | 7922   |
| 26.0      | 30.44461112   | 11565  |
| 26.1      | 32.71190443   | 11850  |
| 27.0      | 28.05097968   | 11213  |
| 28.0      | 31.05318768   | 10535  |
| 29.0      | 27.78900316   | 11061  |
| 30.0      | 29.14366461   | 11312  |
| **Total** | **847.9944402** | **286537** |

*(Table preserved with original values)*

### Choose a Digitized Version of the Holy Quran  

The Quran has multiple digitized versions including [Tanzil](https://tanzil.net) and [King Fahd Complex](https://qurancomplex.gov.sa). We chose Tanzil because:  
* It uses standard Unicode characters  
* Contains both *Imlaei* and *Uthmani* versions  
* Maintains high accuracy  

We excluded KFGQPC due to its evolving/unstable nature compared to Tanzil.

### Define Variant Criteria for Hafs  

*Hafs* riwayah contains variants, e.g., *Madd Al-Munfasil* (مد المنفصل) can extend 2, 4, 5, or 6 beats. We rigorously defined these variants through Qira'at literature [al-dabbaa], summarized in this table below. Each Moshaf has a `MoshafAttributes` card manually annotated through dedicated effort.

|Attribute Name|Arabic Name|Values|Default Value|More Info|
|-|-|-|-|-|
|rewaya|الرواية|- `hafs` (`حفص`)<br>||The type of the quran Rewaya.|
|recitation_speed|سرعة التلاوة|- `mujawad` (`مجود`)<br>- `above_murattal` (`فويق المرتل`)<br>- `murattal` (`مرتل`)<br>- `hadr` (`حدر`)<br>|`murattal` (`مرتل`)|The recitation speed sorted from slowest to the fastest سرعة التلاوة مرتبة من الأبطأ إلي الأسرع|
|takbeer|التكبير|- `no_takbeer` (`لا تكبير`)<br>- `beginning_of_sharh` (`التكبير من أول الشرح لأول الناس`)<br>- `end_of_doha` (`التكبير من آخر الضحى لآخر الناس`)<br>- `general_takbeer` (`التكبير أول كل سورة إلا التوبة`)<br>|`no_takbeer` (`لا تكبير`)|The ways to add takbeer (الله أكبر) after Istiaatha (استعاذة) and between end of the surah and beginning of the surah. `no_takbeer`: "لا تكبير" — No Takbeer (No proclamation of greatness, i.e., there is no Takbeer recitation) `beginning_of_sharh`: "التكبير من أول الشرح لأول الناس" — Takbeer from the beginning of Surah Ash-Sharh to the beginning of Surah An-Nas `end_of_dohaf`: "التكبير من آخر الضحى لآخر الناس" — Takbeer from the end of Surah Ad-Duha to the end of Surah An-Nas `general_takbeer`: "التكبير أول كل سورة إلا التوبة" — Takbeer at the beginning of every Surah except Surah At-Tawbah|
|madd_monfasel_len|مد المنفصل|- `2`<br>- `3`<br>- `4`<br>- `5`<br>|| The length of Mad Al Monfasel "مد النفصل" for Hafs Rewaya.|
|madd_mottasel_len|مقدار المد المتصل|- `4`<br>- `5`<br>- `6`<br>|| The length of Mad Al Motasel "مد المتصل" for Hafs.|
|madd_mottasel_waqf|مقدار المد المتصل وقفا|- `4`<br>- `5`<br>- `6`<br>|| The length of Madd Almotasel at pause for Hafs.. Example "السماء".|
|madd_aared_len|مقدار المد العارض|- `2`<br>- `4`<br>- `6`<br>|| The length of Mad Al Aared "مد العارض للسكون".|
|madd_alleen_len|مقدار مد اللين|- `2`<br>- `4`<br>- `6`<br>|`None`|The length of the Madd al-Leen when stopping at the end of a word (for a sakin waw or ya preceded by a letter with a fatha) should be less than or equal to the length of Madd al-'Arid (the temporary stretch due to stopping). **Default Value is equal to `madd_aared_len`**. مقدرا مع اللين عن القوف (للواو الساكنة والياء الساكنة وقبلها حرف مفتوح) ويجب أن يكون مقدار مد اللين أقل من أو يساوي مع العارض|
|ghonna_lam_and_raa|غنة اللام و الراء|- `ghonna` (`غنة`)<br>- `no_ghonna` (`لا غنة`)<br>|`no_ghonna` (`لا غنة`)|The ghonna for merging (Idghaam) noon with Lam and Raa for Hafs.|
|meem_aal_imran|ميم آل عمران في قوله تعالى: {الم الله} وصلا|- `waqf` (`وقف`)<br>- `wasl_2` (`فتح الميم ومدها حركتين`)<br>- `wasl_6` (`فتح الميم ومدها ستة حركات`)<br>|`waqf` (`وقف`)|The ways to recite the word meem Aal Imran (الم الله) at connected recitation. `waqf`: Pause with a prolonged madd (elongation) of 6 harakat (beats). `wasl_2` Pronounce "meem" with fathah (a short "a" sound) and stretch it for 2 harakat. `wasl_6` Pronounce "meem" with fathah and stretch it for 6 harakat.|
|madd_yaa_alayn_alharfy|مقدار   المد اللازم الحرفي للعين|- `2`<br>- `4`<br>- `6`<br>|`6`| The length of Lzem Harfy of Yaa in letter Al-Ayen Madd "المد الحرفي اللازم لحرف العين" in surar: Maryam "مريم", AlShura "الشورى".|
|saken_before_hamz|الساكن قبل الهمز|- `tahqeek` (`تحقيق`)<br>- `general_sakt` (`سكت عام`)<br>- `local_sakt` (`سكت خاص`)<br>|`tahqeek` (`تحقيق`)|The ways of Hafs for saken before hamz. "The letter with sukoon before the hamzah (ء)".And it has three forms: full articulation (`tahqeeq`), general pause (`general_sakt`), and specific pause (`local_skat`).|
|sakt_iwaja|السكت عند عوجا في الكهف|- `sakt` (`سكت`)<br>- `waqf` (`وقف`)<br>- `idraj` (`إدراج`)<br>|`waqf` (`وقف`)|The ways to recite the word "عوجا" (Iwaja). `sakt` means slight pause. `idraj` means not `sakt`. `waqf`:  means full pause, so we can not determine weither the reciter uses `sakt` or `idraj` (no sakt).|
|sakt_marqdena|السكت عند مرقدنا  في يس|- `sakt` (`سكت`)<br>- `waqf` (`وقف`)<br>- `idraj` (`إدراج`)<br>|`waqf` (`وقف`)|The ways to recite the word "مرقدنا" (Marqadena) in Surat Yassen. `sakt` means slight pause. `idraj` means not `sakt`. `waqf`:  means full pause, so we can not determine weither the reciter uses `sakt` or `idraj` (no sakt).|
|sakt_man_raq|السكت عند  من راق في القيامة|- `sakt` (`سكت`)<br>- `waqf` (`وقف`)<br>- `idraj` (`إدراج`)<br>|`sakt` (`سكت`)|The ways to recite the word "من راق" (Man Raq) in Surat Al Qiyama. `sakt` means slight pause. `idraj` means not `sakt`. `waqf`:  means full pause, so we can not determine weither the reciter uses `sakt` or `idraj` (no sakt).|
|sakt_bal_ran|السكت عند  بل ران في  المطففين|- `sakt` (`سكت`)<br>- `waqf` (`وقف`)<br>- `idraj` (`إدراج`)<br>|`sakt` (`سكت`)|The ways to recite the word "بل ران" (Bal Ran) in Surat Al Motaffin. `sakt` means slight pause. `idraj` means not `sakt`. `waqf`:  means full pause, so we can not determine weither the reciter uses `sakt` or `idraj` (no sakt).|
|sakt_maleeyah|وجه  قوله تعالى {ماليه هلك} بالحاقة|- `sakt` (`سكت`)<br>- `waqf` (`وقف`)<br>- `idgham` (`إدغام`)<br>|`waqf` (`وقف`)|The ways to recite the word {ماليه هلك} in Surah Al-Ahqaf. `sakt` means slight pause. `idgham` Assimilation of the letter 'Ha' (ه) into the letter 'Ha' (ه) with complete assimilation.`waqf`:  means full pause, so we can not determine weither the reciter uses `sakt` or `idgham`.|
|between_anfal_and_tawba|وجه بين الأنفال والتوبة|- `waqf` (`وقف`)<br>- `sakt` (`سكت`)<br>- `wasl` (`وصل`)<br>|`waqf` (`وقف`)|The ways to recite end of Surah Al-Anfal and beginning of Surah At-Tawbah.|
|noon_and_yaseen|الإدغام والإظهار في النون عند الواو من قوله تعالى: {يس والقرآن}و {ن والقلم}|- `izhar` (`إظهار`)<br>- `idgham` (`إدغام`)<br>|`izhar` (`إظهار`)|Weither to merge noon of both: {يس} and {ن} with (و) "`idgham`" or not "`izhar`".|
|yaa_ataan| إثبات الياء وحذفها وقفا في قوله تعالى {آتان} بالنمل|- `wasl` (`وصل`)<br>- `hadhf` (`حذف`)<br>- `ithbat` (`إثبات`)<br>|`wasl` (`وصل`)|The affirmation and omission of the letter 'Yaa' in the pause of the verse {آتاني} in Surah An-Naml.`wasl`: means connected recitation without pasuding as (آتانيَ).`hadhf`: means deletion of letter (ي) at puase so recited as (آتان).`ithbat`: means confirmation reciting letter (ي) at puase as (آتاني).|
|start_with_ism|وجه البدأ بكلمة {الاسم} في سورة الحجرات|- `wasl` (`وصل`)<br>- `lism` (`لسم`)<br>- `alism` (`ألسم`)<br>|`wasl` (`وصل`)|The ruling on starting with the word {الاسم} in Surah Al-Hujurat.`lism` Recited as (لسم) at the beginning. `alism` Recited as (ألسم). ath the beginning`wasl`: means completing recitaion without paussing as normal, So Reciting is as (بئس لسم).|
|yabsut|السين والصاد في قوله تعالى: {والله يقبض ويبسط} بالبقرة|- `seen` (`سين`)<br>- `saad` (`صاد`)<br>|`seen` (`سين`)|The ruling on pronouncing `seen` (س) or `saad` (ص) in the verse {والله يقبض ويبسط} in Surah Al-Baqarah.|
|bastah|السين والصاد في قوله تعالى:  {وزادكم في الخلق بسطة} بالأعراف|- `seen` (`سين`)<br>- `saad` (`صاد`)<br>|`seen` (`سين`)|The ruling on pronouncing `seen` (س) or `saad` (ص ) in the verse {وزادكم في الخلق بسطة} in Surah Al-A'raf.|
|almusaytirun|السين والصاد في قوله تعالى {أم هم المصيطرون} بالطور|- `seen` (`سين`)<br>- `saad` (`صاد`)<br>|`saad` (`صاد`)|The pronunciation of `seen` (س) or `saad` (ص ) in the verse {أم هم المصيطرون} in Surah At-Tur.|
|bimusaytir|السين والصاد في قوله تعالى:  {لست عليهم بمصيطر} بالغاشية|- `seen` (`سين`)<br>- `saad` (`صاد`)<br>|`saad` (`صاد`)|The pronunciation of `seen` (س) or `saad` (ص ) in the verse {لست عليهم بمصيطر} in Surah Al-Ghashiyah.|
|tasheel_or_madd|همزة الوصل في قوله تعالى: {آلذكرين} بموضعي الأنعام و{آلآن} موضعي يونس و{آلله} بيونس والنمل|- `tasheel` (`تسهيل`)<br>- `madd` (`مد`)<br>|`madd` (`مد`)| Tasheel of Madd "وجع التسهيل أو المد" for 6 words in The Holy Quran: "ءالذكرين", "ءالله", "ءائن".|
|yalhath_dhalik|الإدغام وعدمه في قوله تعالى: {يلهث ذلك} بالأعراف|- `izhar` (`إظهار`)<br>- `idgham` (`إدغام`)<br>- `waqf` (`وقف`)<br>|`idgham` (`إدغام`)|The assimilation (`idgham`) and non-assimilation (`izhar`) in the verse {يلهث ذلك} in Surah Al-A'raf. `waqf`: means the rectier has paused on (يلهث)|
|irkab_maana|الإدغام والإظهار في قوله تعالى: {اركب معنا} بهود|- `izhar` (`إظهار`)<br>- `idgham` (`إدغام`)<br>- `waqf` (`وقف`)<br>|`idgham` (`إدغام`)|The assimilation and clear pronunciation in the verse {اركب معنا} in Surah Hud.This refers to the recitation rules concerning whether the letter "Noon" (ن) is assimilated into the following letter or pronounced clearly when reciting this specific verse. `waqf`: means the rectier has paused on (اركب)|
|noon_tamnna| الإشمام والروم (الاختلاس) في قوله تعالى {لا تأمنا على يوسف}|- `ishmam` (`إشمام`)<br>- `rawm` (`روم`)<br>|`ishmam` (`إشمام`)|The nasalization (`ishmam`) or the slight drawing (`rawm`) in the verse {لا تأمنا على يوسف}|
|harakat_daaf|حركة الضاد (فتح أو ضم) في قوله تعالى {ضعف} بالروم|- `fath` (`فتح`)<br>- `dam` (`ضم`)<br>|`fath` (`فتح`)|The vowel movement of the letter 'Dhad' (ض) (whether with `fath` or `dam`) in the word {ضعف} in Surah Ar-Rum.|
|alif_salasila|إثبات الألف وحذفها وقفا في قوله تعالى: {سلاسلا} بسورة الإنسان|- `hadhf` (`حذف`)<br>- `ithbat` (`إثبات`)<br>- `wasl` (`وصل`)<br>|`wasl` (`وصل`)|Affirmation and omission of the 'Alif' when pausing in the verse {سلاسلا} in Surah Al-Insan.This refers to the recitation rule regarding whether the final "Alif" in the word "سلاسلا" is pronounced (affirmed) or omitted when pausing (waqf) at this word during recitation in the specific verse from Surah Al-Insan. `hadhf`: means to remove alif (ا) during puase as (سلاسل) `ithbat`: means to recite alif (ا) during puase as (سلاسلا) `wasl` means completing the recitation as normal without pausing, so recite it as (سلاسلَ وأغلالا)|
|idgham_nakhluqkum|إدغام القاف في الكاف إدغاما ناقصا أو كاملا {نخلقكم} بالمرسلات|- `idgham_kamil` (`إدغام كامل`)<br>- `idgham_naqis` (`إدغام ناقص`)<br>|`idgham_kamil` (`إدغام كامل`)|Assimilation of the letter 'Qaf' into the letter 'Kaf,' whether incomplete (`idgham_naqis`) or complete (`idgham_kamil`), in the verse {نخلقكم} in Surah Al-Mursalat.|
|raa_firq|التفخيم والترقيق في راء {فرق} في الشعراء وصلا|- `waqf` (`وقف`)<br>- `tafkheem` (`تفخيم`)<br>- `tarqeeq` (`ترقيق`)<br>|`tafkheem` (`تفخيم`)|Emphasis and softening of the letter 'Ra' in the word {فرق} in Surah Ash-Shu'ara' when connected (wasl).This refers to the recitation rules concerning whether the letter "Ra" (ر) in the word "فرق"  is pronounced with emphasis (`tafkheem`) or softening (`tarqeeq`) when reciting the specific verse from Surah Ash-Shu'ara' in connected speech. `waqf`: means pasuing so we only have one way (tafkheem of Raa)|
|raa_alqitr|التفخيم والترقيق في راء {القطر} في سبأ وقفا|- `wasl` (`وصل`)<br>- `tafkheem` (`تفخيم`)<br>- `tarqeeq` (`ترقيق`)<br>|`wasl` (`وصل`)|Emphasis and softening of the letter 'Ra' in the word {القطر} in Surah Saba' when pausing (waqf).This refers to the recitation rules regarding whether the letter "Ra" (ر) in the word "القطر" is pronounced with emphasis (`tafkheem`) or softening (`tarqeeq`) when pausing at this word in Surah Saba'. `wasl`: means not pasuing so we only have one way (tarqeeq of Raa)|
|raa_misr|التفخيم والترقيق في راء {مصر} في يونس وموضعي يوسف والزخرف  وقفا|- `wasl` (`وصل`)<br>- `tafkheem` (`تفخيم`)<br>- `tarqeeq` (`ترقيق`)<br>|`wasl` (`وصل`)|Emphasis and softening of the letter 'Ra' in the word {مصر} in Surah Yunus, and in the locations of Surah Yusuf and Surah Az-Zukhruf when pausing (waqf).This refers to the recitation rules regarding whether the letter "Ra" (ر) in the word "مصر" is pronounced with emphasis (`tafkheem`) or softening (`tarqeeq`) at the specific pauses in these Surahs. `wasl`: means not pasuing so we only have one way (tafkheem of Raa)|
|raa_nudhur|التفخيم والترقيق  في راء {نذر} بالقمر وقفا|- `wasl` (`وصل`)<br>- `tafkheem` (`تفخيم`)<br>- `tarqeeq` (`ترقيق`)<br>|`tafkheem` (`تفخيم`)|Emphasis and softening of the letter 'Ra' in the word {نذر} in Surah Al-Qamar when pausing (waqf).This refers to the recitation rules regarding whether the letter "Ra" (ر) in the word "نذر" is pronounced with emphasis (`tafkheem`) or softening (`tarqeeq`) when pausing at this word in Surah Al-Qamar. `wasl`: means not pasuing so we only have one way (tarqeeq of Raa)|
|raa_yasr|التفخيم والترقيق في راء {يسر} بالفجر و{أن أسر} بطه والشعراء و{فأسر} بهود والحجر والدخان  وقفا|- `wasl` (`وصل`)<br>- `tafkheem` (`تفخيم`)<br>- `tarqeeq` (`ترقيق`)<br>|`tarqeeq` (`ترقيق`)|Emphasis and softening of the letter 'Ra' in the word {يسر} in Surah Al-Fajr when pausing (waqf).This refers to the recitation rules regarding whether the letter "Ra" (ر) in the word "يسر" is pronounced with emphasis (`tafkheem`) or softening (`tarqeeq`) when pausing at this word in Surah Al-Fajr. `wasl`: means not pasuing so we only have one way (tarqeeq of Raa)|
|meem_mokhfah|هل الميم مخفاة أو مدغمة|- `meem` (`ميم`)<br>- `ikhfaa` (`إخفاء`)<br>|`ikhfaa` (`إخفاء`)|This is not a **standard** Hafs way but a disagreement between **scholars** in our century on how to **pronounce** **Ikhfa** for meem. Some **scholars** do full merging (`إدغام`) and the others open the **lips** a little bit (`إخفاء`). We did not want to add this, but some of the best reciters disagree about this.|

### Collect Expert Recitations  

We collected recitations from 22 world-class reciters with premium audio quality, totaling **893 hours** pre-filtering.  

![Database Collection Statistics](./figures/stats.png)  
![Reciters Statistics](./figures/reciter.png)  

We developed a web GUI using [Streamlit](https://streamlit.io/) that:  
* Downloads and extracts metadata for each track  
* Organizes data by Moshaf (each chapter as "001.mp3")  
* Annotates Moshaf attributes  

### Segment Recitations  

Since Tajweed rules are affected by pauses (وقف), accurate segmentation is crucial. We initially tested open-source Voice Activity Detection (VAD) models including SileroVAD [Silero VAD] and PyAnnotate [Plaquet23]. Poor Quran-specific performance led us to develop a custom segmenter by fine-tuning Wav2Vec2-BERT [barrault2023seamless] for frame-level classification.  

#### Preparing Segmenter Data  
We selected mosahf compatible with SileroVAD v4, using [EveryAyah](https://everyayah.com/) (pre-segmented by ayah) as ground truth. After tuning parameters per Moshaf:  
- Threshold  
- Minimum silence duration (merges segments)  
- Minimum speech duration (discards short segments)  
- Padding (added at segment boundaries)  

##### Data Augmentation  
Using the [Audiomentations] library, we replicated SileroVAD's noise setup on 40% of samples, adding:  
* `TimeStretch` (0.8x-1.5x) to simulate recitation speeds  
* Sliding window truncation (1-second windows) for long samples instead of exclusion  

#### Training Segmenter  
We fine-tuned Wav2Vec2-BERT for frame classification (1 epoch):  

![VAD architecture vs. standard streaming models](./figures/vad-arch.svg)  

Results on unseen mosahf:  
| Metric          | Value    |
|-----------------|----------|
| Test Loss       | 0.0277   |
| Test Accuracy   | 0.9935   |
| Test F1 Score   | 0.99476  |

### Transcribe Segmented Parts  
We employed Tarteel ASR [tarteel_whisper_ar_quran] (Whisper fine-tuned on Quranic recitations [radford2023robust]). To handle its 30-second limit, we used sliding window truncation (10-second windows), with verification in the next step.

### Verification of Segmentation and Transcription  
**Segmentation Verification**: Manual inspection of 50-75 random samples per Moshaf. Moshaf 25.0 was excluded due to poor segmentation.  

**Transcription Verification**: *Tasmeea*-inspired algorithm:  
1. Match segments to Quranic text  
2. Identify missing surah parts  
3. Manual correction  

#### Tasmeea Algorithm  
We excpet that the input recitations are 100% correct and erros comes from the ASR (Tarteel model)
**Inputs:**  
- `text_segments`: List of text segments \([s_1, s_2, \dots, s_n]\)  
- `sura_idx`: Index of target Quranic sura  
- `overlap_words`: Overlap tolerance (default: 6 words)  
- `window_words`: Search window size (default: 30 words)  
- `acceptance_ratio`: Minimum match threshold (default: 0.5)  
- Flags for special phrases (`include_istiaatha`, `include_bismillah`, `include_sadaka`)  

**Output:**  
List of tuples \((match, ratio)\) for each segment, where \(match\) is the best-matched Quranic segment or null.  

---

#### Steps:
1. **Initialize:**  
   - Start at the first verse (`aya`) of the sura.  
   - Set penalty adjustment \(penalty \leftarrow 0\).  

2. **For each segment \(s_i\) in \(text\_segments\):**  
   a. **Normalize \(s_i\):** Remove spaces/diacritics → \(norm\_text\).  
   b. **Define search bounds:**  
      - Min/max window length: \([window\_words - 10, window\_words + 10]\)  
      - Start position range: \([-(overlap + penalty), (overlap + \max(window\_words, max\_win) + penalty]\)  

   c. **Check special cases:**  
      - **Istiaatha:** Only for first segment if enabled.  
      - **Sadaka:** Only for last segment if enabled.  

   d. **Search for best match:**  
      For each possible start position \(p\) in range:  
        For each window size \(w\) in \([min\_win, max\_win]\):  
          - Extract candidate segment \(c\) from current verse at \((p, w)\).  
          - Compute normalized Levenshtein similarity:  
            \[
            \text{ratio} = 1 - \frac{\min(\text{edit\_distance}(norm\_text, c), |norm\_text|)}{|norm\_text|}
            \]  
          - Update best match if ratio improves (or tie: smaller \(|p|\)).  

   e. **Update state:**  
      - If no match or ratio \(< acceptance\_ratio\):  
          - Output (null, best_ratio)  
          - Increase penalty for next segment: \(penalty \leftarrow max\_win\)  
          - Move verse pointer by default step.  
      - Else:  
          - Output (best_match, best_ratio)  
          - Move verse pointer by \((best\_start, best\_window)\).  


**Complexity**: O(N·W·L²) where N=segments, W=window size, L=segment length  

#### Missing Parts Identification  
After matching, we catalogued missing Quranic portions per surah.  

#### Manual Correction  
We corrected transcription errors identified through the above process.  

