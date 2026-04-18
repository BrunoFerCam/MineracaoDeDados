from scipy.stats import zscore


voltagem = [3.3, 3.2, 3.3, 3.4, 3.3, 1.2, 3.2, 3.3]
z_scores = zscore(voltagem)

print("Z-Scores das voltagens:")
for valor, z in zip(voltagem, z_scores):
    print(f"Voltagem: {valor:.1f} V | Z-Score: {z:.3f}")

if any(z < -2.0 for z in z_scores):
    print("Falha de Energia!")
else:
    print("Sem falhas críticas de energia.")
