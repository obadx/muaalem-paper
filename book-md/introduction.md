# Introduction

The Holy Qurn in the word of ALLAH. The book that he choses for the Humanity until day of judgment. Althought this book is fully Arabic, pepople for other nations can learn to recite it eventhough they do not know Arabic. For this ALLAH says: ﴿ وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍ ﴾ "And We have certainly made the Qur'an easy for remembrance, so is there any who will remember?". Sevral efforts have been made to untilze Aritficial Intellagance (AI) to help Holy Quran Learners to recite it [abdou2014computer], [al2018computer], [ahmed2017arabic]. But the lake of data and poor represnetation of Quran and Tajweed (التجويد)rules  have made the taks seems hard to accomplish.

So launch this project: It is not only a master thesis but it is a complete project to serve three types of people:

* Muslims: Make the Holry Quran to Musilms in the eara of AI.
* Developers: by developing an Software Devlopment Kit (SKD) deployable on all devices including desktops, cloud and edge devices
* Researcher: by contributing this research as completly open source including: data, codes and models.

This thesis marks as the first step which is builing a foundational model which we have achieved thank to ALLAH.

Assessing pronunciation is not a simple task [kheir2023automatic], as it does not only rely on pronouncing phonemes correctly but also involves other factors like intonation, prosody, and stress. Does learning these mean one is done? No—other factors include fluency and completeness [kheir2023automatic]. However, the Holy Quran presents unique characteristics: it is among the easiest spoken texts to learn despite containing special phonemes absent in other languages.  

The pronunciation of the Holy Quran is governed by rigorously strict rules formally defined by ancient Muslim scholars since the 6th century. Despite their beauty and precision, these rules have not been comprehensively digitized (to our knowledge) for Quranic pronunciation assessment.  

Although RDI pioneered computer-aided Quranic instruction [sherif2007enhancing], they neither disclosed their phoneticization process nor released data/models. Consequently, new research must start from basics: defining phoneticization, data, and models. To bridge this gap, we introduce:  

* **A Phonetizer**: Encodes *all* Tajweed rules and articulation attributes (*Sifat*) defined by classical scholars, except *Ishmam* (إشمام)  
* **A 98% automated pipeline**: Generates highly accurate datasets from expert recitations  
* **A dataset**: ~300K annotated utterances (890 hours)  
* **Integration**: Our multi-level CTC model proves the Quranic phonetic script is learnable (0.16% average phoneme error rate)  

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
* **Appendix**: Details on *Mushaf* attributes and algorithms  
