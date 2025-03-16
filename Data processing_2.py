import pandas as pd

# Load the Excel file
file_path = 'modified_data.xlsx'  # Replace this with your file path
sheet_name = 'Sheet1'  # Replace with your sheet name
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Define a function to convert dates to the desired format
def standardize_date(date):
    try:
        # Parse the date
        parsed_date = pd.to_datetime(date, errors='coerce')
        if pd.isnull(parsed_date):
            return date  # Return the original if parsing fails
        # Format the date without time
        return parsed_date.strftime('%m/%d/%Y')
    except Exception as e:
        return date  # Return the original date if an unexpected error occurs

# Apply the function to the date column
df['DATA'] = df['DATA'].apply(standardize_date)  # Replace 'DateColumn' with your actual column name

# Save the changes to a new Excel file
output_path = 'standardized_dates.xlsx'  # Specify your output file path
df.to_excel(output_path, index=False)

print(f"Dates standardized and saved to {output_path}")