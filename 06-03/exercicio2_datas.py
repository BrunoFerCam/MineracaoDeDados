import pandas as pd

df = pd.DataFrame({
    "Data_Compra": pd.to_datetime(["2026-03-01", "2026-03-05", "2026-03-10"]),
    "Data_Entrega": pd.to_datetime(["2026-03-03", "2026-03-01", "2026-03-12"])
})

erros = df[df["Data_Entrega"] < df["Data_Compra"]]

print(erros)