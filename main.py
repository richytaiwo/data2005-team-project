import os
from src.config import raw_csv_file, time_categories, graphs_folder
from src.data_loading import load_dataset
from src.preprocessing import clean_and_prepare_data
from src.analysis import resample_energy, calculate_summary, zscore_normalise, top_peak_periods
from src.visualisations import plot_hourly_trend, plot_correlation_heatmap

def run_pipeline():
    # load data
    df = load_dataset(raw_csv_file)

    # preprocess data
    df_clean = clean_and_prepare_data(df, time_categories)

    # time-series analysis
    hourly, daily, weekly = resample_energy(df_clean)
    
    # descriptive statistics
    summary = calculate_summary(df_clean)
    
    # normalisation
    metrics_to_scale = ["global_active_power", "global_reactive_power", "voltage", "global_intensity"]
    z_df, means, stds = zscore_normalise(df_clean, metrics_to_scale)

    # terminal output
    print("=" * 30)
    print("ENERGY DATA SUMMARY")
    print("=" * 30)
    print(f"Mean active power: {summary['mean']:.3f} kW")
    print(f"Std active power:  {summary['std']:.3f} kW")
    print(f"Min active power:  {summary['min']:.3f} kW")
    print(f"Max active power:  {summary['max']:.3f} kW")
    print(f"Peak timestamp:    {summary['peak_timestamp']}")
    print(f"Peak value:        {summary['peak_value']:.3f} kW")

    # visualisations
    print("\nGenerating charts")
    plot_hourly_trend(hourly)
    plot_correlation_heatmap(df_clean)

    print(f"\nPipeline Complete. Saved figures to: {graphs_folder}")

if __name__ == "__main__":
    run_pipeline()