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
    
def plot_daily_trend(daily: pd.DataFrame):
    _, ax = plt.subplots(figsize=(14, 5))
    plot_df = daily.reset_index()
    plot_df["rolling_7d"] = plot_df["global_active_power"].rolling(window=7, min_periods=1).mean()

    sns.lineplot(data=plot_df, x="timestamp", y="global_active_power", ax=ax, linewidth=1.0, label="Daily mean")
    sns.lineplot(data=plot_df, x="timestamp", y="rolling_7d", ax=ax, linewidth=2.0, label="7-day rolling mean")
    ax.set_title("Daily Global Active Power with 7-Day Rolling Mean")
    ax.set_xlabel("Date")
    ax.set_ylabel("Global Active Power (kW)")
    save_current_figure("03_daily_active_power.png")

def plot_weekly_trend(weekly: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(14, 5))
    plot_df = weekly.reset_index()
    sns.lineplot(data=plot_df, x="timestamp", y="global_active_power", ax=ax, marker="o")
    ax.set_title("Weekly Average Global Active Power")
    ax.set_xlabel("Week")
    ax.set_ylabel("Global Active Power (kW)")
    save_current_figure("04_weekly_active_power.png")