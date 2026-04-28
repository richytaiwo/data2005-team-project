import pandas as pd

def load_dataset(file_path):
    """
    Reads the raw dataset from the CSV file.
    I added some error handling so the script doesn't just crash 
    if someone forgets to put the file in the data folder.
    """
    print(f"Loading data from: {file_path}")
    
    try:
        df = pd.read_csv(file_path)
        
        # fix the column names (lowercase and no extra spaces)
        df.columns = df.columns.str.strip().str.lower()
        
        print(f"Success {len(df)} loaded")
        return df
        
    except FileNotFoundError:
        print("ERROR: CSV file not found")
        raise
    except Exception as e:
        print(f"Something went wrong: {e}")
        raise