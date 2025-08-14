# Quran Phonetic Script  

We consider the Quran Phonetic Script to be the most valuable and important contribution of our work. By formalizing the assessment of Holy Quran pronunciation as an ASR problem represented through this script, we provide a comprehensive solution to the task.

## Motivation for Developing Quran Phonetic Script  

Modern Standard Arabic (MSA) orthography cannot adequately represent Tajweed rules for error detection. For example, MSA cannot measure the precise length of Madd rules. Previous research (e.g., [omran2023automatic]) focused on single rules like Qalqalah. Our phonetic script addresses this limitation by capturing all Tajweed pronunciation errors except Ishmam (إشمام), which involves a visual mouth movement without audible output.

## Background  

We based our script on classical Muslim scholarship rather than the International Phonetic Alphabet (IPA) for these reasons:

1. **Historical Precedence**: Muslim scholars from the 6th to 14th centuries rigorously defined Quranic errors centuries before modern phonetics emerged in the West.
2. **Scientific Foundation**: Scholars like Al-Khalil ibn Ahmad (6th century AH) systematically described articulations and attributes with remarkable accuracy comparable to modern phonetics [article-khalil].
3. **Pedagogical Relevance**: Learners' errors align with classical definitions according to expert Quran teachers.

### Defining Mistakes in Quran Recitation  

Following [sweed2021], Quran recitation errors fall into three categories:  
1. **Articulation Errors**: Incorrect pronunciation of phonemes  
2. **Attribute Errors**: Mistakes in letter characteristics (Sifat al-Huruf)  
3. **Tajweed Rule Errors**: Incorrect application of rules like Ghunnah, Madd, etc.  

Our script comprehensively addresses all three aspects through two output levels:  
* **Phonemes Level**: Represents letters, vowels, and Tajweed rules  
* **Sifat Level**: Represents articulation attributes for each phoneme  

### Phoneme Set (43 Symbols)  

| Phoneme Name          | Symbol | Description                          |
|-----------------------|--------|--------------------------------------|
| hamza                | ء      | Glottal stop                         |
| baa                  | ب      | /b/                                  |
| taa                  | ت      | /t/                                  |
| thaa                 | ث      | /θ/                                  |
| jeem                 | ج      | /d͡ʒ/                                 |
| haa_mohmala          | ح      | Voiceless pharyngeal fricative       |
| khaa                 | خ      | /x/                                  |
| daal                 | د      | /d/                                  |
| thaal                | ذ      | /ð/                                  |
| raa                  | ر      | /r/                                  |
| zay                  | ز      | /z/                                  |
| seen                 | س      | /s/                                  |
| sheen                | ش      | /ʃ/                                  |
| saad                 | ص      | Emphatic /s/                         |
| daad                 | ض      | Pharyngealized /d/                   |
| taa_mofakhama        | ط      | Emphatic /t/                         |
| zaa_mofakhama        | ظ      | Emphatic /ð/                         |
| ayn                  | ع      | /ʕ/                                  |
| ghyn                 | غ      | /ɣ/                                  |
| faa                  | ف      | /f/                                  |
| qaf                  | ق      | /q/                                  |
| kaf                  | ك      | /k/                                  |
| lam                  | ل      | /l/                                  |
| meem                 | م      | /m/                                  |
| noon                 | ن      | /n/                                  |
| haa                  | ه      | /h/                                  |
| waw                  | و      | /w/                                  |
| yaa                  | ي      | /j/                                  |
| alif                 | ا      | /aː/                                 |
| yaa_madd             | ۦ       | Madd extension symbol for /j/        |
| waw_madd             | ۥ       | Madd extension symbol for /w/        |
| fatha                | َ       | /a/                                  |
| dama                 | ُ       | /u/                                  |
| kasra                | ِ       | /i/                                  |
| fatha_momala         | ۪       | Imala-modified /a/                   |
| alif_momala          | ـ       | Imala-modified alif                  |
| hamza_mosahala       | ٲ       | Hamzat al-wasl with tasheel          |
| qlqla                | ڇ       | Qalqalah marker                      |
| noon_mokhfah         | ں       | Ikhfa marker for noon                |
| meem_mokhfah         | ۾       | Ikhfa marker for meem                |
| sakt                 | ۜ       | Slight pause marker                  |
| dama_mokhtalasa      | ؙ       | Rawm marker                          |

### Sifat Set (10 Attributes)  

| Sifat (English)        | Sifat (Arabic)       | Available Attributes (English)          | Available Attributes (Arabic)       |
|------------------------|----------------------|----------------------------------------|-------------------------------------|
| hams_or_jahr         | الهمس أو الجهر     | hams, jahr                           | همس, جهر                          |
| shidda_or_rakhawa    | الشدة أو الرخاوة  | shadeed, between, rikhw              | شديد, بين بين, رخو                     |
| tafkheem_or_taqeeq   | التفخيم أو الترقيق | mofakham, moraqaq                    | مفخم, مرقق                         |
| itbaq                | الإطباق            | monfateh, motbaq                     | منفتح, مطبق                        |
| safeer               | الصفير             | safeer, no_safeer                    | صفير, لا صفير                      |
| qalqla               | القلقلة            | moqalqal, not_moqalqal               | مقلقل, غير مقلقل                   |
| tikraar              | التكرار            | mokarar, not_mokarar                 | مكرر, غير مكرر                     |
| tafashie             | التفشي             | motafashie, not_motafashie           | متفشي, غير متفشي                   |
| istitala             | الاستطالة          | mostateel, not_mostateel             | مستطيل, غير مستطيل                 |
| ghonna               | الغنة              | maghnoon, not_maghnoon               | مغنون, غير مغنون                   |

### Key Design Principles  

1. **Madd Representation**:  
   - Normal Madd appears as consecutive madd symbols (e.g., 4-beat Madd: اااا)  
   - Madd al-Leen represented with multiple waw/yaa symbols  

2. **Emphatic Articulation**:  
   - Stressed Ghunnah (e.g., النون المشددة) as three consecutive noon symbols (ننن)  
   - Ikhfa represented as three consecutive noon_mokhfah (ںںں) or meem_mokhfah (۾۾۾)  

3. **Idgham Handling**:  
   - Assimilation represented by doubling (e.g., مَن يَعْمَلْ → مَنيييَعمَل)  

4. **Special Cases**:  
   - Sakin: No following symbol  
   - Imala: fatha_momala and alif_momala  
   - Rawm: dama_mokhtalasa marker  

### Examples  
| Uthmani Script | Phonetic Script      |
|----------------|----------------------|
| أَ             | ءَ                   |
| تُ             | تُ                   |
| حَـٰٓ          | حَاااااا             |
| جُّ            | ججُ                  |
| وٓ             | ۥۥۥۥۥۥ               |
| نِّ            | ننننِ                |
| ى              | ۦۦ                   |


| Phoneme       | Hams/Jahr | Shidda/Rakhawa | Tafkheem/Taqeeq | Itbaq      | Safeer      | Qalqla          | Tikraar        | Tafashie        | Istitala        | Ghonna        |
|---------------|-----------|----------------|-----------------|------------|-------------|-----------------|----------------|-----------------|-----------------|---------------|
| ءَ            | jahr      | shadeed        | moraqaq         | monfateh   | no_safeer   | not_moqalqal    | not_mokarar    | not_motafashie  | not_mostateel   | not_maghnoon  |
| تُ            | hams      | shadeed        | moraqaq         | monfateh   | no_safeer   | not_moqalqal    | not_mokarar    | not_motafashie  | not_mostateel   | not_maghnoon  |
| حَ            | hams      | rikhw          | moraqaq         | monfateh   | no_safeer   | not_moqalqal    | not_mokarar    | not_motafashie  | not_mostateel   | not_maghnoon  |
| اااااا        | jahr      | rikhw          | moraqaq         | monfateh   | no_safeer   | not_moqalqal    | not_mokarar    | not_motafashie  | not_mostateel   | not_maghnoon  |
| ججُ           | jahr      | shadeed        | moraqaq         | monfateh   | no_safeer   | not_moqalqal    | not_mokarar    | not_motafashie  | not_mostateel   | not_maghnoon  |
| ۥۥۥۥۥۥ         | jahr      | rikhw          | moraqaq         | monfateh   | no_safeer   | not_moqalqal    | not_mokarar    | not_motafashie  | not_mostateel   | not_maghnoon  |
| ننننِ         | jahr      | between        | moraqaq         | monfateh   | no_safeer   | not_moqalqal    | not_mokarar    | not_motafashie  | not_mostateel   | maghnoon      |
| ۦۦ            | jahr      | rikhw          | moraqaq         | monfateh   | no_safeer   | not_moqalqal    | not_mokarar    | not_motafashie  | not_mostateel   | not_maghnoon  |

## Development Methodology  

### Two-Stage Conversion Pipeline  

1. **Imlaey to Uthmani Conversion**  
   We selected Uthmani script as our foundation because:  
   - Contains specialized Tajweed diacritics (Madd, Tasheel, etc.)  
   - Preserves pause rules critical for recitation (e.g., stopping on رحمت)  

In order to do that, we created an annotation UI to manually annotate misaligned words in both scripts. For example,

| Imlaey Script | Uthmani Script |
| -- | -- |
| يَا ابْنَ أُمَّ| يَبْنَؤُمَّ|

after that, we developed an algorithm that relies on the annotations to convert Imlaey to Uthmani. 

2. **Uthmani to Phonetic Script Conversion**  

Implemented through 26 sequential operations:  


| Operation Name           | Arabic Name              | Corrected Description                                                                 |
|--------------------------|--------------------------|----------------------------------------------------------------------------------------|
| DisassembleHrofMoqatta | تفكيك حروف مقطعة      | Separates Quranic initials (e.g., الم، الر) into individual letters.                   |
| SpecialCases           | حالات خاصة             | Handles special words like (يبسط) that have different pronunciation forms defined in `MoshafAttributes` |
| BeginWithHamzatWasl    | البدء بهمزة الوصل     | Processes words starting with connecting hamza (ٱ) and converts it to hamza (ء) with appropriate harakah for nouns and verbs |
| BeginWithSaken         | البدء بساكن            | Manages words beginning with a consonant (sakin) like (لْيَقْطَعْ), as Arabic doesn't start utterances with consonants |
| ConvertAlifMaksora     | تحويل الألف المقصورة  | Converts (ى) in Uthmani script to either yaa (ي) or alif (ا) based on context          |
| NormalizeHmazat        | توحيد الهمزات         | Standardizes hamza forms (أ إ ؤ ئ) to (ء)                                             |
| IthbatYaaYohie         | إثبات ياء يحيى        | Handles words like (يُحْىِۦ) where two yaa letters occur - resolves conflicts when pausing on words with consecutive consonants (التقاء الساكنين) by adding another yaa at end. |
| RemoveKasheeda         | إزالة الكشيدة         | Deletes elongation marks (ـــ) from text                                              |
| RemoveHmzatWaslMiddle  | إزالة همزة الوصل الوسطية | Removes connecting hamza (ٱ) in non-initial positions                                  |
| RemoveSkoonMostadeer   | حذف الحرف الذي فوقع سكون مستدير | Eliminates letters with circular sukoon diacritics like alif in (جَمَعُوا۟)          |
| SkoonMostateel         | سكون مستطيل            | Removes alif with elongated sukoon mid-word and adds it at the end during pauses (وقف) |
| MaddAlewad             | مد العوض               | Removes alif after tanween fatha mid-word and adds alif while removing tanween at pause positions (وقف) |
| WawAlsalah             | واو الصلاة            | Replaces letter waw (و) with small alif above combined with alif                       |
| EnlargeSmallLetters    | تكبير الحروف الصغيرة  | Resizes miniature Arabic letters to standard proportions                              |
| CleanEnd               | تنظيف النهاية         | Removes redundant diacritics and spaces at word endings                               |
| NormalizeTaa           | توحيد التاء            | Converts ة (taa marbuta) to ت or ه based on context, and converts final ة to haa (ه) |
| AddAlifIsmAllah        | إضافة ألف اسم الله    | Inserts compensatory alif in derivatives of "الله"                                    |
| PrepareGhonnaIdghamIqlab | تهيئة الغنة والإدغام والإقلاب | Preprocesses text for nasalization, assimilation, and conversion rules             |
| IltiqaaAlsaknan        | التقاء الساكنين       | Resolves consecutive consonants by inserting vowels                                 |
| DeleteShaddaAtBeginning| حذف الشدة في البداية  | Removes shadda (ّ) from word-initial letters                                        |
| Ghonna                 | غنة                   | Applies nasalization during pronunciation of sakin noon and tanween                  |
| Tasheel                | تسهيل                 | Adds a letter representing alif with tasheel easing                                  |
| Imala                  | إمالة                 | Converts fatha with imala to `fatha_momala` phoneme and alif with imala to `alif_momala` phoneme |
| Madd                   | مد                    | Adds madd symbols for all madd types, inserting `madd_alif` (ا), `madd_waw` (ۥ), and `madd_yaa` (ۦ) |
| Qalqla                 | قلقة                  | Adds echoing effect to ق, ط, ب, ج, د letters with sukoon                           |
| RemoveRasHaaAndShadda  | إزالة رأس الحاء علامة السكون | Deletes sukoon diacritic marks                                                   |
### Sifat Assignment Principles  

We selected these 10 attributes as they comprehensively describe articulation:

- **Hams/Jahr** (الهمس/الجهر)  
  - *Hams*: Whispered letters requiring breath flow ( ف ح ث ه ش خ ص س ك ت)  
  - *Jahr*: Voiced letters with full the rest of letters

- **Shidda/Rakhawa** (الشدة/الرخاوة)  
  - *Shidda*: Complete interruption of sound ( ء ج د ق ط ب ك ت)  
  - *Between Shiddah and Rqkahwa*: in between of both ( ل ن ع م ر)  
  - *Rakhawa*: Continuous airflow the rest of letter.

- **Tafkheem/Taqeeq** (التفخيم/الترقيق)  
  - *Tafkheem*: Heavy/thickened pronunciation ( خ ص ض ط ظ غ ق)  
  - *Taqeeq*: Light/thin pronunciation rest of letter with exepsion descripted below

- **Itbaq** (الإطباق)  
  - *Motbaq* Letters pronounced with tongue-to-palate contact ( ص ض ط ظ)
  - *Monfateh* Rest of the letters

- **Safeer** (الصفير)  
  - *Safeer* Whistling sound in س ص ز
  - *No Safeer* the rest of the letters

- **Qalqala** (القلقلة)  
  - *Moqlqal* Echo effect on ق ط ب ج د when bearing sukoon
  - *Not Moqlqal* the rest of letters

- **Tikraar** (التكرار)  
  - *Mokarrar* the Quranic letter (ر) is trilled just (like Spanish perro)
  - *Not Mokarrar* the rest of letters

- **Tafashie** (التفشي)  
  - *Motafashie* Sound dispersion characteristic of ش
  - *Not Motafashie* Rest of letters

- **Istitala** (الاستطالة)  
  - *Mostateel* sepecial attribute emphatic and pharyngealized for letter (ض)
  - *Not Mostateel* Rest of letters

- **Ghonna** (الغنة)  
  - *Maghnoon* Nasalization in ن and م
  - *Not Maghnoon* The other letters


While excluding:  
- **Inheraf** (إنحراف): Explained through our shidda/rakhawa spectrum  
- **Leen** (اللين): Handled through our Madd representation  

According to [sweed2021], articulation attributes are either permanent or contextual:  

1. **Permanent Attributes**: Fixed for each letter (e.g., tafkheem for ق)  
2. **Contextual Attributes**:  
   - Raa (ر): Varies between mofakham/moraqaq  
   - Lam in Allah: moraqaq when preceded by kasrah  
   - Madd alif: Inherits tafkheem/taqeeq from preceding phoneme  
   - Ikhfa Ghunnah: Inherits tafkheem/taqeeq from following phoneme  

This systematic approach enables precise representation of all Tajweed rules for Hafs except Ishmam, providing a comprehensive foundation for pronunciation assessment.
