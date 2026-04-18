from sklearn.preprocessing import MinMaxScaler


temps = [[-20], [-10], [0], [20]]

scaler = MinMaxScaler()
temps_norm = scaler.fit_transform(temps)

print("Temperaturas originais:")
print(temps)

print("\nTemperaturas normalizadas:")
print(temps_norm)

valor_zero_original = temps_norm[2][0]
print(f"\n0°C continuou sendo 0 após normalização? {valor_zero_original == 0.0}")
print(
    "Não. O 0°C original mudou de posição porque o Min-Max reposiciona todos os valores "
    "entre o mínimo e o máximo observados."
)
print(
    "Aqui, -20 vira 0.0 (novo mínimo) e 20 vira 1.0 (novo máximo). "
    "Logo, o valor 0.0 na escala normalizada representa o menor valor da amostra, não 0°C."
)
