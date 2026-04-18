from sklearn.ensemble import IsolationForest


dados = [[8, 2], [7, 4], [9, 1], [8, 3], [2, 25], [9, 25]]

modelo = IsolationForest(contamination=0.34, random_state=42, n_estimators=300)
predicoes = modelo.fit_predict(dados)

print("Dados [Nota, Faltas] e predição:")
for ponto, pred in zip(dados, predicoes):
    print(f"{ponto} -> {pred}")

indice_alvo = dados.index([9, 25])
pred_alvo = predicoes[indice_alvo]

if pred_alvo == -1:
    print("\nO aluno [9, 25] foi detectado como anomalia (-1).")
else:
    print("\nO aluno [9, 25] não foi marcado como anomalia nesta configuração do modelo.")
