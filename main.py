import os
from src.config import raw_csv_file, time_categories, project_root
from src.data_loading import load_dataset
from src.preprocessing import clean_and_prepare_data
from src.analysis import resample_energy, calculate_summary, zscore_normalise
from src.visualisations import plot_hourly

def run_pipeline():
    print("starting pipeline...")
    
    # load data
    df = load_dataset(raw_csv_file)
    if df is None:
        print("failed to load")
        return

    # clean up the dataframe
    df_clean = clean_and_prepare_data(df, time_categories)