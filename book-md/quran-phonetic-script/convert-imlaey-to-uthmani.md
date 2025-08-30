# Converting Imlaey Script to Uthmani Script

As mentioned, we selected the Uthmani script as our foundation because:
- It contains specialized Tajweed diacritics (Madd, Tasheel, etc.).
- It preserves pause rules critical for recitation (e.g., stopping on رحمت).

To facilitate this conversion, we created an annotation UI to manually annotate misaligned words between the two scripts. For example:

| Imlaey Script    | Uthmani Script |
|------------------|----------------|
| يَا ابْنَ أُمَّ   | يَبْنَؤُمَّ     |

Subsequently, we developed an algorithm that relies on these annotations to convert Imlaey to Uthmani.

## Annotation Platform

We developed an annotation application to map misaligned words between the Uthmani and Imlaey scripts. The platform consists of two components: a frontend using [Streamlit](https://streamlit.io/) and a backend using [FastAPI](https://fastapi.tiangolo.com/). The core idea is to align words between the Imlaey and Uthmani scripts. We first loop over every ayah in both scripts; if we find a misalignment (where the number of Imlaey words is not equal to the number of Uthmani words), we prompt the user to align the words, as shown in the figure below.

![A screenshot of the UI where the user aligns words for both scripts.](../figures/imlaey-to-uthmani.png)

## Observations

After completing the annotation, we attempted to identify patterns of mismatches between the Imlaey and Uthmani scripts. We found the following patterns, as shown below:

| Imlaey Script | Uthmani Script | (Surah, Ayah) |
|---------------|----------------|---------------|
| يَا ابْنَ أُمَّ | يَبْنَؤُمَّ     | (20, 94)      |
| وَأَن لَّوِ     | وَأَلَّوِ       | (72, 16)      |

Specifically, we found that Imlaey words starting with certain patterns, along with the following word, map to a single Uthmani word.

| Imlaey Word Start | Count in the Holy Quran |
|-------------------|-------------------------|
| يَا               | 350                     |
| وَيَا             | 11                      |
| هَا               | 4                       |

## Imlaey to Uthmani Algorithm

Based on these observations, we created an algorithm that performs a lookup for these patterns to align both scripts. This resulted in the [quran-transcript](https://github.com/obadx/quran-transcript) Python package. With a simple `pip` installation command, the conversion is functional:

```bash
pip install quran-transcript
```

```python
from quran_transcript import search, Aya

imlaey_text = 'فأخرج به من الثمرات رزقا لكم'
results = search(
    imlaey_text,
    start_aya=Aya(2, 13),
    window=20,
    remove_tashkeel=True
)

uthmani_script = results[0].uthmani_script
print(uthmani_script)
# Output: فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًۭا لَّكُمْ
```
