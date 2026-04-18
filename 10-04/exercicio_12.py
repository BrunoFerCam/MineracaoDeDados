import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler


producao = [100, 102, 98, 105, 500, 101]

z_scores = zscore(producao)
dados_limpos = [valor for valor, z in zip(producao, z_scores) if abs(z) <= 3]

scaler = MinMaxScaler()
dados_limpos_array = np.array(dados_limpos).reshape(-1, 1)
dados_normalizados = scaler.fit_transform(dados_limpos_array).flatten().tolist()

print(f"Dados originais: {producao}")
print(f"Z-Scores: {[round(z, 4) for z in z_scores]}")
print(f"Dados limpos (sem outlier): {dados_limpos}")
print(f"Lista final normalizada: {[round(v, 4) for v in dados_normalizados]}")

print("\nPor que normalizar depois de remover outliers?")
print(
    "Se o valor 500 permanecesse, ele definiria um máximo muito distante e comprimira os "
    "valores normais em uma faixa muito pequena perto de 0. Isso reduziria a sensibilidade "
    "da análise para diferenças reais entre as leituras normais."
)
