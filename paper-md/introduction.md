# Introduction

The Holy Quran is the central religious text of Islam, believed by Muslims to be the word of Allah (God). Its recitation is a daily practice for Muslims worldwide, making correct pronunciation a fundamental priority. However, learners face significant challenges: many regions have low Muslim populations and limited access to qualified teachers, while economically disadvantaged areas—particularly in parts of Africa—lack reliable internet connectivity. Although some applications like Tarteel [tarteelai] address recitation errors at the character and diacritization level, they do not fully support the complex Tajweed (pronunciation rules) required for proper Quranic recitation.

Assessing pronunciation is inherently complex [kheir2023automatic], requiring not only accurate phoneme production but also proper intonation, prosody, and stress. Furthermore, fluency and completeness remain essential evaluation criteria [kheir2023automatic]. The Quran presents unique additional characteristics: its pronunciation is governed by strict rules (Tajweed rules) codified by Muslim scholars since the 6th century. Despite their precision, these rules have not been comprehensively digitized for automated assessment, creating a critical gap in computational tools for Quranic education.

Since 2006, numerous studies have proposed computer-aided pronunciation learning systems for the Quran like RDI [sherif2007enhancing]. However, these works remain irreproducible due to undisclosed code and data, forcing each new research effort to restart from fundamental definitions of phoneticization, datasets, and models. Although recent efforts like [abdelfattah2025automatic] has introuced a benchmark in Modern Standard Arabic (MS) reciting the holy Quran but it lacks an existance of Tjaweed rules. To address this systemic gap, we introduce:

* **A Phonetizer**: Encodes *all* Tajweed rules and articulation attributes (*Sifat*) defined by classical scholars, except *Ishmam* (إشمام), as a multi-level text representation for input speech
* **A 98% automated pipeline**: Generates highly accurate datasets from expert recitations
* **A dataset**: ~300K annotated utterances (830 hours)
* **Qdat Bench**: An out-of-distribution benchmark for erroneous recitations (120 female and 39 male speakers)
* **Muaalem Model**: A multi-level CTC model demonstrating that our Quranic phonetic script is learnable and suitable for on-device deployment, addressing internet accessibility constraints

Most importantly, we fully open-source our model, code, and data to enable reproducible research.

The paper is organized as follows:  
* **Related Work**: Analyzes strengths and weaknesses of prior research  
* **Quran Phonetic Script**: Details our two-level encoding—phonemes and *Sifat* (10 attributes → 11 total levels)  
* **Data Pipeline**: Describes six stages: (1) Digitized Quran script, (2) *Hafs* methodology criteria, (3) Expert recitation collection, (4) Pause-based segmentation (وقف), (5) Segment transcription, and (6) *Tasmee* (تسميع) validation  
* **Modeling**: Demonstrates script learnability through our architecture  
* **Results**: Presents outcome analysis  
* **Limitations & Future Work**: Identifies research directions  
* **Conclusion**: Summarizes contributions  
* **Appendix**: Provides details on *Mushaf* attributes, Tasmeea algorithm, and Qdat Bench

