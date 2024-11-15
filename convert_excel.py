import pandas as pd

file_path = "Pavan_Manual Testing Steps table.xlsx"
data = pd.read_excel(file_path)

# Save as CSV
csv_path = file_path.replace(".xlsx", ".csv")
data.to_csv(csv_path, index=False)
print(f"File converted to CSV: {csv_path}")

# Save as JSON
json_path = file_path.replace(".xlsx", ".json")
data.to_json(json_path, orient="records")
print(f"File converted to JSON: {json_path}")
