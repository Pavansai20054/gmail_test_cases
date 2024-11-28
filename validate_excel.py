import pandas as pd

def validate_excel(file_path):
    try:
        # Load the Excel file
        df = pd.read_excel(file_path)

        # Check for missing data
        if df.isnull().values.any():
            raise ValueError("The Excel file contains missing data.")

        # Validate structure (Example: Check required columns)
        required_columns = ['Column1', 'Column2']  # Replace with actual column names
        if not all(col in df.columns for col in required_columns):
            raise ValueError(f"The file is missing required columns: {required_columns}")

        print("Validation passed: The Excel file meets all criteria!")

    except Exception as e:
        print(f"Validation failed: {e}")
        exit(1)

# Specify your file name here
file_path = 'Pavan_Manual Testing Steps table.xlsx'
validate_excel(file_path)
