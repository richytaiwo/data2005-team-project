import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.config import graphs_folder

sns.set_theme(style="whitegrid", context="talk")
plt.rcParams["figure.dpi"] = 140

def save_current_figure(filename: str):
    plt.tight_layout()
    plt.savefig(graphs_folder / filename, bbox_inches="tight")
    plt.close()
    
def plot_hourly_trend(hourly: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(14, 5))
    plot_df = hourly.reset_index()

    sns.lineplot(data=plot_df, x="timestamp", y="global_active_power", ax=ax, linewidth=1.2, color="#4C72B0")
    ax.set_title("Hourly Average Global Active Power")
    ax.set_xlabel("Time")
    ax.set_ylabel("Global Active Power (kW)")
    save_current_figure("01_hourly_active_power.png")

def plot_correlation_heatmap(df: pd.DataFrame):
    plt.figure(figsize=(10, 8))
    numeric_df = df.select_dtypes(include=['float64', 'int32', 'int64'])
    correlation_matrix = numeric_df.corr()
    
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Sensor Data Correlation Heatmap")
    save_current_figure("02_sensor_correlation_heatmap.png")
    
