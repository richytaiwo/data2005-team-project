from pathlib import Path

# getting the main folder path so the script works on everyone's laptop in the team
project_root = Path(__file__).resolve().parent.parent

# paths for reading and saving our csv files
raw_csv_file = project_root / "data" / "raw" / "household_power_consumption.csv"
cleaned_csv_export = project_root / "data" / "processed" / "household_energy_consumption_cleaned.csv"

# folders for saving our generated plots and reports
graphs_folder = project_root / "outputs" / "figures"
reports_folder = project_root / "outputs" / "reports"

# making sure the output folders actually exist so the script doesn't crash when saving
graphs_folder.mkdir(parents=True, exist_ok=True)
reports_folder.mkdir(parents=True, exist_ok=True)

# custom sorting lists so our charts print in a logical order later
time_categories = ["Night", "Morning", "Afternoon", "Evening", "Late Night"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]