# Results  

We trained on all mosahf provided above, reserving mosahf `19.0`, `29.0`, and `30.0` for testing. The evaluation results are presented below:  

| Metric                          | Value     |
|---------------------------------|-----------|
| test__loss                      | 0.01196   |
| test__per_phonemes              | 0.00538   |
| test__per_hams_or_jahr          | 0.00144   |
| test__per_shidda_or_rakhawa     | 0.00267   |
| test__per_tafkheem_or_taqeeq    | 0.00219   |
| test__per_itbaq                 | 0.00100   |
| test__per_safeer                | 0.00146   |
| test__per_qalqla                | 0.00094   |
| test__per_tikraar               | 0.00427   |
| test__per_tafashie              | 0.00146   |
| test__per_istitala              | 0.00087   |
| test__per_ghonna                | 0.00128   |
| test__average_per               | 0.00209   |

We achieved an Average Phoneme Error Rate (PER) of **0.21%**, demonstrating that our Quran Phonetic Script can be learned efficiently by the model. The phoneme level remains the most challenging at 0.538% due to its larger 44-symbol vocabulary (including padding).  
