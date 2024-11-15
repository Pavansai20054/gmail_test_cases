import pandas as pd

file_path = r"s:\IIIrd Year\DevOps\CI-CD\Pavan_Manual Testing Steps table.xlsx"
data = pd.read_excel(file_path)

# Updated validation rules based on actual column names
required_columns = ["Test scenario ID", "Test Case Step", "Expected", "Actual"]
missing_columns = [col for col in required_columns if col not in data.columns]
if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")

# Checking for empty required cells in these columns
if data[required_columns].isnull().values.any():
    raise ValueError("Some required cells are empty in the specified columns.")

print("Validation passed successfully!")
