import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.config import graphs_folder, time_categories, days_of_week

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
    _, ax = plt.subplots(figsize=(14, 5))
    plot_df = weekly.reset_index()
    sns.lineplot(data=plot_df, x="timestamp", y="global_active_power", ax=ax, marker="o")
    ax.set_title("Weekly Average Global Active Power")
    ax.set_xlabel("Week")
    ax.set_ylabel("Global Active Power (kW)")
    save_current_figure("04_weekly_active_power.png")

def plot_distribution(df: pd.DataFrame):
    _, ax = plt.subplots(figsize=(12, 5))
    sample = df["global_active_power"].sample(n=min(50000, len(df)), random_state=42)

    sns.histplot(sample, bins=60, stat="density", element="step", fill=False, ax=ax, color="tab:blue")
    sns.kdeplot(sample, ax=ax, color="black", linewidth=2)
    ax.set_title("Distribution of Global Active Power")
    ax.set_xlabel("Global Active Power (kW)")
    ax.set_ylabel("Density")
    save_current_figure("05_distribution_active_power.png")

def plot_box_by_hour(df: pd.DataFrame):
    _, ax = plt.subplots(figsize=(14, 5))
    sns.boxplot(data=df.reset_index(), x="hour", y="global_active_power", ax=ax)
    ax.set_title("Global Active Power by Hour of Day")
    ax.set_xlabel("Hour of Day")
    ax.set_ylabel("Global Active Power (kW)")
    save_current_figure("06_boxplot_by_hour.png")

def plot_violin_by_time_of_day(df: pd.DataFrame):
    _, ax = plt.subplots(figsize=(12, 5))
    sns.violinplot(data=df.reset_index(), x="time_period", y="global_active_power", order=time_categories, ax=ax, inner="quartile", cut=0)
    ax.set_title("Global Active Power by Time of Day")
    ax.set_xlabel("Time of Day")
    ax.set_ylabel("Global Active Power (kW)")
    save_current_figure("07_violin_by_time_of_day.png")

def plot_weekday_hour_heatmap(df: pd.DataFrame):
    pivot = (df.reset_index().pivot_table(index="day_of_week", columns="hour", values="global_active_power", aggfunc="mean").reindex(days_of_week))
    _, ax = plt.subplots(figsize=(14, 5))
    sns.heatmap(pivot, ax=ax, cmap="viridis")
    ax.set_title("Average Global Active Power by Weekday and Hour")
    ax.set_xlabel("Hour of Day")
    ax.set_ylabel("Day of Week")
    save_current_figure("08_weekday_hour_heatmap.png")

def plot_normalised_metrics(z_df: pd.DataFrame):
    _, ax = plt.subplots(figsize=(12, 5))
    long_df = z_df.reset_index(drop=True).melt(var_name="metric", value_name="zscore")

    sns.boxplot(data=long_df, x="metric", y="zscore", ax=ax)
    ax.set_title("Broadcast-Normalised Metrics (Z-Scores)")
    ax.set_xlabel("Metric")
    ax.set_ylabel("Z-Score")
    save_current_figure("09_normalised_metrics_boxplot.png")