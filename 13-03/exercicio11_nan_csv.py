import pandas as pd

df = pd.read_csv("dados_sensores.csv")

print("Valores ausentes por coluna:")
print(df.isna().sum())

colunas_numericas = df.select_dtypes(include="number").columns

for coluna in colunas_numericas:
    df[coluna] = df[coluna].fillna(df[coluna].median())

print("DataFrame sem valores NaN:")
print(df)