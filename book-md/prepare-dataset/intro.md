# Data Preparation  

To prepare the data, we first defined selection criteria. We aimed to collect recitations from the best reciters worldwide to serve as references for judging Quran learners. In our study, we considered only *Hafs* riwayah (رواية حفص) as it's the most popular recitation method globally. Recognizing that manual data annotation requires significant effort and time, we created a 98% automated pipeline for data collection. The steps are:  

(1) Choose a digitized Quran script as the project foundation  
(2) Define criteria for *Hafs* methodology  
(3) Collect expert recitations  
(4) Segment recitations at pause points (وقف)  
(5) Transcribe segments  
(6) Validate data through *Tasmee* (تسميع) Algrithm
(7) Extrac Phonetic Script using our Quran Phonetic Script

We define a *Moshaf* as a complete Quran recitation (chapters 1-114) by a specific reciter. Statistics are summarized in Table [table_all_data_stat]

| Moshaf ID | Hours         | Length |
|-----------|---------------|--------|
| 0.0       | 28.47721296   | 9133   |
| 0.1       | 40.31257093   | 10764  |
| 0.2       | 49.46541671   | 9971   |
| 0.3       | 37.18758118   | 12604  |
| 1.0       | 28.40784367   | 10939  |
| 2.0       | 51.04665234   | 9942   |
| 2.1       | 30.02847051   | 10394  |
| 3.0       | 25.19377593   | 10444  |
| 4.0       | 29.12333379   | 10994  |
| 5.0       | 28.01777693   | 11482  |
| 6.0       | 39.38568468   | 12435  |
| 7.0       | 28.25627201   | 9907   |
| 8.0       | 30.85935158   | 10330  |
| 9.0       | 27.95178738   | 10642  |
| 11.0      | 24.00685052   | 10363  |
| 12.0      | 33.42429862   | 9880   |
| 13.0      | 33.99108879   | 9377   |
| 19.0      | 30.11410843   | 11278  |
| 22.0      | 28.10947704   | 10332  |
| 24.0      | 28.51243509   | 9868   |
| 25.0      | 16.92910042   | 7922   |
| 26.0      | 30.44461112   | 11565  |
| 26.1      | 32.71190443   | 11850  |
| 27.0      | 28.05097968   | 11213  |
| 28.0      | 31.05318768   | 10535  |
| 29.0      | 27.78900316   | 11061  |
| 30.0      | 29.14366461   | 11312  |
| **Total** | **847.9944402** | **286537** |
[table_all_data_stat]
The table shows statiscs of our proposed dataset totaling 286K recitations with 848 hours

