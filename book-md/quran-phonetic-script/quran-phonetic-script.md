## Quran Phonetic Script

The Quran phonetic script is a set of letters and attributes (صفات) that descripes what the Holy Quran's rectiers **exaclly** said. Not only that but it was designed to capture all recitations rules including: all Tajweed rules (excpet Ishmam `إشمام` and puasing with rawm `روم` or `إشمام`) and sifat. This script is composed of 11 levels:

* `phonemes` level: that is designed to capture prounciation letters like baa (ب).
* `sifat` level consisting of 10 levels to catch attribute of articulation (صفة) for every phonemes group. We build this scrit on `Hafs` (رواية حفص) and we gattherd all diffrent ways on reciting for `Hafs` like Moadd Almonfasel length can be (2, 3, 4, 5) an other ways you can check them here [section_hafs_ways]

### Phonemes Level

The phoneme level has somke specific features which is concluded as:

1. **Madd Representation**:  
   - Normal Madd appears as consecutive madd symbols (e.g., 4-beat Madd: اااا)  
   - Madd al-Leen represented with multiple waw/yaa symbols  

2. **Ghonna**:  
   - Stressed Ghunnah (e.g., النون المشددة) as three consecutive noon symbols (ننن)  
   - Ikhfa represented as three consecutive noon_mokhfah (ںںں) or meem_mokhfah (۾۾۾)  

3. **Idgham Handling**:  
   - Assimilation represented by doubling (e.g., مَن يَعْمَلْ → مَنيييَعمَل)  

4. **Special Cases**:  
   - Sakin: No following symbol  
   - Imala: fatha_momala and alif_momala  
   - Rawm: dama_mokhtalasa marker  

# Converted Markdown Table

Here's the LaTeX table converted to Markdown format with the caption placed below the table:

| Uthmani | Phonetic | H/J | S/R | T/T | Itb | Saf | Qal | Tik | Taf | Ist | Gho |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| أَ | ءَ | jahr | shd | mrq | mnf | no | nql | nkr | ntf | nst | nmg |
| تُ | تُ | hams | shd | mrq | mnf | no | nql | nkr | ntf | nst | nmg |
| حَـ | حَ | hams | rkh | mrq | mnf | no | nql | nkr | ntf | nst | nmg |
| ـٰٓ | اااااا | hams | rkh | mrq | mnf | no | nql | nkr | ntf | nst | nmg |
| جُّ | ججُ | jahr | shd | mrq | mnf | no | nql | nkr | ntf | nst | nmg |
| وٓ | ۥۥۥۥۥۥ | jahr | rkh | mrq | mnf | no | nql | nkr | ntf | nst | nmg |
| نِّ | ننننِ | jahr | btw | mrq | mnf | no | nql | nkr | ntf | nst | mg |
| ى | ۦۦ | jahr | rkh | mrq | mnf | no | nql | nkr | ntf | nst | nmg |

Examples of Uthmani to Phonetic Script Conversion with Sifat Attributes: Phonetization of word (أَتُحَٰٓجُّوٓنِّى)
**Attribute Abbreviations:**
- H/J: Hams/Jahr
- S/R: Shidda/Rakhawa
- T/T: Tafkheem/Taqeeq
- Itb: Itbaq
- Saf: Safeer
- Qal: Qalqla
- Tik: Tikraar
- Taf: Tafashie
- Ist: Istitala
- Gho: Ghonna
**Value Abbreviations:**
- shd: shadeed
- rkh: rikhw
- btw: between
- mrq: moraqaq
- mof: mofakham
- mnf: monfateh
- mtb: motbaq
- no: no_safeer
- nql: not_moqalqal
- nkr: not_mokarar
- ntf: not_motafashie
- nst: not_mostateel
- nmg: not_maghnoon
- mg: maghnoon

#### Detailed Phoneme constructoin

We only care about prounced phonemes of letters. If a latter is droped or not proonuced we will drop it for example we droped Wasl Hamza (خمزة الوصل) if it were in betwee: (بِسْمِ اللَّهِ).


##### Disconnceted Letters

Disconnected letters (الحروف المقطعة) are letters that are prounced as a single alphabe one by one example: (الٓمٓ) is prounced (أَلِفْ لَآم مِّيٓمْ). we have 14 forms of theses disconneted letters so we have to disconnet them the way that they are prounced


##### Madd (المد)

we have tree types of elongation (مد):
* Madd Alif (مد ألف): fatha is followed by alif (ا)
* Madd Waw (مد بالواو): dama is followed by waw (و)
* Madd Yaa (مد ياء): kasra is followed by Yaa (ي)

We have diffrent leghtes of the madd given its madd type. so we create special sympol for donating every madd realtive to normal madd (المد الطبيعي) length

* madd Alif is donated by mulitple of alif (ا)
* madd waw is donated by mulitple of small_waw or as dontated `waw_madd` (ۥ)
* madd yaa is donated by mulitple of small_yaa or as dontated `waw_yaa` (ۦ)

###### Normal Madd (المد الطبيعي)

Normal madd is the madd type is prounced as normal without exessive elongation. we dontated it as double of `madd_` phonemes: The exmpale below [table_ex_normal_madd] showes the three types of madd in a sinlge word.

| Uthmani Script | Phonetic Script |
| -- | -- |
| نُوحِيهَا | نُۥۥحِۦۦهَاا |
[table_ex_normal_madd]
The table showes the three types of normal madd: madd alif is (اا), madd yaa is (ۦۦ) and madd waw is (ۥۥ)

##### Madd Small Silah (مد الصلة الصغرى)
Along with Normal madd; Small sila madd (مد الصلة الصغرى) has the same rules for example [table_ex_small_silah]

| Uthmani Script | Phonetic Script |
| -- | -- |
|  إِنَّهُۥ عَلَىٰ رَجْعِهِۦ لَقَادِرٌ| ءِننننَهُۥۥ عَلَاا رَجڇعِهِۦۦ لَقَاادِر |
[table_ex_small_silah]
The table showes small sila madd along with noon moshaddal donated as 3 repeated `noon` (ن) with special qalqla sign: (ڇ)

##### Madd Alewad (مد العوض)
In addition to madd Alewad (مد العوض) as shown in [table_ex_alewad]

| Uthmani Script | Phonetic Script |
| -- | -- |
| قَرِيبًا | قَرِۦۦبَاا |
[table_ex_alewad]
The table showes madd Alewad (مد العوض) same notation as normal madd (المد الطبيعي) for madd alif

##### Madd Alonfasel (مد المنفصل)

For Hafs Moadd Almonfasel can be elonged as 2, 3, 4, and 5 haraka where harak here is donated is half of normal madd if followed by hamaza (ء) not in the same word as shown in the example [table_ex_monfasel]

| Uthmani Script | Phonetic Script |
| -- | -- |
| يَٰٓأَيُّهَا | يَااااءَييُهَاا |
[table_ex_monfasel]
The example showes elongation for madd Alomnfasel with 4 madd alif phonemes along with repeated yaa dontated yaa moshaddada (ياء مشددة) with two yaa: sakin yaa and yaa with harak (damma)

##### Big Silah Madd (مد الصلة الكربى)
Same rule is applied to Big Silah Madd (مد الصلة الكبى). As shown in the example below: [table_ex_big_silah]

| Uthmani Script | Phonetic Script |
| -- | -- |
| مَالَهُۥٓ أَخْلَدَهُۥ | مَاالَهُۥۥۥۥ ءَخلَدَه |
[table_ex_big_silah]
The example showes elongation for big silah madd with 4 madd waw phonemes

##### Madd Almottasel (المد المتصل)

For Hafs Moadd Alottasel (مد المتصل) can be elonged as 2, 3, 4, 5 and (6 at puse only) haraka where harak here is donated is half of normal madd if followed by hamza (ء) in the same word as shown in [table_ex_mottasel]

| Uthmani Script | Phonetic Script |
| -- | -- |
| ٱلسَّمَآءِ مَآءً | ءَسسَمَااااءِ مَااااءَاا |
[table_ex_mottasel]
The example showes elongation for madd Alottasel (مد المتصل) with 4 madd alif phonemes along with madd Alewad (مد العوض) at the puase point

##### Madd Allazim (المد اللازم)

Madd Allazem (مد اللزم) is the madd where madd letter is followed by sakin letter (حرف ساكن) in the same word and elonged with 6 haraka (6 حركات) where haraka here is half of normal madd

| Uthmani Script | Phonetic Script |
| -- | -- |
| ٱلضَّآلِّينَ | ءَضضَااااااللِۦۦۦۦن |
[table_ex_lazem]
The table showes example for madd Allazem () for madd alif elonged with 6 haraka (6 حركات) along with madd Alared (مد العرض للسون) donated with 4 harakt as showen in [table_ex_lazem]


##### Madd Alared for Pause (مد العارض للسكون)

Madd Alaared is the madd that is happend due to puasing after normal madd with a sakin letter . This madd is elonged with 2, 4, and 6 haraka where the haraka is half of normal madd length [table_ex_lazem]

##### Madd Alleen (مد اللين)

Madd Alleen (مد اللين) is the madd that is happend due to puasing after yaa (ي) or waw (و) preceed by fatha and followed with a sakin letter . This madd is elonged with 2, 4, and 6 haraka where the haraka is half of normal madd length [table_ex_leen]. We do not register a special phonemes for this rule as we did we madd becasuse: leen is not just enlongaton for waw (و) or yaa (ي) not a new phonemes.

For 4 haraka madd we dontate this by (num_harka -1) we do that to encounter the case for madd alleen in between like (وَٱلْمَيْسِرِ) not at puase to make the phonetic script consitant. Table [table_ex_leen] showes an exmpale for madd Alleen

| Uthmani Script | Phonetic Script |
| -- | -- |
| لِإِيلَٰفِ قُرَيْشٍ | لِءِۦۦلَاافِ قُرَيييش |
[table_ex_leen]
The exmaple showd two forms of madd the first is normal madd followed by madd Alleen with 4 harakta (evey harak is half normal madd) dontated with 3 yaa (ي)



#### Ghonna

We consider tanween here as harak (fatha or damma or kasra) followed by sakin noon (نون ساكانة) so we do not have to define sperate rules for noon(ن) and tanween 

##### Noon Moshadda (النون المشددة)

We first tried to measure what the reative timimg for sakin noon only (النون اساكنة المظهرة) and compare it to elonged noon (noon with shadda) (نون مشددة) we find that elonged noon is between 3 to 4x sakin noon so we dfindes elonged noon as 3 sakin noon. Example in table: [table_ex_noon_moshadada]


| Uthmani Script | Phonetic Script |
| -- | -- |
|  إِنَّ | ءِننن |
|  شَىْءٍ نُّكُرٍ |  شَيءِننننُكُر |
[table_ex_noon_moshadada]
The table shows how ghonna disaasemply of noon with shadda (نون مشددة) represeted as 3 repeated noon (ن)

##### Meem Moshadda (الميم المشددة)

As we have done with noon moshadda we make it also for meem moshadda (elonged meem) we fonud the same result noon moshaddal is between 3 to 4x sakin meem (مييم مظهرة). We dontated meem moshadda as 3 repeate meem as shown in the example: [table_ex_meem_moshadda]

| Uthmani Script | Phonetic Script |
| -- | -- |
|  أَمَّا | ءَممممَاا |
|  خَيْرٍ مِّن |  خَيرِممممِن |
[table_ex_meem_moshadda]
The table shows how ghonna disaasemply of meem with shadda (نون مشددة) represeted as 3 repeated meem (م)

##### Ikhfaa for Noon (إخفاؤ النون الساكنة)

Ikhfat for sakin noon (إخفاء النون الساكنة) happens when sakin noon (نون ساكنة) for tanween followed by Ikhfaa letters: (ص - ف - ذ - ث - ك - ج - ش - ق - س - د - ط - ز - ت - ض - ظ). we donated this by replacing noon with three `noon_mokhfaa` sympol (ں) as shown in the example [table_ex_noon_mokhfaa]

| Uthmani Script | Phonetic Script |
| -- | -- |
|  مِن صَلْصَٰلٍ | مِںںںصَلصَاااال |
[table_ex_noon_mokhfaa]
Table showes represntation of noon mokhfaa (نون مخفاة) as three dotless noon (ں)



##### Idgham for noon with yaa and waw (إدغام النون الساكنة مع الياء والواو)

The Idgham rule is defined as prouncation two consecative letters as the second letter with shadda or stressed according to Ibn Aljazary [ibnaljazri_alnashr] so we simply delete noon (ن) and replace it with yaa (ي) or waw (و).

As we did with Noon moshadda and meem moshadda we weill preate the yaa and waw two time not three why? to make our phonetic script constant with madd Alleen and for stressed (مشدد) yaa or waw (represnted by sakin and motaharek (متحرك)). The table [table_ex_idghaam_yaa_with_noon] shoes examples of diffrent forms of yaa.


| Uthmani Script | Phonetic Script |
| -- | -- |
|  مَن يَعْمَلْ | مَيييَعمَل |
| ٱلْحَىِّ | ءَلحَيي |
| قُرَيْشٍ | قُرَيييش |
[table_ex_idghaam_yaa_with_noon]
Theis tables demonsrates how representing yaa in diffrent forms. The first row showes how idgham yaa with sakin noon (النون الساكنة) represented by replacing noon by two yaa. The second raw showed yaa with shadda at pause with two yaa. The last raw showes with madd Aleen with 4 harak represented by 3 yaa


##### Ikhfaa for Meem

Ikhfaa sakin meem (إخفاء الميم الساكنة) is defined as sakin meem  (ميم ساكنة) is followed by baa (ب) or when sakin noon or tanween is followed by defined in Tajweed Literature as Iqlab (إقلاب) we represented that as three `meem_mokhfah` (۾). Table [table_ex_ikhfaa_meem] showes how this rule is abbplied

| Uthmani Script | Phonetic Script |
| -- | -- |
| مِنۢ بَعْدِ | مِ۾۾۾بَعدڇ |
| تَرْمِيهِم بِحِجَارَةٍ | تَرمِۦۦهِ۾۾۾بِحِجَاارَه |
[table_ex_idghaam_yaa_with_noon]
The first raw reprents Iqlab rule (الإقلاب) which is dontated by replacing noon with 3 `meem_mokhfah` (۾). The seconds raw showes rule of Ikhfaa sakin meem with baa (إخفاء الميم الساكنة) represented by  3 `meem_mokhfah` (۾)


#### Idgham (الإدغام)

We have two type of merging (Idgham) in Arabic (إدغام):

* Full Merging (إدغام كامل): when two letters follow each other and prounced as the second only but stressed. Example (قَد تَّبَيَّنَ) is prounced as (قَتتَبَييَن) the letter daal is completly not prounced.
* Partial Merging (إدغام ناقص). when two letter follow eatch other and the Ariculation of the first letter is gone but the attriubtes remains. Example: (بَسَطتَ) is prounced as the same (بَسَطت)

#### Saken Letter (الحرف الساكن)

Sakin letter is represented in uthmani script by three forms:

* letter followed by ras haa (رأس حاء): 'ْ'
* letter with shadda (shadda) in Egnlish called stress. The letter is composed fo two letters the first is saken and the second is with haraka (fatha or damma or kasra). Example (بَّ) -> (ببَ)
* Letter that is not followed by any haraka (short vowel) or  any special sympol. happens in Idhgam and with madd letters.

We donate sakin letter by not precceding it by any type of diacritization


#### Puasing (وقف)

At pause (وقف) we make the last letter as sakin (ساكن) by removing any diacritization sympols. See any exmaples like: [table_ex_idghaam_yaa_with_noon] and [table_ex_idghaam_yaa_with_noon]

#### Wasl Hamza (همزة الوصل)

Hazat Al wasel (همزة الوصل) (ٱ) is defined in Tajweed as: the hmza is added to avoid beginning with sakin letter [sweed2021]. It elminated in between recitations and remains at the beginning only.

Hamzat Alwasl can followed by (fatah, damma or kasra) depending on the type of the word:

* For nouns begining with Al Al taareef (ال التعريف) hamza is followed by fatha. 
* For Proper nouns: hamza is followed by kasra.
* For verbs: if the third letter is:
    - damma: the hamza if followed by damma
    - fatha, kasra or transient damma: hamaza is followed by kasra

We mean here by **transient damma* a damma that is not oiginally damma but it weas converted to damma as a transniet state. Example word (ٱمْشُوا۟) the third letter has damma but the verb originated from (ٱمْشِ) where the third letter (ش) has kasra.


| Uthmani Script | Phonetic Script | Word Type | Hamzat Wasl Haraka | 
| -- | -- | -- | -- |
| ٱلْكِتَٰبُ | ءَلكِتَاااابڇ | Proper Noun begins with (ال) | fatha |
| ٱللَّهِ | ءَللَااااه | Proper Noun begins with (ال) | fatha |
| ٱسْتِكْبَارًۭا | ءِستِكبَاارَاا | Proper Noun  | kasra |
| ٱرْكَب | ءِركَبڇ | verb and third letter has fatha  | kasra |
| ٱصْبِرْ | ءِصبِر | verb and third letter has kasra  | kasra |
| ٱصْبِرْ | ءِصبِر | verb and third letter has kasra  | kasra |
| ٱمْشُوا۟ | ءِمشُۥۥ | verb and third letter has transient damma  | kasra |
| ٱرْكُضْ | ءُركُض | verb and third letter has non-transient damma  | damma |
[table_ex_hamzat_wasl]
This table showd diffrent forms of beginning with hamzat wasl (ٱ). The fist and second rows deomstrate begining with hamza followed by fatha becuase of (ال) for tareef. the third row show begining with hamza followed by kasra because fof proper nound. The 4th, 5th, and 6th raws showd begining a verb with hamza followd by kasra becuase the third character has fatha, kasra, or transient damma. The last raw showe begining with hamza followed by damma because the third letter is damma.


**Important Note**: we rely on determinig the type for word either name, verb or noun on Dukes's work [dukes2010morphological] where he dfined words types including Nouns, verbs and propositons. If this work does not exist we will spend at least a year annoting the Holy Quran words whcin outlines the importance of open-source research.

##### Meeting two hzzma the last is consonent (اقتاء همزتان والثانية منهما ساكنة)

After converting hamzat wasl to hamza. Some cases happen where two hamza meets and the seond is akin or consnont. The last one is converted to madd matching the harak of the firt hamza [sweed2021]. Table [table_ex_meeting_two_hamza]

| Uthmani Script | Converting Hamzat Wasl | Final Conversion |
| -- | -- | -- |
|ٱؤْتُمِنَ | ءُءْتُمِن  | ءُۥۥتُمِن |
|ٱئْتُونِى | ءِءْتُۥۥنِۦۦ | ءِۦۦتُۥۥنِۦۦ |
[table_ex_meeting_two_hamza]
The table shows the conversion for a verrb tha has two connected hamza at the begiing. The firt statage is converting Hamzat wasl to hamza followd by kasra or damma and the later stage to convert the second hamza to waw_madd or yaa_madd depending on the harka of the firt hamza. We remintd you that we reprent normal madd by two (اا), (ۦۦ), or (ۥۥ) for madd_alif, madd_yaa and madd waw respectilvy.


#### Meeting two consents (التقاء الساكنان)

In Arabic Language and the Holy Quran: two consent letter (الحرفان الساكنان) do not meet execpt for pause (وقف) like pausing on word (ٱلْأَرْضِ) no problem as the last two letter are sakin. To avoid this three ways can be made:

* Eliminate the first letter
* Elongation of the 
* Make the second letter diarctized with (fatha, damma or kasra)

The Muslim scholars have make our task simpler by nearly annotating this rule entilry in the Uthmani script excpet for:
* The first letter is (alif, waw, or yaa): for this we elminate the fisrt letter
* The first letter is tanween: for this we convert tanween to noon (ن) followed by kasra

Table [table_ex_two_saken] showes how we apply this rule to our phonetizer.

| Uthmani Script | Phonetic Script |
| -- | -- |
| وَقَالَا ٱلْحَمْدُ | وَقَاالَ لحَمدڇ |
| نُوحٌ ٱبْنَهُۥ| نُۥۥحُنِ بڇنَه|
[table_ex_two_saken]
The talbe showes how we reslove meeting of two consents. Firt row showes meeting alif (ا) for word (قالا) with lam (ل) of word (ٱلْحَمْدُ ). In the resulting phonetic script the alif was deleted. But note that normal madd in (قالال) is represented by two alif and qalqal in letter daal (د) is reprented by (ڇ). The second eample showed meeting tanween of (نُوحٌ) with sakin baa (ب) of word (ٱبْنَهُۥ) reselting in converting tanween to noon with kasra. And do not forget that we donate normal madd waw with two (ۥ) and qalqal for baa (ب) with (ڇ).


#### Shadda (التشديد)

Shadda (ّ) donates that the letter is duplicated, so we replace shadda by repeating the letter twice as show in [table_ex_tasheel]


#### Puasing (الوقف)

At pause (وقف) many rules are applied:

* Haraka i.e (fatha, damma, kasra) is elminated meaning making the last letter sakin (ساكن).
* Small Silah Madd is elminated.
* Taa marboota (ة) is converted to haa (ه)



#### Qqlqal (القلقة)

Qalala (قلقة) is defined in tajweed as: "a small sound is followed by on one the letter (ق - ط - ب - ج - د) if one of them is sakin (ساكن) either in between words (وصلا) or on pause (وقفا)"[AlHamad2008]. We dontate this small sound as (ڇ) like in table [table_ex_two_saken].


#### Imala (الإمالة)

Imala (إمالة) is defined in Tajweed as "prouncing fatha between fatha and kasra and alif between alif and yaa"[sweed2021]. We dontate fatha with imala as `fatha_momala` '۪' and alif with imala by two `alif_momala` (ـ) similar to Normal Madd. Table [table_ex_imala]

| Uthmani Script | Phonetic Script |
| -- | -- |
| مَجْر۪ىٰهَا | مَجڇر۪ــهَاا |
[table_ex_imala]
The table showes how we repreent fatha with imala as '۪' and alif with imala as (ـ) and letter jeem (ج) has qalqla donated by (ڇ).

#### Tasheel (التسهيل)

Tasheel is defined in tajweed as "prouncing hamza (ء) between hzma and the next madd letter similar to haraka (حرمة) i.e:  fatha, dama, kasra "[sweed2021]. We dontated this hamza by `hama_mosaha` (ٲ). Table: [table_ex_tasheel]


| Uthmani Script | Phonetic Script |
| -- | -- |
| ءَا۬عْجَمِىٌّ | ءَٲعجَمِيي |
[table_ex_tasheel]
The table showes hamza with tasheel dontated (). along with diassimple of letter yaa (ي) with shadda (ّ) to two yaa.



#### Sakt (السكت)

Sakt is defined in tajweed by "cutting voice without releasing of breathe for short period learned from expert reciters"[AlHamad2008]. Sakat happens in a specified posisions see: [section_hafs_ways]. we dontate sakt by `sakt` 'ۜ'.


#### Implementation

We implemented our phonetic representation by applying 26 operation. Every operation is a single or multiple of reqular expersion as shown in: [section_phonemes_operations]

| Operation Name           | Arabic Name              | Corrected Description                                                                 |
|--------------------------|--------------------------|----------------------------------------------------------------------------------------|
| DisassembleHrofMoqatta | تفكيك حروف مقطعة      | Separates Quranic initials (e.g., الم، الر) into individual letters.                   |
| SpecialCases           | حالات خاصة             | Handles special words like (يبسط) that have different pronunciation forms defined in `MoshafAttributes` |
| BeginWithHamzatWasl    | البدء بهمزة الوصل     | Processes words starting with connecting hamza (ٱ) and converts it to hamza (ء) with appropriate harakah for nouns and verbs |
| BeginWithSaken         | البدء بساكن            | Manages words beginning with a consonant (sakin) like (لْيَقْطَعْ), as Arabic doesn't start utterances with consonants |
| ConvertAlifMaksora     | تحويل الألف المقصورة  | Converts (ى) in Uthmani script to either yaa (ي) or alif (ا) based on context          |
| NormalizeHmazat        | توحيد الهمزات         | Standardizes hamza forms (أ إ ؤ ئ) to (ء)                                             |
| IthbatYaaYohie         | إثبات ياء يحيى        | Handles words like (يُحْىِۦ) where two yaa letters occur - resolves conflicts when pausing on words with consecutive consonants (التقاء الساكنين) by adding another yaa at end. |
| RemoveKasheeda         | إزالة الكشيدة         | Deletes elongation marks (ـــ) from text                                              |
| RemoveHmzatWaslMiddle  | إزالة همزة الوصل الوسطية | Removes connecting hamza (ٱ) in non-initial positions                                  |
| RemoveSkoonMostadeer   | حذف الحرف الذي فوقع سكون مستدير | Eliminates letters with circular sukoon diacritics like alif in (جَمَعُوا۟)          |
| SkoonMostateel         | سكون مستطيل            | Removes alif with elongated sukoon mid-word and adds it at the end during pauses (وقف) |
| MaddAlewad             | مد العوض               | Removes alif after tanween fatha mid-word and adds alif while removing tanween at pause positions (وقف) |
| WawAlsalah             | واو الصلاة            | Replaces letter waw (و) with small alif above combined with alif                       |
| EnlargeSmallLetters    | تكبير الحروف الصغيرة  | Resizes miniature Arabic letters to standard proportions                              |
| CleanEnd               | تنظيف النهاية         | Removes redundant diacritics and spaces at word endings                               |
| NormalizeTaa           | توحيد التاء            | Converts ة (taa marbuta) to ت or ه based on context, and converts final ة to haa (ه) |
| AddAlifIsmAllah        | إضافة ألف اسم الله    | Inserts compensatory alif in derivatives of "الله"                                    |
| PrepareGhonnaIdghamIqlab | تهيئة الغنة والإدغام والإقلاب | Preprocesses text for nasalization, assimilation, and conversion rules             |
| IltiqaaAlsaknan        | التقاء الساكنين       | Resolves consecutive consonants by inserting vowels                                 |
| DeleteShaddaAtBeginning| حذف الشدة في البداية  | Removes shadda (ّ) from word-initial letters                                        |
| Ghonna                 | غنة                   | Applies nasalization during pronunciation of sakin noon and tanween                  |
| Tasheel                | تسهيل                 | Adds a letter representing alif with tasheel easing                                  |
| Imala                  | إمالة                 | Converts fatha with imala to `fatha_momala` phoneme and alif with imala to `alif_momala` phoneme |
| Madd                   | مد                    | Adds madd symbols for all madd types, inserting `madd_alif` (ا), `madd_waw` (ۥ), and `madd_yaa` (ۦ) |
| Qalqla                 | قلقة                  | Adds echoing effect to ق, ط, ب, ج, د letters with sukoon                           |
| RemoveRasHaaAndShadda  | إزالة رأس الحاء علامة السكون | Deletes sukoon diacritic marks                                                   |
### Sifat Level

Sifa (صفة) or in English as: attribute of articulation. We relied on Ibn Aljzazry to define sifat. Ibn Aljazary mentioned 17 sifa [AlJazariyyahSwaid]. We exculded 4 sifat:

* Ismat (إصمات): is a phonlogical not photenic.
* Ithlaq (إذلاق): is phonological not phontenic.
* Leen (اللين): is already exists in Madd Alleen (مد اللين).
* Inheraf (الإنحارف): is explaing why letter lam (ل) and raa (ر) are between shidda (شدة) and rakhawa (رخاوة)

We included Alghonna sifa (صفة الغنة), so we are representing 14 sifa organized in 10 levels as follows in table [table_sifa_level_def].


- **Hams/Jahr** (الهمس/الجهر)  
  - *Hams*: Whispered letters requiring breath flow ( ف ح ث ه ش خ ص س ك ت)  
  - *Jahr*: Voiced letters with full the rest of letters

- **Shidda/Rakhawa** (الشدة/الرخاوة)  
  - *Shidda*: Complete interruption of sound ( ء ج د ق ط ب ك ت)  
  - *Between Shiddah and Rqkahwa*: in between of both ( ل ن ع م ر)  
  - *Rakhawa*: Continuous airflow the rest of letter.

- **Tafkheem/Taqeeq** (التفخيم/الترقيق)  
  - *Tafkheem*: Heavy/thickened pronunciation ( خ ص ض ط ظ غ ق)  
  - *Taqeeq*: Light/thin pronunciation rest of letter with exepsion descripted below

- **Itbaq** (الإطباق)  
  - *Motbaq* Letters pronounced with tongue-to-palate contact ( ص ض ط ظ)
  - *Monfateh* Rest of the letters

- **Safeer** (الصفير)  
  - *Safeer* Whistling sound in س ص ز
  - *No Safeer* the rest of the letters

- **Qalqala** (القلقلة)  
  - *Moqlqal* Echo effect on ق ط ب ج د when bearing sukoon
  - *Not Moqlqal* the rest of letters

- **Tikraar** (التكرار)  
  - *Mokarrar* the Quranic letter (ر) is trilled just (like Spanish perro)
  - *Not Mokarrar* the rest of letters

- **Tafashie** (التفشي)  
  - *Motafashie* Sound dispersion characteristic of ش
  - *Not Motafashie* Rest of letters

- **Istitala** (الاستطالة)  
  - *Mostateel* sepecial attribute emphatic and pharyngealized for letter (ض)
  - *Not Mostateel* Rest of letters

- **Ghonna** (الغنة)  
  - *Maghnoon* Nasalization in ن and م
  - *Not Maghnoon* The other letters



Our methodology of trancripting sifat is we first chunk phonemes by grouping similar groups of phonemes and then extract sif for every phoneme group. like in example [table_example_with_sifat]. After that we extract sifa for every gropu.

Th extraction of sifa is straigh forwad expect for Tafkheem and Tarqeeq.

#### Tafkheem and Tarqeeq (التفخيم والترقيق)

Tafkheem (التفخيم) "is thickening that affects phoneme makeing it fill the whole mouse"[sweed2021]

In Tajweed we have 6 levels of tafkheem and Tarqeeq. sorted from most mofakham (strgest) to moraqaq (weakest)

1. mofakham followed by fatha then madd alif.
2. Mofkaham followed by fatha not madd alif.
3. Mofaam folowed by damma.
4. Mofakham is sakin (ساكان).
5. Mofakham followed by kasra.
6. Moraqaq.

we forumulated them by only three labels:

1. `mofakham` to cover casses form 1 to 4.
2. `moraqaq` to cover case 6
3. `low_mofakham` to cover case 5 for letter (غ - خ - ق) which are letters an monfateh (منفتح) not motbaq (مطبق). These letter are gettin weakend by kasra unlike motbaq letters lik (ص - ض- ط - ظ)


Some phonemes are cases whare they are moraqaq and otther are mofakham:

* `madd_alif` (ا): which follows it preceding phonemes in Tarqeeq and Tafkheem.
* `noon_mokhfah` (ں): followes the phonemes following it Tafkheem and Tarqeeq.
* `raa` (ر) is morqaq in the following cases:
    - `raa` (ر) followed by kasra.
    - `raa` is preeceed by yaa (ياء)
    - `raa` (ر) is sakin (ساكن) and preeced by a mostafel (مستفل) phonemes that has kasra and `raa` is not follwed by mostaalie (مستعلي) phoneme.
    - `raa` (ر) cames after hamzat wasl (ٱ)

**Note**: Mostaalie (حروف الاستعلاء) letters are (خ - ص - ض - غ - ط - ق - ظ) and Mostafel (مستفل) letters are the rest



