import pandas as pd
from scipy.stats import zscore


vendas = [1200, 1350, 1250, 1300, 13500, 1280]

df = pd.DataFrame({"vendas": vendas})
df["z_score"] = zscore(df["vendas"])

df_limpo = df[df["z_score"].abs() <= 3]

print("DataFrame original com Z-Score:")
print(df)

print("\nDataFrame filtrado (dados limpos):")
print(df_limpo)
