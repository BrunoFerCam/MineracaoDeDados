from sklearn.preprocessing import MinMaxScaler


minimo = 100
maximo = 500
leitura = 200

valor_manual = (leitura - minimo) / (maximo - minimo)

pressao = [[100], [200], [500]]
scaler = MinMaxScaler()
pressao_normalizada = scaler.fit_transform(pressao)

valor_codigo = float(pressao_normalizada[1][0])

print(f"Valor normalizado manual para 200 psi: {valor_manual:.4f}")
print("Valores normalizados com MinMaxScaler:")
print(pressao_normalizada)
print(f"Valor normalizado via código para 200 psi: {valor_codigo:.4f}")
print(f"Bate com a conta manual? {abs(valor_manual - valor_codigo) < 1e-9}")
