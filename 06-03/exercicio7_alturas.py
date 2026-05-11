import pandas as pd

df = pd.DataFrame({
    "Paciente": ["Ana", "Bruno", "Carlos"],
    "Altura_Metros": [1.70, 2.50, 170]
})

alturas_invalidas = df[
    (df["Altura_Metros"] < 0.5) |
    (df["Altura_Metros"] > 2.5)
]

print(alturas_invalidas)