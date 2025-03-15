## Entre no site abaixo e escolha o que quer buscar
## https://adm.senado.gov.br/adm-dadosabertos/swagger-ui/index.html?configUrl=/adm-dadosabertos/swagger-config.json#/
## No exemplo abaixo estou buscando as despesas CEAPS

import requests
import pandas as pd

import requests

url = "https://adm.senado.gov.br/adm-dadosabertos/api/v1/senadores/despesas_ceaps/2025"
response = requests.get(url)
data = response.json()

# Print a portion of the data to understand its structure
print(data[:3])  # Printing the first three entries or datasets

url = "https://adm.senado.gov.br/adm-dadosabertos/api/v1/senadores/despesas_ceaps/2025"
response = requests.get(url)
data = response.json()

# Assume the data is a list of dictionaries
if isinstance(data, list):
    # Convert list of dictionaries to DataFrame directly
    df = pd.DataFrame(data)
else:
    # If it's a dictionary, further investigation needed
    print("Unexpected data format:", type(data))
    df = pd.DataFrame()  # fallback empty DataFrame

# Save DataFrame to an Excel file
df.to_excel("despesas_ceaps_2025.xlsx", index=False)