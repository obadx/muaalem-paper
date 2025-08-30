## Collect Expert Recitations  

We collected recitations from 22 world-class reciters with premium audio quality, totaling **893 hours** pre-filtering.  

![Database Collection Statistics](../figures/stats.png)  
![Reciters Statistics: Total collected hours of recitation for every rectiter](./figures/reciter.png)  

We developed a web GUI using [Streamlit](https://streamlit.io/) that:  

* Downloads and extracts metadata for each track  
* Organizes data by Moshaf (each chapter as "001.mp3")  
* Annotates Moshaf attributes card


### Running the collection App

#### Clone the repo

```bash
git clone https://github.com/obadx/prepare-quran-dataset
```


### Install `uv`

```bash
pip install uv
```
Or
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Install dependencies

```
cd prepare-quran-dataset
```

```bash
uv sync  --extra annotate
```


#### Install Frontend dpendencies

```bash
cd frontend
```

```bash
uv pip -r install requirements.txt
```

#### Run the frontend

```bash
streamlit run streamlit_app.py
```


### UI Snaphots

![Annotation Platorm main Page](../figures/ui_main_page.png)

![Viewing Reciters Page](../figures/ui_veiw_reciters.png)

![Viewing All moshaf](../figures/ui_veiw_all_moshaf.png)

![Inserting a Rectier](../figures/ui_insert_new_reciter.png)

![Inserting new Moshaf Card](../figures/ui_inset_new_mohaf.png)

![View Moshaf tracks](../figures/ui_play_recitatins.png)




