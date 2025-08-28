# Limitations and Future Work  

Our primary limitation is that our dataset consists of golden recitations with no errors, limiting our ability to evaluate performance on real-world data. Although we tested on a few actual samples and successfully detected *madd*, *ghunnah*, and *qalqalah* errors, we need to develop a comprehensive dataset containing error-containing recitations transcribed with our Quran Phonetic Script.  

A secondary limitation arises from attribute-specific articulation patterns: Certain attributes apply exclusively to individual letters, such as `Istitala` for (ض) and `Tikrar` for (ر). Consequently, we expect our model will be unable to capture instances of (ض) without `Istitala` or (ر) without `Tikrar`. This limitation similarly applies to Tajweed rules that occur less frequently in the Holy Quran, such as `Imala`, `Rawm`, and `Tasheel`.  
