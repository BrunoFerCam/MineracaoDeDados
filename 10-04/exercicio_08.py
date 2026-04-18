import pandas as pd
from sklearn.ensemble import IsolationForest


df = pd.DataFrame(
    {
        "idade": [17, 18, 16, 19, 17, 150],
        "horas_estudo": [8, 10, 7, 9, 11, 2],
        "nota_final": [7.5, 8.2, 7.0, 8.0, 8.4, 1.0],
    }
)

modelo = IsolationForest(contamination=0.16, random_state=42)
df["Outlier"] = modelo.fit_predict(df)

anomalias = df[df["Outlier"] == -1]

print("DataFrame com coluna Outlier:")
print(df)

print("\nApenas linhas anômalas:")
print(anomalias)
