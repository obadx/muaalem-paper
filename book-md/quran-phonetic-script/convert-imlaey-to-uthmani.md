# Convert Imlaey to Uthmani

As we mentioned we selected Uthmani script as our foundation because:  
   - Contains specialized Tajweed diacritics (Madd, Tasheel, etc.)  
   - Preserves pause rules critical for recitation (e.g., stopping on رحمت)  

In order to do that, we created an annotation UI to manually annotate misaligned words in both scripts. For example,

| Imlaey Script | Uthmani Script |
| -- | -- |
| يَا ابْنَ أُمَّ| يَبْنَؤُمَّ|

after that, we developed an algorithm that relies on the annotations to convert Imlaey to Uthmani. 


## Annotation Platfrom

We have developed an annotation application to annotate mapping form misaligned words between Uthmani and Imlaey scripts. The platform has two components. Frontend using [streamlit](https://streamlit.io/) and a backend using [fastapi](https://fastapi.tiangolo.com/). The core idea is to rying to aligh words between Imlaey and Uthmani script. We first we loop over every aya for both scripts then if we find misalighmens (number of Imlaey words is not equal to number of Utmani words) we prompt the user to align worrs as show in the figure below.


![The figure below shows a screenshot of the UI where the user tries to align words for both scripts.](../figures/imlaey-to-uthmani.png)


## Observation

After we have done annotation we tried to identfy patterns of mismaaches between Imleay and Uthmani scripts. we found the following patters as shown below

| Imlaey Script | Uthmani Script | (Sura, Aya) |
| -- | -- | -- |
| يَا ابْنَ أُمَّ| يَبْنَؤُمَّ| (20, 94) |
|  وَأَن لَّوِ| وَأَلَّوِ | (72, 16) |

and Imlaey words that starts with these patterns along with the second words maps to single Uthmai word

| Imlaey Word Start | counts in the Holy Quran | 
| -- | -- |
| يَا | 350 |
| وَيَا| 11 |
| هَا| 4 |

## Imlaey to Uthmani Algorithm

Based on the observation we created an algorithm by simply looking up to these patterns to align both script resulting producing [quran-transcript](https://github.com/obadx/quran-transcript) python package. With a simple `pip` instalation command we can conversion working:

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
# فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًۭا لَّكُمْ
```

