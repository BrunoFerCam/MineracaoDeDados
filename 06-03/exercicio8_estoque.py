import pandas as pd

df = pd.DataFrame({
    "Componente": ["Resistor", "Capacitor", "Arduino"],
    "Quantidade_Estoque": [50, -10, 999999]
})

problemas = df[
    (df["Quantidade_Estoque"] < 0) |
    (df["Quantidade_Estoque"] > 10000)
]

print(problemas)