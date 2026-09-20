# data2005-team-project
 [Energy and Utilities] - DATA 2005 Team Project

## Team Members

| Name | Role | GitHub |
|------|------|--------|
| [Richard Taiwo] | Data Engineer | [@richytaiwo] |
| [Rory Maher] | Data Analyst | [@rmtudublin] |
| [Richard Taiwo] | Visualization Lead | [] |
| [Richard Taiwo] | Documentation Lead | [@richytaiwo] |

## Project Description

The goal of this assignment is to create a thorough pipeline for analysing large datasets of time series energy data using Python. We created this pipeline to show our skills in preprocessing data, resampling, taking in data, statistical analysis and creating visualisations that we have learned throughout the semester.
The dataset we used in this assignment contains household electrical power consumption data at high speed, showing real energy usage over a long time, making it perfect for our time series analysis.
## Dataset

- **Name:** [household_power_consumption]
- **Source:** [https://www.kaggle.com/datasets/shivsaar/dataset)]
- **Size:** [261,000 rows]
- **Format:** CSV

## Project Structure
data2005-team-project/
├── data/
│   ├── raw/              # Original dataset files
│   │   └── .gitkeep
│   └── processed/        # Cleaned data
│       └── .gitkeep
├── src/
│   ├── __init__.py
│   ├── data_loading.py   # Data Engineer
│   ├── preprocessing.py  # Data Engineer
│   ├── analysis.py       # Data Analyst
│   └── visualization.py  # Visualization Lead
├── notebooks/
│   └── exploration.ipynb # Exploratory analysis
├── outputs/
│   ├── figures/          # Generated plots
│   │   └── .gitkeep
│   └── reports/          # Exported results
│       └── .gitkeep
├── tests/                # Unit tests (optional)
├── requirements.txt      # Dependencies
├── README.md             # Documentation
└── .gitignore            # Git ignore rules


## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/[richytaiwo]/data2005-team-project.git
   cd data2005-team-project

2. Create virtual environment:

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
    pip install -r requirements.txt
