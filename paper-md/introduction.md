# Introudtion

Assessning Prounciation is not a simple task [kheir2023automatic] as it is not only rely on prunciation phonemes correctlry but there are another factors llike annotation, prsedoy and stress. If you succeed to learn these things you are done? No, another factors incluedes fluency and completeness [kheir2023automatic]. But when comes to the Holy Quran it is another thing: The Holy Quran has very unique features that makes it the easiest spken words to learn even it has some special phonemes that does not exits in the other languages.

The Prounciation of the Holy Quran is governed by rigrously strict prounication rules. These rules were formlly defined and measured by acient Muslim scholarks form the 6th century. Despite the beuity and regrousty of these rules no one has defined them in a  digitalized mannar (to our knowlege) that can be used by prounciation assestment for the Holy Quarn.

Despite great work done by RDI (first work to create compute aided programe to teach Holy Quran rules) [sherif2007enhancing] they did not reveal their phonetization process neither the data or opensource the model. For that every new research addressing this problem nearly start from the very basics to define every thing: define the phonetization, data and model. So we want to  bridge this gap by introudcing:

* Phonetizer: that encodes **all** tajweed and attributes of articulation (sifat) defined by the acinet musolt scholars excpet for rule of Ishmam (إشمام)
* A 98% automated pipline to create a very accurate dataset from expert reciters
* A dataset consits of nearly 300k annotted utterance with 890 hour
* Gluing all things up by introudcing our Multi-level CTC model and prove that the Quran Phonetic script is indeed learnable by achieving 0.16% average phoneme error rate

The rest of the paper is organized as follows:

* Related Work section expands weekneess and strenthes
* Quran Phonetic Script where we intorucde our Quran phonecitc script tha is composed ot two levels: **phonems** level and  **sifat** level compsed of 10 attributes resulting for `11` levels
* Our data preparaing pipline which we show differnct stating including: (1) Choose a digitized Quran script as the project foundation  
(2) Define criteria for *Hafs* methodology  
(3) Collect expert recitations  
(4) Segment recitations at pause points (وقف)  
(5) Transcribe segments  
(6) Validate data through *Tasmee* (تسميع) Algrithm
* Modeling where we prove theat Quran phonetic script can be learned succssfully
* Result where we analyze the results
* Limitation and future work: where we dfine our next work direction
* Conclusion where we conclude our work
* Appendict where we talk about details like Moshaf Attributes and Algorithms used to create this work

