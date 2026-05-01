import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_hourly(hourly_data, output_path):
    # log start of chart generation
    print(f"generating hourly power plot...")
    
    # use seaborn theme
    sns.set_theme(style="darkgrid")
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=hourly_data, x=hourly_data.index, y="global_active_power", color="coral")
    
    # add labels and title
    plt.title("average hourly global active power")
    plt.xlabel("timestamp")
    plt.ylabel("active power (kw)")
    plt.tight_layout()
    
    # create figures folder if it doesnt exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # save and close
    plt.savefig(output_path)
    plt.close()
    
    print(f"saved chart successfully to {output_path}")
    # end of plot_hourly function

def plot_correlation_heatmap(df, output_path):
    # check how the different sub-meters correlate with overall power
    print("generating correlation heatmap...")
    
    plt.figure(figsize=(10, 8))
    
    # grab only the numeric columns for the math
    numeric_df = df.select_dtypes(include=['float64', 'int32', 'int64'])
    
    # calculate correlations and plot them
    correlation_matrix = numeric_df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    
    plt.title("sensor data correlation heatmap")
    plt.tight_layout()
    
    plt.savefig(output_path)
    plt.close()
    
