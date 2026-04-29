import pandas as pd

def clean_and_prepare_data(df, time_bins_labels):
    # clean the energy data and fix timestamps
    # handle missing values so charts dont break later
    print("starting data cleaning")
    
    # find columns that should be numbers ignoring date and time
    cols_to_fix = [c for c in df.columns if c not in ['date', 'time']]
    
    # convert text to numbers and force errors to become nan
    for col in cols_to_fix:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # fill missing sensor data by carrying the last known value forward
    print("filling missing values")
    df[cols_to_fix] = df[cols_to_fix].ffill().bfill()

    # set up the proper time series index starting from 2007
    print("setting up the timeline index")
    start_date = pd.Timestamp("2007-01-01 00:00:00")
    
    # assuming data is recorded every minute
    df['timestamp'] = pd.date_range(start=start_date, periods=len(df), freq='min')
    df = df.set_index('timestamp')

    # add extra columns for easier grouping
    df['hour'] = df.index.hour
    df['day_of_week'] = df.index.day_name()

    # bin the hours into categories like morning or night
    df['time_period'] = pd.cut(
        df['hour'],
        bins=[-1, 5, 11, 17, 21, 24],
        labels=time_bins_labels
    )

    print("cleaning complete. data ready")
    return df

# temporary test block so you can verify it works locally
if __name__ == "__main__":
    from data_loading import load_dataset
    from config import raw_csv_file, time_categories
    
    print("testing preprocessing")
    raw_data = load_dataset(raw_csv_file)
    cleaned_data = clean_and_prepare_data(raw_data, time_categories)
    
    print("first 5 rows of cleaned data:")
    print(cleaned_data.head())