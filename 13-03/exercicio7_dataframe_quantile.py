import pandas as pd

df = pd.DataFrame({
    "ID_Maquina": [1, 2, 3, 4, 5],
    "Uso_Memoria_MB": [2048, 2100, 2050, 8192, 2080]
})

q1 = df["Uso_Memoria_MB"].quantile(0.25)
q3 = df["Uso_Memoria_MB"].quantile(0.75)

iqr = q3 - q1

print(df)
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)