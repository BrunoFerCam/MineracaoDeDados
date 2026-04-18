from sklearn.ensemble import IsolationForest


servidores = [[20, 30], [25, 35], [22, 32], [99, 95], [21, 31]]

modelo = IsolationForest(random_state=42)
modelo.fit(servidores)
predicoes = modelo.predict(servidores)

print("Predições do Isolation Forest:")
print(predicoes.tolist())
