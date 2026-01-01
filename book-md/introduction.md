# Introduction

The Holy Quran is the word of Allah, the book He chose for humanity until the Day of Judgment. Although this book is entirely in Arabic, people from other nations can learn to recite it even if they do not know the Arabic language. Regarding this, Allah says:  
> ﴿ وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍ ﴾  
“And We have certainly made the Qur’an easy for remembrance, so is there any who will remember?” (Surah Al-Qamar, 54:17)  

Several efforts have been made to utilize Artificial Intelligence (AI) to help Holy Quran learners recite it properly [abdou2014computer], [al2018computer], [ahmed2017arabic]. However, the lack of data and poor representation of Quranic recitation and Tajweed rules have made the task difficult to accomplish.

This project is launched not only as a master’s thesis but as a comprehensive initiative to serve three groups of people:

- **Muslims**: Making the Holy Quran accessible in the era of AI.
- **Developers**: By developing a Software Development Kit (SDK) deployable on all devices, including desktops, cloud, and edge devices.
- **Researchers**: By contributing this research as fully open source, including data, code, and models.

This thesis represents the first step: building a foundational model, which, by the grace of Allah, we have achieved.

Assessing pronunciation is not a simple task [kheir2023automatic], as it involves not only correct phoneme articulation but also factors such as intonation, prosody, and stress. Furthermore, fluency and completeness are also essential [kheir2023automatic]. However, the Holy Quran possesses unique characteristics: it is among the easiest spoken texts to learn, despite containing phonemes absent in other languages.

The pronunciation of the Holy Quran is governed by rigorously defined rules formalized by classical Muslim scholars since the 6th century. Despite their precision and beauty, these rules have not been comprehensively digitized (to our knowledge) for automated Quranic pronunciation assessment.

Although the RDI company pioneered computer-aided Quranic instruction [sherif2007enhancing], they did not disclose their phoneticization process or release data or models. As a result, new research must start from the basics: defining phoneticization, data, and models. To bridge this gap, we introduce:

- **A Phonetizer**: Encodes *all* Tajweed rules and articulation attributes (*Sifat*) defined by classical scholars, except *Ishmam* (إشمام).
- **A 98% Automated Pipeline**: Generates highly accurate datasets from expert recitations.
- **A Dataset**: 286K annotated utterances (848 hours).
- **Integration**: Our multi-level CTC model demonstrates the learnability of the Quranic phonetic script (achieving a 0.21% average phoneme error rate).

The Thesis is organized as follows:

- **Related Work**: Expands on the strengths and weaknesses of prior research.
- **Quran Phonetic Script**: Introduces our two-level script: **phonemes** and **Sifat** (10 attributes → 11 total levels).
- **Data Pipeline**: Stages include:  
  (1) Digitized Quran script as foundation,  
  (2) *Hafs* methodology criteria,  
  (3) Expert recitation collection,  
  (4) Segmentation at pause points (وقف),  
  (5) Segment transcription,  
  (6) Validation via *Tasmee* (تسميع) algorithm.  
- **Modeling**: Demonstrates the learnability of the phonetic script.
- **Results**: Analysis of outcomes.
- **Limitations & Future Work**: Proposed research directions.
- **Conclusion**: Summary of contributions.
