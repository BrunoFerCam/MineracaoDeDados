import pandas as pd

datas = pd.to_datetime([
    "2026-12-25",
    "2026-11-27",
    "2026-06-15"
])

feriados = ["12-25", "11-27"]

df = pd.DataFrame({"data_transacao": datas})

df["flag_evento"] = df["data_transacao"].dt.strftime("%m-%d").isin(feriados).astype(int)

print(df)