import pandas as pd

df = pd.DataFrame({
    "Sistema_Operacional": [
        "Ubuntu", "Ubuntu", "Debian", "Armbian",
        "Ubuntu", "Debian", "ErroOS"
    ]
})

proporcoes = df["Sistema_Operacional"].value_counts(normalize=True)

raros = proporcoes[proporcoes < 0.05]

print(raros)