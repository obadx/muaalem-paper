# Limitations and Future Work  

Our primary limitation is that our dataset consists of golden recitations with no errors, limiting our ability to evaluate performance on real-world data. Although we tested on a few actual samples and successfully detected *madd*, *ghunnah*, and *qalqalah* errors, we need to develop a comprehensive dataset containing error-containing recitations transcribed with our Quran Phonetic Script.  

A secondary limitation arises from attribute-specific articulation patterns: Certain attributes apply exclusively to individual letters, such as `Istitala` for (ض) and `Tikrar` for (ر). Consequently, we expect our model will be unable to capture instances of (ض) without `Istitala` or (ر) without `Tikrar`. This limitation similarly applies to Tajweed rules that occur less frequently in the Holy Quran, such as `Imala`, `Rawm`, and `Tasheel`.  


## Future Work  

To address these limitations, we plan to:  

1.  **Develop an Error-Included Dataset**:  
    Collect and annotate a large-scale dataset of learner recitations containing common Tajweed errors, transcribed using our phonetic script. This will enable more robust model training and evaluation.  

2.  **Expand to Other Recitation Styles (Riwayat)**:  
    Extend the phonetic script and modeling framework to support additional recitation styles (e.g., Warsh or Qalun), facilitating broader applicability across the Muslim world.  

3.  **Deploy and Evaluate in Real-World Settings**:  
    Integrate the model into user-friendly applications and evaluate its effectiveness in real-world learning environments, incorporating feedback from Quran teachers and students to iteratively improve the system.  

By addressing these challenges, we aim to advance the state of Quranic pronunciation assessment and make automated, accurate feedback accessible to learners worldwide.
