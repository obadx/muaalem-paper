# Related Work

## Quran Prounciatin Datasets

We will talk here the most important datasets. [everyayah](everyayah.com) is the largets openly available dataset with 26 complete moshaf segmented and annotead by Ayah for expert like Al Hossary and non expoerts like: Fares Abbad. 1509 utterance of single aya to label three rules Madd, Ghonna and Ikhfaa, Althoug the scale of the data is realy small but it was widelly adopted buy community [10092350], [10092350], and [shaiakhmetov2025evaluation] because of it is open source. Tarteel v1 [khan2021tarteel] dataset which conssits of 25K utterance with diclication with no Tajweed rules. The last one is the Tarteel [tarteelai] private dataset which is massive 9k hours of annoated diarctized with no Tajweed rules.


## Quran Prouncication Models

To our kowledge the first work to address and build Automation Prounciatin assesment for the Holy Quran is RDI [sherif2007enhancing] which has build a complete system for detecting various prouncication erros. The work does not mention which erros they include and exclued but they mentioned testing rules of Qalqal, Idgham and Iqlab. They alos do not mentin how they phonize quranic words. Following the work they continue with [abdou2014computer] and [al2018computer] using Deep Neural Netwrok replacing HMMs improving their system. Many studies relies on modeling phoneme duration to model duration related rules like Madd and Ghonna like: [mohammed2017recognition], [alqadasi2023improving] but with limited datasets and on limted verses not the whole Quran. Others consentrate their efforts on detection specific rule like Qlaqla: [10092350] and for Ghonna and Madd: [shaiakhmetov2025evaluation], [10485145]. But most of the efforts except for RDI work train on a very small scale datasets of on specfic chapters of the Holy Quran.

To this point comes Tarteel [tarteelai] although they did not add tajweed rules but they build robust ASR ssytem for detecting charcters with diarctization. The developed a crowd-sourced dataset [khan2021tarteel] consits of 25k utterances with 68 hours and they extened it from their application users to 9k hours of private annotated data. 
The best work aligns with our notion for building for ssystem to detect All types of mistakes including Tajweed and Sifat (attributes of articulations) is [putra2012developing] Althout this work is relying on HMMs and is trained on too little data length they introudced the idea of mulilevel detection system: level for the Makhraj (phoneme level) and level of the tajweed rules (Tajweed rules level)




## Pre-trained Speech Encoders with Self Supervsed Learning (SSL)

The idea of pre-training for speech begins too early [hinton2006reducing] but it was limited bysequentional natual of recurunet nural networks (RNNs) [hopfield1982neural] but the riase of tranformers [vaswani2017attention] architrecture faciliates far more paralizations on GPUs allowing to train with more data with bigger models that results for pretraining on large piece of text with Masked Lanugge Model BERT [devlin2019bert] soon the idea reached to speech with wav2vec [schneider2019wav2vec] and wav2vec2 which extened the idea with product quntization [baevski2020wav2vec] then the conformer replaces vanila transformes for speech by utlizing convolution [gulati2020conformer] then comes Google Wav2Vec2BERT [chung2021w2v] that with using the idea of MLM in speech finally Facebook extened pretraining of Wav2Vec2BERT [barrault2023seamless] to 4.5 M hours including 110K Arabic hours which is ideal for low resourced langugre fine-tuning.


