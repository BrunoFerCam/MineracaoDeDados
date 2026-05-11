import pandas as pd
from datetime import datetime

ano_atual = datetime.now().year

df = pd.DataFrame({
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Ano_Nascimento": [2000, 1995, 2010],
    "Idade_Declarada": [25, 20, 15]
})

df["Idade_Real"] = ano_atual - df["Ano_Nascimento"]

inconsistencias = df[df["Idade_Real"] != df["Idade_Declarada"]]

print(inconsistencias)