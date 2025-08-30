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


| Phoneme Name          | Symbol | الحرف  بالعربية                          |
|-----------------------|--------|--------------------------------------|
| hamza                 | ء      | همزة                                 |
| baa                   | ب      | باء                                  |
| taa                   | ت      | تاء                                  |
| thaa                  | ث      | ثاء                                  |
| jeem                  | ج      | جيم                                  |
| haa_mohmala           | ح      | حاء                                  |
| khaa                  | خ      | خاء                                  |
| daal                  | د      | دال                                  |
| thaal                 | ذ      | ذال                                  |
| raa                   | ر      | راء                                  |
| zay                   | ز      | زاي                                  |
| seen                  | س      | سين                                  |
| sheen                 | ش      | شين                                  |
| saad                  | ص      | صاد                                  |
| daad                  | ض      | ضاد                                  |
| taa_mofakhama         | ط      | طاء                                  |
| zaa_mofakhama         | ظ      | ظاء                                  |
| ayn                   | ع      | عين                                  |
| ghyn                  | غ      | غين                                  |
| faa                   | ف      | فاء                                  |
| qaf                   | ق      | قاف                                  |
| kaf                   | ك      | كاف                                  |
| lam                   | ل      | لام                                  |
| meem                  | م      | ميم                                  |
| noon                  | ن      | نون                                  |
| haa                   | ه      | هاء                                  |
| waw                   | و      | واو                                  |
| yaa                   | ي      | ياء                                  |
| alif                  | ا      | نصف مد ألف                                  |
| yaa_madd              | ۦ       | نصف مد ياء
| waw_madd              | ۥ       | نصف مد واوا
| fatha                 | َ       | فتحة                                 |
| dama                  | ُ       | ضمة                                 |
| kasra                 | ِ       | كسرة                                 |
| fatha_momala          | ۪       | فتحة ممالة 
| alif_momala           | ـ       | ألف ممالة
| hamza_mosahala        | ٲ       | همزة مسهلة                           |
| qlqla                 | ڇ       | قلقة                                 |
| noon_mokhfah          | ں       | نون مخفاة                            |
| meem_mokhfah          | ۾       | ميم مخفاة                            |
| sakt                  | ۜ       | سكت                                  |
| dama_mokhtalasa       | ؙ       | ضمة مختلسة (عند الروم في تأمنا)
[table_phonemes_level_def]. The table shows our defening for the phonemes level for the Quran Phonetic Script by (43) phonemes.

### Sifat (Attributes) (10)

| Sifat (English)        | Sifat (Arabic)       | Available Attributes (English)          | Available Attributes (Arabic)       |
|------------------------|----------------------|----------------------------------------|-------------------------------------|
| hams_or_jahr         | الهمس أو الجهر     | hams, jahr                           | همس, جهر                          |
| shidda_or_rakhawa    | الشدة أو الرخاوة  | shadeed, between, rikhw              | شديد, بين بين, رخو                     |
| tafkheem_or_taqeeq   | التفخيم أو الترقيق | mofakham, moraqaq, low_mofakham                    | مفخم, مرقق, أدنى المفخم                         |
| itbaq                | الإطباق            | monfateh, motbaq                     | منفتح, مطبق                        |
| safeer               | الصفير             | safeer, no_safeer                    | صفير, لا صفير                      |
| qalqla               | القلقلة            | moqalqal, not_moqalqal               | مقلقل, غير مقلقل                   |
| tikraar              | التكرار            | mokarar, not_mokarar                 | مكرر, غير مكرر                     |
| tafashie             | التفشي             | motafashie, not_motafashie           | متفشي, غير متفشي                   |
| istitala             | الاستطالة          | mostateel, not_mostateel             | مستطيل, غير مستطيل                 |
| ghonna               | الغنة              | maghnoon, not_maghnoon               | مغنون, غير مغنون                   |
[table_sifa_level_def]. The table showes sefining 14 sifa (صفة) as 10 levels.



### Development Methodology  

1. **Imlaey to Uthmani Conversion**: where convert Imlaey Script to Uthmani Script as we rely on Uthmani script to construct Quran Phoneme Script.
2. **Uthmani to Phonetic Script Conversion**: where we convert Uthmani Script to Quran Phonetic Script. 

