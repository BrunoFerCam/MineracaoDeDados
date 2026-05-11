import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Temperatura": [80, 82, 85, 81, 300, 83]
})

q1 = np.percentile(df["Temperatura"], 25)
q2 = np.percentile(df["Temperatura"], 50)
q3 = np.percentile(df["Temperatura"], 75)

iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

df["Temperatura_Corrigida"] = np.where(
    (df["Temperatura"] < limite_inferior) |
    (df["Temperatura"] > limite_superior),
    q2,
    df["Temperatura"]
)

print("Mediana:", q2)
print(df)