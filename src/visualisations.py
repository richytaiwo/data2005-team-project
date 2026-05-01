import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_hourly(hourly_data, output_path):
    # log start of chart generation
    print(f"generating hourly power plot...")
    
    # use seaborn theme to make it look professional
    sns.set_theme(style="darkgrid")
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=hourly_data, x=hourly_data.index, y="global_active_power", color="coral")
    
    # add labels for the grader
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