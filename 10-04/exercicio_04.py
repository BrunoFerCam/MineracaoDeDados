import numpy as np
from scipy.stats import zscore


medidas = [10, 12, 11, 10, 10000]

media = np.mean(medidas)
desvio_padrao = np.std(medidas, ddof=0)
z_scores = zscore(medidas)
z_10000 = z_scores[-1]

print(f"Média da lista: {media:.4f}")
print(f"Desvio padrão da lista: {desvio_padrao:.4f}")
print(f"Z-Score do valor 10000: {z_10000:.4f}")

if z_10000 > 3:
    print("O valor 10000 ultrapassa a marca de 3.")
else:
    print("O valor 10000 NÃO ultrapassa a marca de 3.")
    print("Isso acontece porque o outlier infla o desvio padrão, reduzindo o próprio Z-Score.")
