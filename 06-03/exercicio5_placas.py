import pandas as pd

df = pd.DataFrame({
    "Placa_Veiculo": [
        "ABC1234",
        "AB123",
        "XYZ9876",
        "AAAA11111"
    ]
})

placas_invalidas = df[df["Placa_Veiculo"].str.len() != 7]

print(placas_invalidas)