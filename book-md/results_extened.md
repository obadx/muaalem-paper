# Ablation Studies

We ran more than 13 expriements. In ourder to tune weights per every level we ran an evaluation set for every experiemnt on 20% of the data while logging Phoneme Error Rate (PER) per every level. Our goal is to mimimize two things:
* Avergage Phoneme Error Rate (PER).
* Standard Devication accros all levels.

We log her best three experiemnts called `EXP1`, `EXP2`, and `EXP3`. We tried every loss weight for every level. We make `phonemes` level weith constant accross all runs with 0.4 and we change `shidda_or_rakhawa` and `tafkheem_or_tarqeeq` every time to get the best results possible.


| Attribute | EXP1 | EXP2 | EXP3 |
|-----------|-------| ----- | --- |
| phonemes | 0.4  | 0.4 | 0.4 |
| tikraar | 0.06 | 0.058625 | 0.059625 |
| tafkheem_or_tarqeeq | 0.06  | 0.063 | 0.0060 |
| tafashie | 0.06 | 0.05825 | 0.059625 |
| Qalqala | 0.06 | 0.0585| 0.059625  |
| Safeer | 0.06| 0.05825 | 0.059625 |
| Shidda_or_rakhawa | 0.06  | 0.068| 0.059625|
| Istitala | 0.06| 0.05825 | 0.059625 |
| Itbaaq | 0.06| 0.05825 | 0.059625 |
| Ghonna | 0.060 | 0.05825 | 0.059625 |
| hams_or_jahr | 0.06| 0.05825 | 0.059625|
| average_per | 0.065  | 0.05825 | 0.059625|
| std_per |0.06|0.05825 |0.059625 |
[table_results_v2_weights]
The table showes diffrent loss weight applied to equation [loss_equation] for 3 experiemnts: `EXP1`, `EXP` and `EXP3`. We made `phonemes` level constant accross all runs. In every run we tune the weight for `shidda_or_rakhawa` and `tafkheem_or_tarqeeq` to get the maximum average Phoneme Error Rate (PER) and mimum standard deviation accross all runs. Note that the sum of all loss weiths adds to 1.

We notice that the last expeiemnt is the best one with average PER of 0.293% and with standard devication of 0.0017. as shown for both Table [table_results_v2] and the figure [figure_results_v2_std]. The `EXP3` is the best one because it gives more wight to levels that have more labels: `shidda_or_rakhawa` and the more challenging to learn `tafkheem_or_tarqeeq` without having sifnificat diffrence between the rest of levels

![Average Phoneme Error Rate and Standrad Deviation for all the 3 runs showing that the `EXP3` is the best one because it gives more wight to levels that have more labels: `shidda_or_rakhawa` and the more challenging to learn `tafkheem_or_tarqeeq` without having sifnificat diffrence between the rest of levels](./figures/results_stats_v2.png)




| Attribute | EXP1 | EXP2 | EXP3 |
|-----------|-------| ----- | --- |
| phonemes | 0.0069  | 0.0069 | 0.0063 |
| tikraar | 0.006 | 0.006 |0.0017 |
| tafkheem_or_tarqeeq | 0.002599  | 0.00279 | 0.0065 |
| tafashie | 0.001837 | 0.0025 | 0.0035 |
| Qalqala | 0.001808 | 0.008 | 0.00174  |
| Safeer | 0.00346 | 0.00246 | 0.00174 |
| Shidda_or_rakhawa | 0.015276  | 0.0053| 0.0031|
| Istitala | 0.00243 | 0.00166 | 0.001525 |
| Itbaaq | 0.00176 | 0.00217 | 0.00168 |
| Ghonna | 0.044 | 0.02675 | 0.00199 |
| hams_or_jahr | 0.0024  | 0.00256 | 0.00234|
| average_per | 0.0080455  | 0.006 | 0.00293|
| std_per |0.0191  |0.0062 |0.0017 |
[table_results_v2]
Phoneeme Error Rate on every level on 20% of training data. `EXP3` is the best one because it gives more wight to levels that have more labels: `shidda_or_rakhawa` and the more challenging to learn `tafkheem_or_tarqeeq` without having sifnificat diffrence between the rest of levels



![The figure showes the evaluation PER every 20% training steps slowing done nicely which indicated the model is acutalll learning](./figures/eval_v2_plot.png)
