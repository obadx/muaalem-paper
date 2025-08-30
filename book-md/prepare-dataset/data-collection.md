## Collection of Expert Recitations

Recitations were collected from 22 world-class reciters, amounting to a total of **893 hours** of audio before filtering. The collection process prioritized premium audio quality.

![Statistics of the collected database](../figures/stats.png)
*Figure 1: Overview statistics of the collected audio database.*

![Breakdown of collected hours per reciter](./figures/reciter.png)
*Figure 2: Total duration of collected recitations, broken down by individual reciter.*

To facilitate this collection, a web GUI was developed using [Streamlit](https://streamlit.io/). This application performs the following tasks:
*   Downloads audio tracks and extracts their metadata.
*   Organizes the data by Moshaf, with each chapter saved as a separate file (e.g., `001.mp3`).
*   Provides an interface for annotating Moshaf attribute cards.

### Running the Collection Application

#### Cloning the Repository
The application source code can be obtained by cloning the Git repository:
```bash
git clone https://github.com/obadx/prepare-quran-dataset
```

#### Installing `uv`
The project uses `uv` for dependency management. It can be installed via `pip`:
```bash
pip install uv
```
Alternatively, it can be installed directly from the official installer:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Installing Project Dependencies
Navigate to the project directory and sync the dependencies, including those for annotation:
```bash
cd prepare-quran-dataset
uv sync --extra annotate
```

#### Installing Frontend Dependencies
The frontend has additional requirements. Navigate to its directory and install them:
```bash
cd frontend
uv pip install -r requirements.txt
```

#### Launching the Frontend Application
With dependencies installed, the Streamlit application can be launched from the `frontend` directory:
```bash
streamlit run streamlit_app.py
```

### UI Snapshots

![Main interface of the annotation platform](../figures/ui_main_page.png)
*Figure 3: The main page of the custom annotation platform.*

![Interface for viewing and managing reciters](../figures/ui_veiw_reciters.png)
*Figure 4: The reciter management view within the application.*

![Interface for browsing all collected Masahif](../figures/ui_veiw_all_moshaf.png)
*Figure 5: View displaying all available Masahif in the database.*

![Form for adding a new reciter to the database](../figures/ui_insert_new_reciter.png)
*Figure 6: Dialog for inserting a new reciter's details.*

![Form for adding a new Moshaf card](../figures/ui_inset_new_mohaf.png)
*Figure 7: Dialog for creating and annotating a new Moshaf attribute card.*

![Interface for viewing and playing recitation tracks](../figures/ui_play_recitatins.png)
*Figure 8: Interface for viewing a Moshaf's tracks and playing individual recitations.*
