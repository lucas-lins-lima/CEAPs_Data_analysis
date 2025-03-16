import pandas as pd
import re

# Load your spreadsheet into a DataFrame
# For Excel: df = pd.read_excel('your_file.xlsx')
# For CSV: df = pd.read_csv('your_file.csv')
df = pd.read_excel('Ceaps_expense_every_year.xlsx')  # Make sure to adjust the file path and name as necessary

# Step 1: Fill Blank Cells
# Fill numeric columns with 0
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(0)

# Fill text columns with "n/d"
text_cols = df.select_dtypes(include='object').columns
df[text_cols] = df[text_cols].fillna('n/d')

# Step 2: Separate CPFs and CNPJs
def separate_cpfs_cnpjs(df):
    cpfs = []
    cnpjs = []

    pattern_cpf = r'\d{3}\.\d{3}\.\d{3}-\d{2}'
    pattern_cnpj = r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}'

    for value in df['CNPJ_CPF']:
        if re.match(pattern_cpf, str(value)):
            cpfs.append(value)
            cnpjs.append(None)
        elif re.match(pattern_cnpj, str(value)):
            cpfs.append(None)
            cnpjs.append(value)
        else:
            cpfs.append(None)
            cnpjs.append(None)
    
    df['CPF'] = cpfs
    df['CNPJ'] = cnpjs
    return df

df = separate_cpfs_cnpjs(df)

# Step 3: Standardize VALOR_REEMBOLSADO
def format_currency(value):
    try:
        value = float(value)
        return f"R${value:,.2f}"
    except ValueError:
        return value  # If conversion fails, return the original value

df['VALOR_REEMBOLSADO'] = df['VALOR_REEMBOLSADO'].apply(format_currency)

# Step 4: Separate EXPENSE_TYPE into Multiple Columns
# Split the EXPENSE_TYPE column
expense_types = df['TIPO_DESPESA'].str.split(',', expand=True)

# Add new columns to the DataFrame
for i in range(expense_types.shape[1]):
    df[f'TIPO_DESPESA_{i+1}'] = expense_types[i]

# Optionally drop the original EXPENSE_TYPE column
# df.drop(columns=['EXPENSE_TYPE'], inplace=True)

# Save the modified DataFrame to a new Excel file
df.to_excel('modified_data.xlsx', index=False)  # Adjust the file name as needed