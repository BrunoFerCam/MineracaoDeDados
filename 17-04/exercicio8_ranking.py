import pandas as pd

df = pd.DataFrame({
    "produto": ["A","B","C","D"],
    "vendas": [500,300,700,200]
})

df["ranking"] = df["vendas"].rank(ascending=False)

print(df)