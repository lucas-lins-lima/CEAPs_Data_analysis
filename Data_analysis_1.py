import pandas as pd
import matplotlib.pyplot as plt
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import dash_table
import seaborn as sns

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

'''

# Suppose 'df' is your DataFrame already loaded with the appropriate data
# Ensure you've imported your data properly into a Pandas DataFrame named df

 def plot_scatter(df, x, y='VALOR_REEMBOLSADO', title='Scatter Plot'):
    plt.figure(figsize=(12, 6))
    plt.scatter(df[x], df[y], alpha=0.5)
    plt.title(f'{title} - {x} vs {y}')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(True)
    plt.show()

Plotting scatter plots for each time dimension
plot_scatter(df, 'ANO', title='Yearly Reimbursed Value')
plot_scatter(df, 'MES', title='Monthly Reimbursed Value')
plot_scatter(df, 'SEMESTRE', title='Semester Reimbursed Value')
plot_scatter(df, 'TRIMESTRE', title='Quarterly Reimbursed Value')
plot_scatter(df, 'BIMESTRE', title='Bimonthly Reimbursed Value')'
'''
'''

# Assuming 'df' is your DataFrame

def plot_line(df, time_column, title):
    plt.figure(figsize=(14, 7))
    for year in sorted(df['ANO'].unique()):
        yearly_data = df[df['ANO'] == year]
        plt.plot(yearly_data[time_column], yearly_data['VALOR_REEMBOLSADO'], marker='o', label=f'Year {year}')
      
    plt.title(title)
    plt.xlabel(time_column)
    plt.ylabel('Reimbursed Value')
    plt.legend()
    plt.grid(True)
    plt.show()

# Generate plots for each required time dimension viewed by year
# plot_line(df, 'MES', 'Monthly Reimbursed Value by Year')
# plot_line(df, 'SEMESTRE', 'Half-Yearly Reimbursed Value by Year')
# plot_line(df, 'TRIMESTRE', 'Quarterly Reimbursed Value by Year')
plot_line(df, 'BIMESTRE', 'Bimonthly Reimbursed Value by Year')'
'''

'''
# Assuming 'df' is your DataFrame with columns 'SENADOR', 'MES', 'VALOR_REEMBOLSADO', and 'ANO'
# Sample DataFrame setup if needed: df = pd.DataFrame({'SENADOR': [...], 'MES': [...], 'VALOR_REEMBOLSADO': [...], 'ANO': [...]})

# Create Dash app
app = dash.Dash(__name__)

# Ensure you have a non-empty list of senators
senator_list = df['SENADOR'].unique()

# Define the layout
app.layout = html.Div([
    dcc.Dropdown(
        id='senator-dropdown',
        options=[{'label': senator, 'value': senator} for senator in senator_list],
        value=senator_list[0],  # Default selection
        style={'width': '50%'}  # Adjust dropdown width
    ),
    dcc.Graph(id='reimbursed-value-graph')
])

@app.callback(
    Output('reimbursed-value-graph', 'figure'),
    [Input('senator-dropdown', 'value')]
)
def update_graph(selected_senator):
    # Filter data for the selected senator
    filtered_data = df[df['SENADOR'] == selected_senator]

    # Create the plot only if there is data to show
    if not filtered_data.empty:
        fig = px.line(
            filtered_data, 
            x='MES', 
            y='VALOR_REEMBOLSADO', 
            color='ANO',
            title=f'Monthly Reimbursed Value for {selected_senator} by Year'
        )
        fig.update_traces(mode='lines+markers')
        fig.update_layout(xaxis=dict(tickmode='linear'))
    else:
        # Display a message if no data is available
        fig = {'layout': {'title': f'No data available for {selected_senator}'}}

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
'''
     
'''
# Example data setup, replace with your actual DataFrame
# df = pd.DataFrame({
#     'SENADOR': [...],
#     'MES': [...],
#     'VALOR_REEMBOLSADO': [...],
#     'ANO': [...]
# })

# Create a Dash app
app = dash.Dash(__name__)

# Calculate the month with the highest reimbursement for each senator
highest_reimbursements = (
    df.groupby(['SENADOR', 'ANO', 'MES'])['VALOR_REEMBOLSADO'].sum()
    .reset_index()
    .sort_values(['SENADOR', 'VALOR_REEMBOLSADO'], ascending=[True, False])
    .drop_duplicates(subset=['SENADOR'])
)

# Sort the senators by their maximum monthly reimbursement
highest_reimbursements.sort_values('VALOR_REEMBOLSADO', ascending=False, inplace=True)

# Add a rank column
highest_reimbursements['Rank'] = highest_reimbursements['VALOR_REEMBOLSADO'].rank(ascending=False).astype(int)

# Define the layout
app.layout = html.Div([
    html.H1("Senators’ Highest Monthly Reimbursement"),
    dash_table.DataTable(
        id='reimbursement-table',
        columns=[
            {'name': 'Rank', 'id': 'Rank', 'type': 'numeric'},
            {'name': 'Senator', 'id': 'SENADOR', 'type': 'text'},
            {'name': 'Year', 'id': 'ANO', 'type': 'numeric'},
            {'name': 'Month', 'id': 'MES', 'type': 'numeric'},
            {'name': 'Value Reimbursed', 'id': 'VALOR_REEMBOLSADO', 'type': 'numeric'}
        ],
        data=highest_reimbursements.to_dict('records'),
        sort_action='native', # Allows for dynamic sorting in the table
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left', 'padding': '10px'},
        style_header={'backgroundColor': 'lightgrey', 'fontWeight': 'bold'}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
    '''


# Assuming 'df' is your DataFrame
# Calculate monthly averages and standard deviations
monthly_stats = df.groupby(['ANO', 'MES', 'SENADOR'])['VALOR_REEMBOLSADO'].sum().reset_index()
monthly_avg_std = monthly_stats.groupby(['ANO', 'MES'])['VALOR_REEMBOLSADO'].agg(['mean', 'std']).reset_index()

# Merge back with the monthly spending data to flag outliers
monthly_spending_with_stats = monthly_stats.merge(monthly_avg_std, on=['ANO', 'MES'])

# Calculate Z-scores to identify outliers
monthly_spending_with_stats['Z_score'] = (
    (monthly_spending_with_stats['VALOR_REEMBOLSADO'] - monthly_spending_with_stats['mean']) /
    monthly_spending_with_stats['std']
)

# Flagging senators with Z-score above a certain threshold (e.g., 2 or 3)
outliers = monthly_spending_with_stats[monthly_spending_with_stats['Z_score'] > 2]

# Visualize using a bar plot for monthly
# plt.figure(figsize=(14, 7))
# sns.barplot(data=monthly_spending_with_stats, x='MES', y='VALOR_REEMBOLSADO', hue='ANO', ci=None)
# plt.axhline(y=monthly_spending_with_stats['mean'].mean(), color='red', linestyle='--')
# plt.title('Monthly Spending with Yearly Averages')
# plt.show()


# Calculate annual averages and standard deviations
annual_stats = df.groupby(['ANO', 'SENADOR'])['VALOR_REEMBOLSADO'].sum().reset_index()
annual_avg_std = annual_stats.groupby(['ANO'])['VALOR_REEMBOLSADO'].agg(['mean', 'std']).reset_index()

# Merge back with the annual spending data to flag outliers
annual_spending_with_stats = annual_stats.merge(annual_avg_std, on=['ANO'])

# Flagging senators who are annual outliers
annual_spending_with_stats['Z_score'] = (
    (annual_spending_with_stats['VALOR_REEMBOLSADO'] - annual_spending_with_stats['mean']) /
    annual_spending_with_stats['std']
)
annual_outliers = annual_spending_with_stats[annual_spending_with_stats['Z_score'] > 2]

# Visualizing annual spending along with highlighted outliers
# plt.figure(figsize=(14, 7))
# sns.barplot(data=annual_spending_with_stats, x='ANO', y='VALOR_REEMBOLSADO', ci=None, alpha=0.5)
# plt.scatter(x=annual_outliers['ANO'], y=annual_outliers['VALOR_REEMBOLSADO'], color='red', label='Outliers')
# plt.axhline(y=annual_spending_with_stats['mean'].mean(), color='green', linestyle='--', label='Overall Mean')
# plt.title('Annual Spending with Outliers Highlighted')
# plt.xlabel('Year')
# plt.ylabel('Reimbursed Amount')
# plt.legend()
# plt.show()

# Monthly exceedance calculation
monthly_exceed_detail = monthly_stats[monthly_stats['VALOR_REEMBOLSADO'] > 25000]
monthly_exceed_table = monthly_exceed_detail[['ANO', 'MES', 'SENADOR', 'VALOR_REEMBOLSADO']]

# Yearly exceedance calculation
yearly_exceed_detail = annual_stats[annual_stats['VALOR_REEMBOLSADO'] > 240000]
yearly_exceed_table = yearly_exceed_detail[['ANO', 'SENADOR', 'VALOR_REEMBOLSADO']]

# print("Monthly Spending Exceedances by Senator:")
# print(monthly_exceed_table.to_string(index=False))  # For terminal or plain script

# Monthly Exceedances to Excel
# monthly_exceed_table.to_excel("monthly_exceedances.xlsx", index=False, engine='openpyxl')

# Display Yearly Exceedances
print("Yearly Spending Exceedances by Senator:")
print(yearly_exceed_table.to_string(index=False))  # For terminal or plain script

# Yearly Exceedances to Excel
yearly_exceed_table.to_excel("yearly_exceedances.xlsx", index=False, engine='openpyxl')