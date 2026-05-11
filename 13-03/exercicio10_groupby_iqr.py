import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Sensor_ID": ["A", "A", "A", "A", "B", "B", "B", "B"],
    "Valor_Leitura": [10, 12, 11, 100, 50, 52, 51, 200]
})

def marcar_anomalias(grupo):
    q1 = grupo["Valor_Leitura"].quantile(0.25)
    q3 = grupo["Valor_Leitura"].quantile(0.75)

    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    grupo["Limite_Inferior"] = limite_inferior
    grupo["Limite_Superior"] = limite_superior

    grupo["Anomalia"] = (
        (grupo["Valor_Leitura"] < limite_inferior) |
        (grupo["Valor_Leitura"] > limite_superior)
    )

    return grupo

resultado = df.groupby("Sensor_ID", group_keys=False).apply(marcar_anomalias)

anomalias = resultado[resultado["Anomalia"]]

print(resultado)
print("Anomalias:")
print(anomalias)