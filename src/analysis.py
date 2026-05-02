import numpy as np
import pandas as pd

def resample_energy(df):
    # map out how to aggregate each column
    # active power gets averaged but sub metering gets added up
    agg_map = {
        "global_active_power": "mean",
        "global_reactive_power": "mean",
        "voltage": "mean",
        "global_intensity": "mean",
        "sub_metering_1": "sum",
        "sub_metering_2": "sum",
        "sub_metering_3": "sum",
    }

    # resample the data into different time chunks
    hourly = df.resample("h").agg(agg_map)
    daily = df.resample("d").agg(agg_map)
    weekly = df.resample("w").agg(agg_map)

    return hourly, daily, weekly

def calculate_summary(df):
    stats = df["global_active_power"].agg(["mean", "std", "min", "max", "median"])
    peak_timestamp = df["global_active_power"].idxmax()
    peak_value = df.loc[peak_timestamp, "global_active_power"]

    return {
        "mean": float(stats["mean"]),
        "std": float(stats["std"]),
        "min": float(stats["min"]),
        "max": float(stats["max"]),
        "median": float(stats["median"]),
        "peak_timestamp": peak_timestamp,
        "peak_value": float(peak_value),
    }

def top_peak_periods(hourly: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    peaks = hourly["global_active_power"].nlargest(n).to_frame(name="hourly_mean_active_power")
    peaks["timestamp"] = peaks.index
    return peaks[["timestamp", "hourly_mean_active_power"]]

def zscore_normalise(df: pd.DataFrame, columns):
    values = df[columns].to_numpy(dtype=float)

    means = values.mean(axis=0)
    stds = values.std(axis=0, ddof=0)
    stds = np.where(stds == 0, 1, stds)

    z_values = (values - means) / stds
    z_df = pd.DataFrame(
        z_values,
        index=df.index,
        columns=[f"{col}_zscore" for col in columns],
    )

    return z_df, means, stds

