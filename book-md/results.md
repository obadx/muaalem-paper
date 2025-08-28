# Results  

We trained on all mosahf provided above, reserving moshaf `26.1` and `19.0` for testing. The evaluation results are presented below:  

| Metric                          | Value     |
|---------------------------------|-----------|
| test__loss                      | 0.01162   |
| test__per_phonemes              | 0.00543   |
| test__per_hams_or_jahr          | 0.00117   |
| test__per_shidda_or_rakhawa     | 0.00172   |
| test__per_tafkheem_or_taqeeq    | 0.00167   |
| test__per_itbaq                 | 0.00092   |
| test__per_safeer                | 0.00132   |
| test__per_qalqla                | 0.00085   |
| test__per_tikraar               | 0.0009    |
| test__per_tafashie              | 0.0016    |
| test__per_istitala              | 0.0008    |
| test__per_ghonna                | 0.0013    |
| test__average_per               | 0.0016    |

We achieved an Average Phoneme Error Rate (PER) of **0.16%**, demonstrating that our Quran Phonetic Script can be learned efficiently by the model.  
