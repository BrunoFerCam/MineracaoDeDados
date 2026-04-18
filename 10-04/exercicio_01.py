from scipy.stats import zscore


temp = [45.5, 46.0, 45.2, 45.8, 46.1, 98.0, 45.9, 45.3]
z_scores = zscore(temp)

anomalias = [valor for valor, z in zip(temp, z_scores) if z > 2.5]

print("Temperaturas anômalas (Z-Score > 2.5):")
for valor in anomalias:
    print(valor)
