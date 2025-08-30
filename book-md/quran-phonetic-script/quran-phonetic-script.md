## Quran Phonetic Script

The Quran Phonetic Script is a set of letters and attributes (صفات) that describes what the Holy Quran's reciters **actually** said. It was designed to capture all recitation rules, including all Tajweed rules (except Ishmam `إشمام` and pausing with rawm `روم` or `إشمام`) and Sifat. This script is composed of 11 levels:

*   `phonemes` level: Designed to capture pronunciation of letters like baa (ب) and diaractization like (fatha, damma and kasra).
*   `sifat` level: Consisting of 10 levels to capture the attribute of articulation (صفة) for every phoneme group.

We built this script based on `Hafs` (رواية حفص) and incorporated all the different ways of reciting for `Hafs`. For example, the length of Madd Almunfasil can be (2, 3, 4, or 5 beats). Other variations can be found here [section_hafs_ways].

### Phonemes Level

The phoneme level has specific features, which are summarized as:

1.  **Madd Representation**:
    *   Normal Madd appears as consecutive madd symbols (e.g., 4-beat Madd: اااا).
    *   Madd al-Leen is represented with multiple waw/yaa symbols.

2.  **Ghunnah**:
    *   Stressed Ghunnah for noon (e.g., النون المشددة) is represented as three consecutive noon symbols (ننن).
    *   Ikhfa is represented as three consecutive noon_mokhfah (ںںں) or meem_mokhfah (۾۾۾).

3.  **Idgham Handling**:
    *   Idgham for sakin noon with yaa is represented by consonant doubling (e.g., مَن يَعْمَلْ → مَنيييَعمَل).

4.  **Special Cases**:
    *   Sakin: No following vowel symbol.
    *   Imala: Represented by fatha_momala and alif_momala.
    *   Rawm: Represented by the dama_mokhtalasa marker.


| Uthmani | Phonetic | H/J | S/R | T/T | Itb | Saf | Qal | Tik | Taf | Ist | Gho |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| أَ | ءَ | jahr | shd | mrq | mnf | no | nql | nkr | ntf | nst | nmg |
| تُ | تُ | hams | shd | mrq | mnf | no | nql | nkr | ntf | nst | nmg |
| حَـ | حَ | hams | rkh | mrq | mnf | no | nql | nkr | ntf | nst | nmg |
| ـٰٓ | اااااا | hams | rkh | mrq | mnf | no | nql | nkr | ntf | nst | nmg |
| جُّ | ججُ | jahr | shd | mrq | mnf | no | nql | nkr | ntf | nst | nmg |
| وٓ | ۥۥۥۥۥۥ | jahr | rkh | mrq | mnf | no | nql | nkr | ntf | nst | nmg |
| نِّ | ننننِ | jahr | btw | mrq | mnf | no | nql | nkr | ntf | nst | mg |
| ى | ۦۦ | jahr | rkh | mrq | mnf | no | nql | nkr | ntf | nst | nmg |

Examples of Uthmani to Phonetic Script Conversion with Sifat Attributes: Phonetization of word (أَتُحَٰٓجُّوٓنِّى)
**Attribute Abbreviations:**
- H/J: Hams/Jahr
- S/R: Shidda/Rakhawa
- T/T: Tafkheem/Taqeeq
- Itb: Itbaq
- Saf: Safeer
- Qal: Qalqla
- Tik: Tikraar
- Taf: Tafashie
- Ist: Istitala
- Gho: Ghonna
**Value Abbreviations:**
- shd: shadeed
- rkh: rikhw
- btw: between
- mrq: moraqaq
- mof: mofakham
- mnf: monfateh
- mtb: motbaq
- no: no_safeer
- nql: not_moqalqal
- nkr: not_mokarar
- ntf: not_motafashie
- nst: not_mostateel
- nmg: not_maghnoon
- mg: maghnoon

#### Detailed Phoneme Construction

We only care about pronounced phonemes of letters. If a letter is dropped or not pronounced, we will omit it. For example, we drop the Wasl Hamza (همزة الوصل) when it appears in a context like: (بِسْمِ اللَّهِ).

##### Disconnected Letters

Disconnected letters (الحروف المقطعة) are letters that are pronounced as individual alphabets one by one. For example: (الٓمٓ) is pronounced (أَلِفْ لَآم مِّيٓمْ). There are 14 forms of these disconnected letters, so we must separate them according to their actual pronunciation.

##### Madd (المد)

There are three types of elongation (مد):
*   **Madd Alif** (مد ألف): Fatha followed by alif (ا)
*   **Madd Waw** (مد بالواو): Damma followed by waw (و)
*   **Madd Yaa** (مد ياء): Kasra followed by Yaa (ي)

These Madd types have different lengths relative to the natural Madd (المد الطبيعي). We created special symbols to denote each Madd type:

*   **Madd Alif** is denoted by multiple alif symbols (ا)
*   **Madd Waw** is denoted by multiple small_waw symbols, designated as `waw_madd` (ۥ)
*   **Madd Yaa** is denoted by multiple small_yaa symbols, designated as `yaa_madd` (ۦ)


###### Normal Madd (المد الطبيعي)

Normal Madd is the type of elongation pronounced at its standard length without excessive prolongation. We denote it by doubling the respective `madd` phonemes. The example below [table_ex_normal_madd] shows all three types of Madd in a single word.

| Uthmani Script | Phonetic Script |
|----------------|-----------------|
| نُوحِيهَا       | نُۥۥحِۦۦهَاا     |

[table_ex_normal_madd]
The table demonstrates the three types of normal Madd: Madd Alif (اا), Madd Yaa (ۦۦ), and Madd Waw (ۥۥ), each represented with two symbols to indicate a two-beat elongation.


##### Madd Small Silah (مد الصلة الصغرى)

Along with Normal Madd, Small Silah Madd (مد الصلة الصغرى) follows the same representation rules. For example [table_ex_small_silah]:

| Uthmani Script              | Phonetic Script                 |
|-----------------------------|---------------------------------|
| إِنَّهُۥ عَلَىٰ رَجْعِهِۦ لَقَادِرٌ | ءِننننَهُۥۥ عَلَاا رَجڇعِهِۦۦ لَقَاادِر |

[table_ex_small_silah]
The table shows Small Silah Madd along with noon mushaddad denoted as 3 repeated `noon` (ن) with a special qalqala sign: (ڇ) for letter jeem (ج).


##### Madd Al-'Iwad (مد العوض)

In addition, Madd Al-'Iwad (مد العوض) is represented as shown in [table_ex_alewad]:

| Uthmani Script | Phonetic Script |
|----------------|-----------------|
| قَرِيبًا       | قَرِۦۦبَاا       |

[table_ex_alewad]
The table shows Madd Al-'Iwad (مد العوض) using the same notation as normal Madd (المد الطبيعي) for Madd alif. This type of Madd occurs when a tanween fatha on a final letter is replaced by an alif madd during pause.


##### Madd Al-Munfasil (مد المنفصل)

For Hafs recitation, Madd Al-Munfasil can be elongated for 2, 3, 4, or 5 harakat, where a haraka here is represented as half of a normal Madd when followed by a hamza (ء) not in the same word, as shown in the example [table_ex_monfasel]:

| Uthmani Script | Phonetic Script |
|----------------|-----------------|
| يَٰٓأَيُّهَا    | يَااااءَييُهَاا  |

[table_ex_monfasel]
The example shows elongation for Madd Al-Munfasil with 4 alif madd phonemes, along with a repeated yaa representing yaa mushaddada (ياء مشددة) with both a sakin yaa and a yaa with haraka (damma).


##### Madd As-Silah Al-Kubra (مد الصلة الكبرى)

The same rule is applied to Madd As-Silah Al-Kubra (مد الصلة الكبرى). As shown in the example below: [table_ex_big_silah]

| Uthmani Script | Phonetic Script |
|----------------|-----------------|
| مَالَهُۥٓ أَخْلَدَهُۥ | مَاالَهُۥۥۥۥ ءَخلَدَه |

[table_ex_big_silah]
The example shows elongation for Madd As-Silah Al-Kubra with 4 madd waw phonemes (ۥۥۥۥ).

##### Madd Al-Muttasil (المد المتصل)

For Hafs recitation, Madd Al-Muttasil (مد المتصل) can be elongated for 2, 3, 4, 5, or (6 at pause only) harakat, where a haraka is represented as half of a normal Madd when followed by a hamza (ء) in the same word, as shown in [table_ex_mottasel]:

| Uthmani Script | Phonetic Script    |
|----------------|--------------------|
| ٱلسَّمَآءِ مَآءً | ءَسسَمَااااءِ مَااااءَاا |

[table_ex_mottasel]
The example shows elongation for Madd Al-Muttasil (مد المتصل) with 4 madd alif phonemes, along with Madd Al-'Iwad (مد العوض) at the pause point.


##### Madd Al-Lazim (المد اللازم)

Madd Al-Lazim (المد اللازم) is the type of Madd where a Madd letter is followed by a Sakin letter (حرف ساكن) in the same word and is elongated for 6 harakat (6 حركات), where a haraka is represented as half of a normal Madd.

| Uthmani Script | Phonetic Script       |
|----------------|-----------------------|
| ٱلضَّآلِّينَ  | ءَضضَااااااللِۦۦۦۦنَ |

[table_ex_lazem]
The table shows an example of Madd Al-Lazim (المد اللازم) with Madd alif elongated for 6 harakat, along with Madd Al-'Arid Li-S-Sukun (مد العرض للسكون) represented with 4 harakat.



##### Madd Al-'Arid Li-S-Sukun (مد العارض للسكون)

Madd Al-'Arid Li-S-Sukun is the madd that occurs when pausing after a normal madd with a sakin letter. This madd is elongated for 2, 4, or 6 harakat, where the haraka is represented as half of the normal madd length, as shown in [table_ex_lazem]:


##### Madd Al-Leen (مد اللين)

Madd Al-Leen (مد اللين) occurs when pausing after a yaa (ي) or waw (و) that is preceded by a fatha and followed by a sakin letter. This madd is elongated for 2, 4, or 6 harakat, where a haraka is represented as half of the normal madd length [table_ex_leen]. We do not create special phonemes for this rule as we did with other madd types because Leen represents an elongation of existing waw (و) or yaa (ي) phonemes rather than introducing new phonemes.

For a 4-haraka madd, we denote this with (number_of_harakat - 1) symbols. This approach accounts for cases of Madd Al-Leen in the middle of recitation (like وَٱلْمَيْسِرِ) as well as at pause positions, maintaining consistency in the phonetic script. Table [table_ex_leen] shows an example of Madd Al-Leen:

| Uthmani Script | Phonetic Script |
|----------------|-----------------|
| لِإِيلَٰفِ قُرَيْشٍ | لِءِۦۦلَاافِ قُرَيييش |

[table_ex_leen]
The example shows two forms of madd: the first is normal madd followed by Madd Al-Leen with 4 harakat (each haraka being half of normal madd), denoted with 3 yaa (ي) symbols.



#### Ghunnah

We consider tanween here as a haraka (fatha, damma, or kasra) followed by a sakin noon (نون ساكنة), so we do not need to define separate rules for noon (ن) and tanween.

##### Noon Mushaddadah (النون المشددة)

We first attempted to measure the relative timing of a sakin noon alone (النون الساكنة المظهرة) and compare it to an elongated noon (noon with shaddah - نون مشددة). We found that the elongated noon is approximately 3 to 4 times longer than the sakin noon, so we defined the elongated noon as equivalent to 3 sakin noon repetitions. Example in table: [table_ex_noon_moshadada]

| Uthmani Script | Phonetic Script |
|----------------|-----------------|
| إِنَّ           | ءِننن           |
| شَىْءٍ نُّكُرٍ  | شَيءِننننُكُر   |
[table_ex_noon_moshadada]
The table shows how Ghunnah disassembly of noon with shaddah (نون مشددة) is represented as 3 repetitive noon (ن) symbols.


##### Meem Mushaddadah (الميم المشددة)

As we have done with Noon Mushaddadah, we applied the same principle to Meem Mushaddadah (elongated meem). We found the same result: Meem Mushaddadah is approximately 3 to 4 times longer than a regular sakin meem (ميم ساكنة مظهرة). We denote Meem Mushaddadah as 3 repeated meem symbols, as shown in the examples: [table_ex_meem_moshadda]


| Uthmani Script | Phonetic Script |
| -- | -- |
|  أَمَّا | ءَممممَاا |
|  خَيْرٍ مِّن |  خَيرِممممِن |
[table_ex_meem_moshadda]
The table shows how Ghunnah disassembly of meem with shaddah (ميم مشددة) is represented as 3 repeated meem (م) symbols.

##### Ikhfaa for Noon (إخفاء النون الساكنة)

Ikhfaa for sakin noon (إخفاء النون الساكنة) occurs when a sakin noon (نون ساكنة) or tanween is followed by any of the Ikhfaa letters: (ص، ذ، ث، ك، ج، ش، ق، س، د، ط، ز، ت، ض، ظ، ف). We denote this by replacing the noon with three `noon_mokhfaa` symbols (ں), as shown in the example [table_ex_noon_mokhfaa]:

| Uthmani Script | Phonetic Script |
|----------------|-----------------|
| مِن صَلْصَٰلٍ   | مِںںںصَلصَاااال  |

[table_ex_noon_mokhfaa]
The table shows the representation of noon mokhfaa (نون مخفاة) as three dotless noon symbols (ں).


##### Idgham for Noon with Yaa and Waw (إدغام النون الساكنة مع الياء والواو)

The Idgham rule is defined as pronouncing two consecutive letters as the second letter with shadda (stress) according to Ibn Al-Jazari [ibnaljazri_alnashr]. Therefore, we simply delete the noon (ن) and replace it with a yaa (ي) or waw (و).

As with Noon Mushaddadah and Meem Mushaddadah, we represent the resulting stressed yaa or waw with two repetitions rather than three. This maintains consistency with our representation of Madd Al-Leen and follows the convention that a stressed letter (مشدد) is represented by both a sakin and mutaharrik (متحرك) form. Table [table_ex_idghaam_yaa_with_noon] shows examples of different forms of yaa:

| Uthmani Script | Phonetic Script |
|----------------|-----------------|
| مَن يَعْمَلْ    | مَيييَعمَل       |
| ٱلْحَىِّ       | ءَلحَيي         |
| قُرَيْشٍ       | قُرَيييش        |

[table_ex_idghaam_yaa_with_noon]
This table demonstrates different representations of yaa. The first row shows Idgham of yaa with sakin noon (النون الساكنة) represented by replacing the noon with two yaa symbols. The second row shows yaa with shadda at pause represented with two yaa symbols. The third row shows Madd Al-Leen with 4 harakat represented by 3 yaa symbols.


##### Ikhfaa for Meem (إخفاء الميم الساكنة)

Ikhfaa for sakin meem (إخفاء الميم الساكنة) occurs when a sakin meem (ميم ساكنة) is followed by a baa (ب). Additionally, when a sakin noon or tanween is followed by baa, it is defined in Tajweed literature as Iqlab (إقلاب). We represent both cases with three `meem_mokhfah` symbols (۾). Table [table_ex_ikhfaa_meem] shows how this rule is applied:

| Uthmani Script | Phonetic Script |
|----------------|-----------------|
| مِنۢ بَعْدِ | مِ۾۾۾بَعدڇ |
| تَرْمِيهِم بِحِجَارَةٍ | تَرمِۦۦهِ۾۾۾بِحِجَاارَه |

[table_ex_ikhfaa_meem]
The first row represents the Iqlab rule (الإقلاب), which is denoted by replacing the noon with 3 `meem_mokhfah` symbols (۾). The second row shows the rule of Ikhfaa for sakin meem with baa (إخفاء الميم الساكنة), represented by 3 `meem_mokhfah` symbols (۾).

#### Idgham (الإدغام)

There are two types of merging (Idgham) in Arabic:

*   **Full Merging (إدغام كامل)**: When two letters follow each other and are pronounced as only the second letter, but stressed. Example: (قَد تَّبَيَّنَ) is pronounced as (قَتتَبَييَن) where the letter daal is completely not pronounced.
*   **Partial Merging (إدغام ناقص)**: When two letters follow each other and the articulation point (makhraj) of the first letter is lost but its attributes (sifat) remain. Example: (بَسَطْتَ) is pronounced the same (بَسَطَت).

#### Sakin Letter (الحرف الساكن)

A sakin letter is represented in the Uthmani script in three forms:

1.  A letter followed by sukun (سُكُون): 'ْ'
2.  A letter with shaddah (شَدَّة), which represents a stressed letter composed of two identical letters: the first is sakin and the second has a haraka (fatḥah, ḍammah, or kasrah). Example: (بَّ) → (بْبَ)
3.  A letter that is not followed by any haraka (short vowel) or any special symbol, which occurs in Idgham and with madd letters.

We denote a sakin letter by the absence of any following vowel diacritic.

#### Pausing (وَقْف)

At a pause (وَقْف), we make the final letter sakin (سَاكِن) by removing any vowel diacritic. See examples in: [table_ex_idghaam_yaa_with_noon] and other relevant tables.


#### Hamzat Al-Wasl (همزة الوصل)

Hamzat Al-Wasl (همزة الوصل) (ٱ) is defined in Tajweed as a hamza added to avoid beginning with a sakin letter [sweed2021]. It is elided during continuous recitation and is only pronounced at the beginning.

The vowel following Hamzat Al-Wasl (fatha, damma, or kasra) depends on the word type:

*   For nouns beginning with Alif-Lam at-ta'reef (ال التعريف), the hamza is followed by fatha.
*   For proper nouns, the hamza is followed by kasra.
*   For verbs: the vowel depends on the third root letter:
    *   Damma: hamza is followed by non-transient damma
    *   Fatha, kasra, or transient damma: hamza is followed by kasra

**Transient damma** refers to a damma that is not original but results from a temporary grammatical state. For example, the word (ٱمْشُوا۟) has a damma on its third letter, but the verb originates from (ٱمْشِ) where the third letter (ش) has kasra.

| Uthmani Script | Phonetic Script      | Word Type                          | Hamzat Wasl Vowel |
|----------------|----------------------|------------------------------------|-------------------|
| ٱلْكِتَٰبُ     | ءَلكِتَاااابڇ        | Noun beginning with (ال)           | fatha             |
| ٱللَّهِ       | ءَللَااااه           | Proper Noun beginning with (ال)    | fatha             |
| ٱسْتِكْبَارًۭا | ءِستِكبَاارَاا       | Proper Noun                        | kasra             |
| ٱرْكَب        | ءِركَبڇ              | Verb (3rd letter has fatha)        | kasra             |
| ٱصْبِرْ       | ءِصبِر               | Verb (3rd letter has kasra)        | kasra             |
| ٱمْشُوا۟      | ءِمشُۥۥ              | Verb (3rd letter has transient damma) | kasra          |
| ٱرْكُضْ       | ءُركُض               | Verb (3rd letter has non-transient damma) | damma       |

[table_ex_hamzat_wasl]
This table shows different forms of Hamzat Al-Wasl (ٱ). The first and second rows demonstrate beginning with hamza followed by fatha due to (ال) at-ta'reef. The third row shows beginning with hamza followed by kasra for a proper noun. The 4th, 5th, and 6th rows show verbs beginning with hamza followed by kasra because the third radical has fatha, kasra, or transient damma. The last row shows beginning with hamza followed by damma because the third radical has a non-transient damma.

**Important Note**: We rely on Dukes's work [dukes2010morphological] for determining word types (nouns, verbs, and particles). Without this foundational research, annotating the Holy Quran's words would require at least a year of dedicated effort, highlighting the critical importance of open-source linguistic resources.


##### Meeting Two Hamzas (Second One is Sakin) (اقتاء همزتان والثانية منهما ساكنة)

After converting Hamzat Wasl to a pronounced hamza, certain cases occur where two hamzas meet and the second one is sakin (consonant). In such cases, the second hamza is converted to a madd letter matching the vowel (haraka) of the first hamza [sweed2021]. Table [table_ex_meeting_two_hamza] illustrates this process:

| Uthmani Script | Converting Hamzat Wasl | Final Conversion |
|----------------|------------------------|------------------|
| ٱؤْتُمِنَ       | ءُءْتُمِن                | ءُۥۥتُمِن           |
| ٱئْتُونِى       | ءِءْتُۥۥنِۦۦ              | ءِۦۦتُۥۥنِۦۦ          |

[table_ex_meeting_two_hamza]
The table shows the conversion process for verbs that begin with two connected hamzas. The first stage converts Hamzat Wasl to a hamza followed by kasra or damma. The second stage converts the second hamza to either waw_madd (ۥ) or yaa_madd (ۦ), depending on the vowel of the first hamza. We maintain our established representation where normal madd is represented by two symbols: (اا) for madd_alif, (ۦۦ) for madd_yaa, and (ۥۥ) for madd_waw.



#### Meeting Two Sakin Letters (التقاء الساكنين)

In Arabic language and the Holy Quran, two sakin letters (الحرفان الساكنان) cannot meet consecutively except at pause (وقف), such as pausing on the word (ٱلْأَرْضِ) where the final two letters are sakin. To resolve this meeting, three approaches may be employed:

*   Eliminate the first letter
*   Elongate the first letter
*   Diacritize the second letter with a vowel (fatha, damma, or kasra)

Muslim scholars have simplified this task by comprehensively annotating these rules within the Uthmani script, except for two specific cases:
*   When the first letter is (alif, waw, or yaa): we eliminate the first letter
*   When the first letter is tanween: we convert the tanween to a noon (ن) followed by kasra

Table [table_ex_two_saken] shows how we apply this rule in our phonetization process:

| Uthmani Script | Phonetic Script |
|----------------|-----------------|
| وَقَالَا ٱلْحَمْدُ | وَقَاالَ لحَمدڇ |
| نُوحٌ ٱبْنَهُۥ   | نُۥۥحُنِ بڇنَه   |

[table_ex_two_saken]
The table demonstrates how we resolve the meeting of two sakin letters. The first row shows the meeting of alif (ا) from the word (قَالَا) with the lam (ل) of the word (ٱلْحَمْدُ). In the resulting phonetic script, the alif was deleted. Note that normal madd in (قَالَ) is represented by two alif (اا), and qalqala in the letter daal (د) is represented by (ڇ). The second example shows the meeting of tanween from (نُوحٌ) with the sakin baa (ب) of the word (ٱبْنَهُۥ), resulting in the conversion of tanween to noon with kasra. Note also that normal madd waw is represented with two (ۥۥ) and qalqala for baa (ب) with (ڇ).



#### Shadda (التشديد)

Shadda (ّ) indicates that a letter is doubled or geminated. We represent this by repeating the letter twice, as shown in [table_ex_tasheel].

#### Pausing (الوقف)

Several rules apply at pause (وقف):

*   Vowels (harakat) such as fatha, damma, and kasra are elided, meaning the final letter becomes sakin (ساكن).
*   Small Silah Madd is elided.
*   Taa marboota (ة) is converted to haa (ه).

#### Qalqala (القلقة)

Qalala (قلقة) is defined in tajweed as: "a small sound is followed by on one the letter (ق - ط - ب - ج - د) if one of them is sakin (ساكن) either in between words (وصلا) or at pause (وقفا)"[AlHamad2008]. We dontate this small sound as (ڇ) like in table [table_ex_two_saken].


#### Imala (الإمالة)

Imala (إمالة) is defined in Tajweed as "pronouncing a fatha somewhere between a fatha and a kasra, and an alif somewhere between an alif and a yaa" [sweed2021]. We denote a fatha with imala as `fatha_momala` (۪) and an alif with imala with two `alif_momala` symbols (ــ), similar to the representation of Normal Madd. Table [table_ex_imala] provides an example:

| Uthmani Script | Phonetic Script |
|----------------|-----------------|
| مَجْر۪ىٰهَا     | مَجڇر۪ــهَاا     |

[table_ex_imala]
The table shows how we represent fatha with imala as (۪) and alif with imala as (ــ). The letter jeem (ج) also exhibits qalqala, denoted by (ڇ).


#### Tasheel (التسهيل)

Tasheel is defined in Tajweed as "pronouncing a hamza (ء) with a quality intermediate between a full hamza and the following madd letter, similar to an intermediate vowel (حركة) between fatha, damma, and kasra" [sweed2021]. We denote this facilitated hamza with the symbol `hamza_mosahala` (ٲ). Table [table_ex_tasheel] provides an example:

| Uthmani Script | Phonetic Script |
|----------------|-----------------|
| ءَا۬عْجَمِىٌّ     | ءَٲعجَمِيي       |

[table_ex_tasheel]
The table shows a hamza with Tasheel denoted by (ٲ), along with the disassembly of the letter yaa (ي) with shaddah (ّ) into two yaa symbols.


#### Sakt (السكت)

Sakt is defined in tajweed by "cutting voice without releasing of breathe for short period learned from expert reciters"[AlHamad2008]. Sakat happens in a specified posisions see: [section_hafs_ways]. we dontate sakt by `sakt` 'ۜ'.


#### Implementation

We implemented our phonetic representation by applying 26 operations. Each operation consists of one or more regular expressions, as detailed in: [section_phonemes_operations].

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
### Sifat Level

Sifat (صفة), or in English, attributes of articulation, form a foundational component of our phonetic representation. We based our classification on the classical scholarship of Ibn Al-Jazari. While Ibn Al-Jazari enumerated 17 sifat [AlJazariyyahSwaid], we have excluded 4 of them for the following reasons:

*   **Ismat (إصمات)**: This is a phonological, not a purely phonetic, property.
*   **Ithlaq (إذلاق)**: Similarly, this is a phonological characteristic rather than a phonetic one.
*   **Leen (اللين)**: This attribute is already accounted for within the rules of Madd Al-Leen (مد اللين).
*   **Inhiraf (الانحراف)**: This property explains why the letters lam (ل) and raa (ر) are classified between shidda (شدة) and rakhawa (رخاوة), and is thus subsumed by those attributes.

We have included the sifa of Al-Ghunnah (صفة الغنة), resulting in a system that represents 14 sifat organized into 10 distinct levels, as detailed in table [table_sifa_level_def].


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



Our methodology for transcribing Sifat involves first chunking phonemes by grouping similar phoneme categories and then extracting the Sifat for each phoneme group, as shown in the example [table_example_with_sifat]. Subsequently, we extract the Sifat for every group.

The extraction of Sifat is straightforward, with the exception of Tafkheem and Tarqeeq.

#### Tafkheem and Tarqeeq (التفخيم والترقيق)

Tafkheem (التفخيم) is defined as "thickening that affects a phoneme, causing it to fill the entire mouth" [sweed2021].

In Tajweed, there are 6 levels of Tafkheem and Tarqeeq, ordered from strongest (most mofakham) to weakest (moraqaq):

1.  Mofakham followed by fatha and then madd alif.
2.  Mofakham followed by fatha without madd alif.
3.  Mofakham followed by damma.
4.  Mofakham in a sakin (ساكن) state.
5.  Mofakham followed by kasra.
6.  Moraqaq.

We have formulated these into three labels:

1.  `mofakham` to cover cases 1 to 4.
2.  `moraqaq` to cover case 6.
3.  `low_mofakham` to cover case 5 for the letters (غ, خ, ق), which are monfateh (منفتح) and not motbaq (مطبق). These letters are weakened by a kasra, unlike motbaq letters such as (ص, ض, ط, ظ).

Some phonemes exhibit cases where they can be either moraqaq or mofakham:

*   `madd_alif` (ا): Its Tafkheem or Tarqeeq follows that of the preceding phoneme.
*   `noon_mokhfah` (ں): Its Tafkheem or Tarqeeq follows that of the subsequent phoneme.
*   `raa` (ر) is moraqaq in the following cases:
    *   When followed by a kasra.
    *   When preceded by a sakin yaa (ياء).
    *   When it is sakin (ساكن) and preceded by a mostafel (مستفل) phoneme with a kasra, and not followed by a mosta'lie (مستعلي) phoneme.
    *   When it appears after a hamzat wasl (ٱ).

**Note**: The Mosta'lie (حروف الاستعلاء) letters are (خ, ص, ض, غ, ط, ق, ظ), and the Mostafel (مستفل) letters comprise all others.
