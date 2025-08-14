# Quran Phonetic Script

We think that the most valubale and import contribution of our work is the Quran Phonetic Script as the fromlization of the Assessing Prounciation for the Holy Quran as an ASR probelm represented by Quran Phonetic Script helps to slove the task.

## Motivation for Developing Quran Phonetic script

If you want to decet the length of the Madd rule in Holy Quran the Modern standard Arabic (MSA)[] can not measre this rule to detect erros. Some researcher for example [omran2023automatic] focuses on a specific rule (QalQla Rule). So we argue that we have created a phonetic script that can detect all Tajweed prounced erros exexpt for Ishmam (إشمام) as it is a sign by the mouth wich has no vocice.

## background

We relyed on the Acinet Muslim scholars to define Quran erros not The (International Photonic Association) IPA for the following reasons:

* Muslim schoars starting from 6th century to 14th century have regrously defined all types of erros that may encounter Holy Quran Learner far before raising of modern photenics at the west in the 17th century

* Muslim schoarls have the favour of defining photonics far before IPA in a very scientific and organized manar for example Scholar Al-Khalil in the 6th centurey centuries before modern phtonics has nearly achieved same results defining arctulations and its attributes accorading to [article-khalil] 
* In practises learners mistakes while recition the Holy Quarn does not go away to theri difinitions according to expert teachers.


### Defining Mistakes in the Holy Quran

According to [sweed2021] Mistakes while reciting the Holy Quran are the following:

* Mistakes in the articulations of the phonemes
* Mistakes in the attributes for the articulations (Sifat)(صفات الحروف)
* Tajweed rules include Ghonna and Madd, ..etc.

So for our script to be complete we have to include the 3 ascpects. But articulations can be represented by the phoneme itself and we can represent tajweed rules as phonemes also as we will show so our script outputs two things:

* **Phonemes Level**: that represnets letters, tajweed rules and short and long vowels (الحركات ولامدود)
* **Sifa Level**: that represents the attribute for articulation of every phonemes defined in the phoneme set


| Phoneme Name           | Symbol |
|------------------------|--------|
| hamza                 | ء     | 
| baa                   | ب     |
| taa                   | ت     |
| thaa                  | ث     |
| jeem                  | ج     |
| haa_mohmala           | ح     |
| khaa                  | خ     |
| daal                  | د     |
| thaal                 | ذ     |
| raa                   | ر     |
| zay                   | ز     | 
| seen                  | س     |
| sheen                 | ش     |
| saad                  | ص     |
| daad                  | ض     |
| taa_mofakhama         | ط     |
| zaa_mofakhama         | ظ     |
| ayn                   | ع     |
| ghyn                  | غ     |
| faa                   | ف     |
| qaf                   | ق     |
| kaf                   | ك     |
| lam                   | ل     |
| meem                  | م     |
| noon                  | ن     |
| haa                   | ه     |
| waw                   | و     |
| yaa                   | ي     |
| alif                  | ا     |
| yaa_madd              | ۦ     |
| waw_madd              | ۥ     |
| fatha                 | َ     |
| dama                  | ُ     |
| kasra                 | ِ     |
| fatha_momala          | ۪     |
| alif_momala           | ـ     |
| hamza_mosahala        | ٲ     |
| qlqla                 | ڇ     |
| noon_mokhfah          | ں     |
| meem_mokhfah          | ۾     |
| sakt                  | ۜ     |
| dama_mokhtalasa       | ؙ     |


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


Important Notes About phoneme Level:
* we represent normal madd as two conscative `madd_alif` for golden recitation same as `madd_waw` and `madd_yaa`
* for madd aleen (مد اللين) we represent it with yaa and waw yaa and waw but with multiple of them according to the madd length
* We represents stressed Gonna for noon (النون لمشددة) as tree consecative `noon` same as stressed meem but with three `meem`s
* We represent golded Ikhfaa for noon and tanween as three conscative `noon_mokhfah`
* We reprsetn rule of Idgham for noon or tanween with yaa (ي) or waw (و) as two of both example ( مَن يَعْمَلْ) can be representd as (مَنيييَعمَل)
* We represent golded Ikhfaa for meem  as three conscative `meem_mokhfaah` or 3 `meem` according to moshaf attributes `meem_mokhfah`
* We represet saken with nothing after it
* We represent sakt (sligh pause) as `skat` sign
* We represent alif moshaha as `alif_moshala` 
* We represent fatha momala in word (مجراها) as `fatha_momala`
* We represent alif momala in word (مجراها) as two  `alif_momala`
* We represent `rawm` for letter `noon` in word (تأمنا) by `dama_mokhtalasa`
* We add a letter for `qalqal` so model can diffrenital with letter that has haraka (`fatha`, `damm`, `kasra` and with saken letter)


As we see we have modeled all tajweed rules for `Hafs` exept for `rawm` (الوقف بالروم) and Ishmam (إشمام) as it is is voices like normal phonemes but donated by a sign of damma form the mouth


### Examples:

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



### Steps From Development

the steps of development consits of mainly two steps: converting Imlaey script to Uthmani script and the second script is to convert the Uthmani script to the phonetic script

#### Convert Imlaey Script to Uthmani Script

We relied on the Uthmani script for prducing the phonetics scripts for the following reasons: 
* Muslim Scholars has put special signs to dontate most of Tajweed rules like Madd, Tasheel, ..etc
* The recitations rules on puase are built upon the Uthmani script not the Imlaey Script like stoping on word (رحمت)

In order to do that we created an annotation UI to manually annotate miss aligned words in both scripts for example

| Imlaey Script | Uthmani Script |
| -- | -- |
| يَا ابْنَ أُمَّ| يَبْنَؤُمَّ|

After that we created an algorithm to that rely on the annotation to convert Imlaey to Uthmani


#### Convert Uthmnia script to Phonetic Script

As we said before we have two levels `phonemes` level and `sifat` level

##### Phoneme level

We created and Algorithm composed of 26 sequentional operations. Every operation is composed of a single or mulitple reqular expreesion. Given the MoshafAttribute and the uthmani script we can produce the phonetic script


Here's the markdown table with operations, their Arabic names, and descriptions:

| Operation Name                 | Arabic Name                   | Description                                                                 |
|--------------------------------|-------------------------------|-----------------------------------------------------------------------------|
| DisassembleHrofMoqatta       | تفكيك حروف مقطعة            | Separates Quranic initials (e.g., الم، الر) into individual letters.        |
| SpecialCases()                 | حالات خاصة                   | Hafs has special words like (يبسط) that has diffrent prounciation forms for every moshaf defined in `MoshafAttributes`                |
| BeginWithHamzatWasl()          | البدء بهمزة الوصل           | Processes words starting with connecting hamza (ٱ) and convert it hamza (ء) with its appropriate haraka for nouns and verbs.                         |
| BeginWithSaken()               | البدء بساكن                  | Manages words beginning with a consonant (saken) from like (لْيَقْطَعْ) as Arabs does not start a talking with consonent.                 |
| ConvertAlifMaksora()           | تحويل الألف المقصورة        | (ى) in Uthmani script can represent yaa (ي) or alif (ا) .                          |
| NormalizeHmazat()              | توحيد الهمزات               | Standardizes hamza forms (أ إ ؤ ئ) to (ء).           |
| IthbatYaaYohie()               | إثبات ياء يحيى              | word (يُحْىِۦ) has two yaa (ي) letters at end first is (ي)  and the other is written at small yaa (ۦ) some of these work are writting with a sinlge yaa due to meeting two consenet (التقاء الساكنان) so we add it in cause of pusing on it                           |
| RemoveKasheeda()               | إزالة الكشيدة               | Deletes elongation marks (ـــ) from text.                                   |
| RemoveHmzatWaslMiddle()        | إزالة همزة الوصل الوسطية    | Removes connecting hamza (ٱ) in non-initial positions.                       |
| RemoveSkoonMostadeer()         | حذف الحرف الذي فوقع سكون مستدير       | Eliminates  letter that has skoon mokstadeel like letter alif in word (جَمَعُوا۟).                          |
| SkoonMostateel()               | سكون مستطيل                  | remove alif with skoon mostateel in-between and add it at the end (وقف).                               |
| MaddAlewad()                   | مد العوض                     | remove alif after tanween with fath and in-between and add alif while removing tnawwen at end (وقف)           |
| WawAlsalah()                   | واو الصلاة                  | Replace letter waw (و) with small alif above eith alif                           |
| EnlargeSmallLetters()          | تكبير الحروف الصغيرة        | Resizes miniature Arabic letters to standard proportions.                   |
| CleanEnd()                     | تنظيف النهاية               | Removes redundant diacritics/spaces at word endings.                        |
| NormalizeTaa()                 | توحيد التاء                  | Converts ة (taa marbuta) to ت or ه based on context and (ة) at end to haa (ه).                         |
| AddAlifIsmAllah()              | إضافة ألف اسم الله          | Inserts compensatory ا in "الله" derivatives.                               |
| PrepareGhonnaIdghamIqlab()     | تهيئة الغنة والإدغام والإقلاب | Preprocesses text for nasalization, merging, and conversion rules.          |
| IltiqaaAlsaknan()              | التقاء الساكنين             | Resolves consecutive consonants by inserting vowels.                        |
| DeleteShaddaAtBeginning()      | حذف الشدة في البداية        | Removes shadda (ّ) from word-initial letters.                               |
| Ghonna()                       | غنة                         | Applies nasalization during noon ساكنة/تنوين pronunciation.                 |
| Tasheel()                      | تسهيل                       | Add a letter representing alif with tasheel (تسهيل).                                 |
| Imala()                        | إمالة                       | convert fatha with imalal to `fahta_momala` phoneme and alif with imalal to `alif_momoal` phoneme.              |
| Madd()                         | مد                          | Adding madd sings for all madd tyes ans inserting madd letter `madd_alif` (ا) `madd_waw` (ۥ) and `madd_yaa` (ۦ).                              |
| Qalqla()                       | قلقة                        | Adds echoing effect to ق ط ب ج د letters with sukoon.                       |
| RemoveRasHaaAndShadda()        | إزالة رأس الحاء علامة السكون      | Delete skoon sign.              |



#### Sifat Level
The work of sifat is a bit more simpler than phonemes. 
we have chosed these attributes to describe letters:

Here's the list converted to a dotted format with Arabic names and descriptions:

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


We did not include: 
* **Inheraf** (إنحراف) as it explains why letter (ر) and (ل) are between `shidda` and `rakhawa`
* **Leen** (اللين) as it explains why (و) or (ي) are elonged if they prefixed wth fatha and we formulate this during madd

Accourding to [sweed2021] attrubtes for articulation (صفات الحرقو) for quranic letters has two forms presetance attrbutes and variable attributes

All attributations of articulations (صفات الحروف) are devided into defined group of letter prsestanlty for all occupation of letters exepct for:

* Letter raaa (raa): in some casses can be mofakham (مفخم) or morqaqa (مرقق)
* Lam of word Allah (الله) can be  morqaqa (مرقق) if preceeded by kasra and  mofakham (مفخم)other wise
* Madd alif (ا) folllows the precceded phoneme in mofakham (تفخيم) or morqaqa (ترقيق)
* Ghonna for Ikhfaa folllowd the  phoneme after it in mofakham (تفخيم) or morqaqa (ترقيق)
