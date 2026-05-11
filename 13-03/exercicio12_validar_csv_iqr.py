import pandas as pd

df = pd.read_csv("dados_sensores.csv")

colunas_numericas = df.select_dtypes(include="number").columns

for coluna in colunas_numericas:
    df[coluna] = df[coluna].fillna(df[coluna].median())

colunas_analisadas = ["temperatura_celsius", "pressao_psi"]

mascara = pd.Series(True, index=df.index)

for coluna in colunas_analisadas:
    q1 = df[coluna].quantile(0.25)
    q3 = df[coluna].quantile(0.75)

    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    mascara = mascara & (
        (df[coluna] >= limite_inferior) &
        (df[coluna] <= limite_superior)
    )

df_validado = df[mascara]

df_validado.to_csv("dados_validados.csv", index=False)

print("Arquivo dados_validados.csv gerado com sucesso.")
print(df_validado)