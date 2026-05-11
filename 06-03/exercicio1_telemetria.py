import pandas as pd

df = pd.DataFrame({
    "Temperatura_C": ["25", "30", "falha_sinal", "28", "erro"]
})

df["Temperatura_C_Num"] = pd.to_numeric(df["Temperatura_C"], errors="coerce")

falhas = df[df["Temperatura_C_Num"].isna()]

print(falhas)