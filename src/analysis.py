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

def zscore_normalise(df, metrics):
    # normalise using numpy broadcasting
    z_values = {}
    means = {}
    stds = {}

    for col in metrics:
        # convert column to a numpy array for the fast math
        data_array = df[col].to_numpy()
        
        # get mean and standard deviation ignoring any lingering nan values
        col_mean = np.nanmean(data_array)
        col_std = np.nanstd(data_array)
        
        # broadcast the calculation across the whole array at once
        # this is much faster than looping through rows one by one
        z_score = (data_array - col_mean) / col_std
        
        z_values[col] = z_score
        means[col] = col_mean
        stds[col] = col_std
        
    return z_values, means, stds 