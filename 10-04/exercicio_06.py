import numpy as np
from sklearn.ensemble import IsolationForest


np.random.seed(42)

dados_normais = np.random.normal(loc=0, scale=1, size=(1000, 2))

outliers_injetados = np.random.normal(loc=15, scale=0.5, size=(50, 2))

dados = np.vstack([dados_normais, outliers_injetados])

modelo_005 = IsolationForest(contamination=0.05, random_state=42)
pred_005 = modelo_005.fit_predict(dados)
qtd_anom_005 = np.sum(pred_005 == -1)

modelo_020 = IsolationForest(contamination=0.20, random_state=42)
pred_020 = modelo_020.fit_predict(dados)
qtd_anom_020 = np.sum(pred_020 == -1)

print(f"Anomalias detectadas com contamination=0.05: {qtd_anom_005}")
print(f"Anomalias detectadas com contamination=0.20: {qtd_anom_020}")
