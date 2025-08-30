# Data Preparation

The data preparation process began with the definition of clear selection criteria. Our objective was to compile recitations from world-class experts to serve as reference models for evaluating Quranic learners. This study focuses exclusively on the *Hafs* *riwayah* (رواية حفص) due to its status as the most prevalent recitation method globally.

Acknowledging that manual annotation is prohibitively time-consuming, we developed a data collection pipeline that is approximately 98% automated. The procedure consists of the following steps:

1.  Selection of a digitized Quranic script as the foundational text.
2.  Definition of precise criteria for the *Hafs* methodology.
3.  Collection of expert recitations.
4.  Segmentation of audio at pause points (وقف).
5.  Transcription of the segmented audio.
6.  Data validation using a *Tasmee'* (تسميع) algorithm.
7.  Extraction of a phonetic script using our custom Quran Phonetic Script.

For the purposes of this work, a *Moshaf* is defined as a complete recitation of the Quran (chapters 1-114) by a single reciter. The statistics of the collected dataset are summarized in Table [table_all_data_stat].

| Moshaf ID | Hours         | Recitation Count |
|-----------|---------------|------------------|
| 0.0       | 28.48         | 9,133            |
| 0.1       | 40.31         | 10,764           |
| 0.2       | 49.47         | 9,971            |
| 0.3       | 37.19         | 12,604           |
| 1.0       | 28.41         | 10,939           |
| 2.0       | 51.05         | 9,942            |
| 2.1       | 30.03         | 10,394           |
| 3.0       | 25.19         | 10,444           |
| 4.0       | 29.12         | 10,994           |
| 5.0       | 28.02         | 11,482           |
| 6.0       | 39.39         | 12,435           |
| 7.0       | 28.26         | 9,907            |
| 8.0       | 30.86         | 10,330           |
| 9.0       | 27.95         | 10,642           |
| 11.0      | 24.01         | 10,363           |
| 12.0      | 33.42         | 9,880            |
| 13.0      | 33.99         | 9,377            |
| 19.0      | 30.11         | 11,278           |
| 22.0      | 28.11         | 10,332           |
| 24.0      | 28.51         | 9,868            |
| 25.0      | 16.93         | 7,922            |
| 26.0      | 30.44         | 11,565           |
| 26.1      | 32.71         | 11,850           |
| 27.0      | 28.05         | 11,213           |
| 28.0      | 31.05         | 10,535           |
| 29.0      | 27.79         | 11,061           |
| 30.0      | 29.14         | 11,312           |
| **Total** | **847.99**    | **286,537**      |
[table_all_data_stat]
*Table : Summary of the proposed dataset. The final collection comprises approximately 848 hours of audio, totaling over 286,000 individual recitation segments.*
