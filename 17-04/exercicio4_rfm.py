import pandas as pd
from datetime import datetime

dados = {
    "id_cliente": [1,1,2,2,3],
    "data": ["2026-05-01","2026-05-10","2026-04-20","2026-05-08","2026-05-09"],
    "valor": [100,200,150,300,500]
}

df = pd.DataFrame(dados)

df["data"] = pd.to_datetime(df["data"])

data_referencia = datetime(2026,5,15)

rfm = df.groupby("id_cliente").agg({
    "data": lambda x: (data_referencia - x.max()).days,
    "id_cliente": "count",
    "valor": "sum"
})

rfm.columns = ["Recencia", "Frequencia", "ValorMonetario"]

print(rfm)