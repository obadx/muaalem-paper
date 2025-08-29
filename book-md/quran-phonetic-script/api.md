# 📖 Quran Transcript API

We have created a python packge [quran-transcript](https://github.com/obadx/quran-transcript) representing the Quran Phonetic Script.

## 🔧 Installation

Install the package directly from GitHub using pip:

```bash
pip install quran-transcript
```

## 🧠 Usage Examples

### 🕋 Aya Object

Create an Aya object to represent a specific verse and retrieve its information

```python
from quran_transcript import Aya

aya = Aya(1, 1)  # Surah Al-Fatiha, Verse 1
print(aya)

aya_info = aya.get()
print(aya_info)
```

```bash
AyaFormat(sura_idx=1, aya_idx=1, sura_name='الفاتحة', num_ayat_in_sura=7, uthmani='بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ', uthmani_words=['بِسْمِ', 'ٱللَّهِ', 'ٱلرَّحْمَـٰنِ', 'ٱلرَّحِيمِ'], imlaey_words=['بِسْمِ', 'اللَّهِ', 'الرَّحْمَٰنِ', 'الرَّحِيمِ'], imlaey='بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ', istiaatha_uthmani='أَعُوذُ بِٱللَّهِ مِنَ ٱلشَّيْطَانِ ٱلرَّجِيمِ', istiaatha_imlaey='أَعُوذُ بِاللَّهِ مِنَ الشَّيْطَانِ الرَّجِيمِ', rasm_map=None, bismillah_uthmani=None, bismillah_imlaey=None, bismillah_map=None)
AyaFormat(sura_idx=1, aya_idx=1, sura_name='الفاتحة', num_ayat_in_sura=7, uthmani='بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ', uthmani_words=['بِسْمِ', 'ٱللَّهِ', 'ٱلرَّحْمَـٰنِ', 'ٱلرَّحِيمِ'], imlaey_words=['بِسْمِ', 'اللَّهِ', 'الرَّحْمَٰنِ', 'الرَّحِيمِ'], imlaey='بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ', istiaatha_uthmani='أَعُوذُ بِٱللَّهِ مِنَ ٱلشَّيْطَانِ ٱلرَّجِيمِ', istiaatha_imlaey='أَعُوذُ بِاللَّهِ مِنَ الشَّيْطَانِ الرَّجِيمِ', rasm_map=None, bismillah_uthmani=None, bismillah_imlaey=None, bismillah_map=None)
```

### 🔁 Loop Through All Surahs

Iterate through all verses in the Quran

```python
start_aya = Aya()
for aya in start_aya.get_ayat_after():
    aya_info = aya.get()
    # Do something with the aya info
```

### 🧮 Get Number of Verses per Surah

Build a map of surah numbers and their verse counts

```python
sura_to_aya_count = {}
start_aya = Aya(1, 1)

for i in range(1, 115):  # 114 surahs in the Quran
    aya.set(i, 1)
    sura_to_aya_count[i] = aya.get().num_ayat_in_sura

print(sura_to_aya_count)
```

```bash
فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًۭا لَّكُمْ
```

### 🔄 Convert Imlaey Script to Uthmani

Convert Imlaey script to Uthmani script

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
```

### 🔤 Convert Uthmani Script to Phonetic Script

Convert Uthmani script to Quranic phonetic script

```python
from quran_transcript import Aya, search, quran_phonetizer, MoshafAttributes
import json

imlaey_text = "بسم الله الرحمن الرحيم"
results = search(
    imlaey_text,
    start_aya=Aya(1, 1),
    window=2,
    remove_tashkeel=True
)

uthmani_script = results[0].uthmani_script
print(f"Uthmani Script:\n{uthmani_script}")

# Specify Mushaf attributes for phonetic conversion
moshaf = MoshafAttributes(
    rewaya="hafs",
    madd_monfasel_len=4,
    madd_mottasel_len=4,
    madd_mottasel_waqf=4,
    madd_aared_len=4,
)

phonetic_script = quran_phonetizer(uthmani_script, moshaf)

print('\n' * 2)
print(f"Phonetic Script:\n{phonetic_script.phonemes}")
print('\n' * 2)
print("Letter Attributes:")
for sifa in phonetic_script.sifat:
    print(json.dumps(sifa.model_dump(), ensure_ascii=False, indent=4))
    print()
```

```bash

الرسم العثماني:
أَتُحَـٰٓجُّوٓنِّى



الرسم الصوتي:
ءَتُحَااااااججُۥۥۥۥۥۥننننِۦۦ



صفات الحروف:
{
    "phonemes": "ءَ",
    "hams_or_jahr": "jahr",
    "shidda_or_rakhawa": "shadeed",
    "tafkheem_or_taqeeq": "moraqaq",
    "itbaq": "monfateh",
    "safeer": "no_safeer",
    "qalqla": "not_moqalqal",
    "tikraar": "not_mokarar",
    "tafashie": "not_motafashie",
    "istitala": "not_mostateel",
    "ghonna": "not_maghnoon"
}

{
    "phonemes": "تُ",
    "hams_or_jahr": "hams",
    "shidda_or_rakhawa": "shadeed",
    "tafkheem_or_taqeeq": "moraqaq",
    "itbaq": "monfateh",
    "safeer": "no_safeer",
    "qalqla": "not_moqalqal",
    "tikraar": "not_mokarar",
    "tafashie": "not_motafashie",
    "istitala": "not_mostateel",
    "ghonna": "not_maghnoon"
}

{
    "phonemes": "حَ",
    "hams_or_jahr": "hams",
    "shidda_or_rakhawa": "rikhw",
    "tafkheem_or_taqeeq": "moraqaq",
    "itbaq": "monfateh",
    "safeer": "no_safeer",
    "qalqla": "not_moqalqal",
    "tikraar": "not_mokarar",
    "tafashie": "not_motafashie",
    "istitala": "not_mostateel",
    "ghonna": "not_maghnoon"
}

{
    "phonemes": "اااااا",
    "hams_or_jahr": "jahr",
    "shidda_or_rakhawa": "rikhw",
    "tafkheem_or_taqeeq": "moraqaq",
    "itbaq": "monfateh",
    "safeer": "no_safeer",
    "qalqla": "not_moqalqal",
    "tikraar": "not_mokarar",
    "tafashie": "not_motafashie",
    "istitala": "not_mostateel",
    "ghonna": "not_maghnoon"
}

{
    "phonemes": "ججُ",
    "hams_or_jahr": "jahr",
    "shidda_or_rakhawa": "shadeed",
    "tafkheem_or_taqeeq": "moraqaq",
    "itbaq": "monfateh",
    "safeer": "no_safeer",
    "qalqla": "not_moqalqal",
    "tikraar": "not_mokarar",
    "tafashie": "not_motafashie",
    "istitala": "not_mostateel",
    "ghonna": "not_maghnoon"
}

{
    "phonemes": "ۥۥۥۥۥۥ",
    "hams_or_jahr": "jahr",
    "shidda_or_rakhawa": "rikhw",
    "tafkheem_or_taqeeq": "moraqaq",
    "itbaq": "monfateh",
    "safeer": "no_safeer",
    "qalqla": "not_moqalqal",
    "tikraar": "not_mokarar",
    "tafashie": "not_motafashie",
    "istitala": "not_mostateel",
    "ghonna": "not_maghnoon"
}

{
    "phonemes": "ننننِ",
    "hams_or_jahr": "jahr",
    "shidda_or_rakhawa": "between",
    "tafkheem_or_taqeeq": "moraqaq",
    "itbaq": "monfateh",
    "safeer": "no_safeer",
    "qalqla": "not_moqalqal",
    "tikraar": "not_mokarar",
    "tafashie": "not_motafashie",
    "istitala": "not_mostateel",
    "ghonna": "maghnoon"
}

{
    "phonemes": "ۦۦ",
    "hams_or_jahr": "jahr",
    "shidda_or_rakhawa": "rikhw",
    "tafkheem_or_taqeeq": "moraqaq",
    "itbaq": "monfateh",
    "safeer": "no_safeer",
    "qalqla": "not_moqalqal",
    "tikraar": "not_mokarar",
    "tafashie": "not_motafashie",
    "istitala": "not_mostateel",
    "ghonna": "not_maghnoon"
}
```


> 📘 For more information on `MoshafAttributes`, refer to the [Quran Dataset Documentation](https://github.com/obadx/prepare-quran-dataset?tab=readme-ov-file#moshaf-attributes-docs).
