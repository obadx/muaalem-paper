# Introduction

Holy Quran is the holy book of Islam. Muslims believe that it is the word of Allah (God). Reciting the holy Quran is part of the day to day activity of every Muslim. So learning to recite it correctly is vital for them. Muslims seek to learn how to recite holy Quran correctly but they face some challenges: Some areas of the world have low Muslim density or teachers, or with their availability. Although some chatting application may solve the problem, some poor areas like in Africa have limited access to the internet. Although some solutions like Tarteel [tarteelai] have very good application to correct recitation errors on character and diacritization level, it lacks reliability and support for Tajweed rules.

Assessing pronunciation is not a simple task [kheir2023automatic], as it does not only rely on pronouncing phonemes correctly but also involves other factors like intonation, prosody, and stress. Does learning these mean one is done? No—other factors include fluency and completeness [kheir2023automatic]. However, the holy Quran presents unique characteristics: The pronunciation of the holy Quran is governed by rigorously strict rules formally defined by ancient Muslim scholars since the 6th century. Despite their beauty and precision, these rules have not been comprehensively digitized (to our knowledge) for Quranic pronunciation assessment.

Many research works were published since 2006 to develop computer aided pronunciation learning for the holy Quran. Despite paper publishing, there is no way to replicate the work of other researchers because they did not disclose their code or the data. So replicating the other research work is very hard. Consequently, new research must start from basics: defining phoneticization, data, and models. To bridge this gap, we introduce:

* **A Phonetizer**: Encodes *all* Tajweed rules and articulation attributes (*Sifat*) defined by classical scholars, except *Ishmam* (إشمام) working as a multi-level text representation for the input speech.
* **A 98% automated pipeline**: Generates highly accurate datasets from expert recitations.
* **A dataset**: ~300K annotated utterances (830 hours).
* **Qdat Bench**: an out-of-distribution benchmark for recitations with errors (120 female and 39 male).
* **Muaalem Model**: Our multi-level CTC model proves the Quranic phonetic script is learnable and this model can be hosted on device solving limited internet access of poor countries.

And more important thing with opensource our: model, code, and data.

The paper is organized as follows:
* **Related Work**: Expands on strengths/weaknesses of prior research
* **Quran Phonetic Script**: Introduces our two-level script: **phonemes** and **Sifat** (10 attributes → 11 total levels)
* **Data Pipeline**: Stages include:
  (1) Digitized Quran script as foundation
  (2) *Hafs* methodology criteria
  (3) Expert recitation collection
  (4) Segmentation at pause points (وقف)
  (5) Segment transcription
  (6) Validation via *Tasmee* (تسميع) algorithm
* **Modeling**: Demonstrates learnability of the phonetic script
* **Results**: Analysis of outcomes
* **Limitations & Future Work**: Next research directions
* **Conclusion**: Summary of contributions
* **Appendix**: Details on *Mushaf* attributes, Tasmeea algorithm, and Qdat Bench







# Introduction

The Holy Quran is the central religious text of Islam, believed by Muslims to be the word of Allah (God). Its recitation is a daily practice for Muslims worldwide, making correct pronunciation a fundamental priority. However, learners face significant challenges: many regions have low Muslim populations and limited access to qualified teachers, while economically disadvantaged areas—particularly in parts of Africa—lack reliable internet connectivity. Although some applications like Tarteel [tarteelai] address recitation errors at the character and diacritization level, they do not fully support the complex Tajweed (pronunciation rules) required for proper Quranic recitation.

Assessing pronunciation is inherently complex [kheir2023automatic], requiring not only accurate phoneme production but also proper intonation, prosody, and stress. Furthermore, fluency and completeness remain essential evaluation criteria [kheir2023automatic]. The Quran presents unique additional characteristics: its pronunciation is governed by strict rules (Tajweed rules) codified by Muslim scholars since the 6th century. Despite their precision, these rules have not been comprehensively digitized for automated assessment, creating a critical gap in computational tools for Quranic education.

Since 2006, numerous studies have proposed computer-aided pronunciation learning systems for the Quran. However, these works remain irreproducible due to undisclosed code and data, forcing each new research effort to restart from fundamental definitions of phoneticization, datasets, and models. To address this systemic gap, we introduce:

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

