# Results  

We trained our model on all available Mushaf recitations, reserving Mushaf 26.1 and 19.0 exclusively for testing. The evaluation results are summarized in Table [table_results]. The achieved Average Phoneme Error Rate (PER) of 0.16% strongly supports our hypothesis that the Quran Phonetic Script is learnable using modern speech processing techniques.

We further tested the model on actual samples containing errors in *Madd*, *Ghunnah*, *Qalqalah*, and *Tafkheem*. Despite being trained only on error-free expert recitations, the model successfully detected these common pronunciation mistakes. While these preliminary results are promising, a more comprehensive evaluation on dedicated error-annotated datasets—such as [khan2021tarteel]—is planned for future work.

We observe that the PER is well-balanced across nearly all phonetic and attribute levels, with the exception of the phoneme level itself. This is expected, as the phoneme level has a significantly larger vocabulary (44 symbols, including padding), increasing its complexity relative to the attribute levels.

| Metric                      | Value     |
|-----------------------------|-----------|
| loss                        | 0.01162   |
| per_phonemes                | 0.00543   |
| per_hams_or_jahr            | 0.00117   |
| per_shidda_or_rakhawa       | 0.00172   |
| per_tafkheem_or_taqeeq      | 0.00167   |
| per_itbaq                   | 0.00092   |
| per_safeer                  | 0.00132   |
| per_qalqla                  | 0.00085   |
| per_tikraar                 | 0.00090   |
| per_tafashie                | 0.00160   |
| per_istitala                | 0.00080   |
| per_ghonna                  | 0.00130   |
| average_per                 | 0.00160   |

[table_results]
*Test results on Mushaf 26.1 and 19.0. The Average Phoneme Error Rate (PER) is **0.16%**, confirming the learnability of the Quran Phonetic Script. The phoneme-level PER is higher (0.54%) due to its larger vocabulary.*

To evaluate real-world performance, we developed a demonstration application using [Gradio](https://www.gradio.app/). The interface allows users to record or upload their recitations and receive immediate phonetic and attribute-level feedback.

![Gradio Web App interface allowing users to test our model.](./figures/gradio_ui_main.png)

![Gradio Web App interface showing detailed Sifat (attribute) level feedback.](./figures/gradio_ui_sifa.png)

User feedback has been extremely positive. Notably, the model generalized well to female voices despite being trained exclusively on male recitations, successfully detecting common errors such as incorrect *Madd* elongation or weak *Qalqalah* pronunciation. This demonstrates the robustness and practical applicability of our approach.
