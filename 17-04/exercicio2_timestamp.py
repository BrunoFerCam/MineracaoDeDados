import pandas as pd

datas = pd.to_datetime([
    "2026-05-10 10:00",
    "2026-05-11 14:00",
    "2026-05-16 20:00"
])

df = pd.DataFrame({"timestamp": datas})

df["mes"] = df["timestamp"].dt.month
df["dia_semana"] = df["timestamp"].dt.day_name()

df["flag_final_semana"] = df["timestamp"].dt.weekday >= 5

print(df)