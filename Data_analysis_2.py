import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_squared_error
import numpy as np
import os

# Load your DataFrame, assuming it's already loaded into 'df'
file_path = 'Final_Table.xlsx'
df = pd.read_excel(file_path)

# Correct the cleansing step with raw string literals
# Ensure all values contain only numbers and a single decimal point
df['VALOR_REEMBOLSADO'] = df['VALOR_REEMBOLSADO'].replace(r'[^\d.]', '', regex=True)

# Convert to numeric and ensure rounding to two decimal places
df['VALOR_REEMBOLSADO'] = pd.to_numeric(df['VALOR_REEMBOLSADO'], errors='coerce').round(2)

# Check if any values became NaN during conversion
missing_count = df['VALOR_REEMBOLSADO'].isnull().sum()
print(f'Number of NaN values in VALOR_REEMBOLSADO after conversion: {missing_count}')


# Check for non-date entries
print(df['DATA'].unique())

# Remove or handle non-date entries
df = df[df['DATA'] != '0']  # Or any other invalid entry

# Convert the 'DATA' column to datetime format
df['DATA'] = pd.to_datetime(df['DATA'], errors='coerce', format='%m/%d/%Y')

# Check for conversion results and investigate unparseable dates
print(df['DATA'].isna().sum())  # Check the number of NaT values

# Drop rows with NaT values in 'DATA' if necessary
df = df.dropna(subset=['DATA'])

df['DATA'] = pd.to_datetime(df['DATA'], errors='coerce')

if df['DATA'].isna().any():
    print("There are still incorrect date formats that need manual inspection.")

'''
# Sample data frame setup
# df = pd.read_csv('your_expenses_data.csv') # Load your data
df['DATA'] = pd.to_datetime(df['DATA'])
df = df.set_index('DATA')

# Summarizing expenses by month or any other relevant period
monthly_expenses = df.resample('ME')['VALOR_REEMBOLSADO'].sum()

monthly_expenses.plot(title='Monthly Reimbursed Expenses', figsize=(12, 6))
plt.show()

# Prepare data for Prophet
df_prophet = monthly_expenses.reset_index()
df_prophet.columns = ['ds', 'y']

# Fit Prophet model
model = Prophet()
model.fit(df_prophet)

# Forecast
future = model.make_future_dataframe(periods=12, freq='M')
forecast = model.predict(future)

# Plot
fig = model.plot(forecast)
plt.show()

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(monthly_expenses, forecast['yhat'][:len(monthly_expenses)]))
print(f'Root Mean Squared Error: {rmse}')

plt.figure(figsize=(12, 6))
plt.plot(monthly_expenses, label='Observed')
plt.plot(forecast['ds'], forecast['yhat'], label='Forecast')
plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='gray', alpha=0.2)
plt.title('Forecast vs Actuals')
plt.legend()
plt.show()
'''

# Sample structure of data loading
# df = pd.read_csv('your_expenses_data.csv')
df['DATA'] = pd.to_datetime(df['DATA'])

# Directory to save the plots
output_directory = "forecast_plots"

# Create directory if it does not exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to forecast expenses and save plots for each senator
def forecast_by_senator(df):
    # Get list of unique senators
    senators = df['SENADOR'].unique()

    for senator in senators:
        # Filter data for each senator
        senator_data = df[df['SENADOR'] == senator]

        if senator_data.empty:
            continue

        # Resample data by month to aggregate expenses
        monthly_expenses = senator_data.resample('M', on='DATA')['VALOR_REEMBOLSADO'].sum().reset_index()

        if monthly_expenses.empty:
            continue

        # Prepare data for Prophet
        monthly_expenses.columns = ['ds', 'y']  # Prophet requires these specific column names

        # Initialize and fit Prophet model
        model = Prophet()
        model.fit(monthly_expenses)

        # Create future dataframe and forecast
        future = model.make_future_dataframe(periods=12, freq='M')
        forecast = model.predict(future)

        # Plot results
        plt.figure(figsize=(10, 6))
        plt.title(f"Expenses Forecast for {senator}")
        plt.plot(monthly_expenses['ds'], monthly_expenses['y'], label='Observed', marker='o')
        plt.plot(forecast['ds'], forecast['yhat'], label='Forecast', linestyle='--', color='orange')
        plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='gray', alpha=0.2)
        plt.xlabel('Date')
        plt.ylabel('Expense (Reais)')
        plt.legend()
        plt.grid(True)

        # Save each plot as a PNG file
        plt_file_path = os.path.join(output_directory, f"{senator}_forecast.png")
        plt.savefig(plt_file_path)
        plt.close()  # Close the plot to save memory

        print(f"Saved forecast plot for {senator} at {plt_file_path}")

# Call the function to forecast for each senator and save the plots
forecast_by_senator(df)