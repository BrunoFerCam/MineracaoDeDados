import numpy as np

def detectar_anomalias(dados, multiplicador):
    dados = np.array(dados)

    q1 = np.percentile(dados, 25)
    q3 = np.percentile(dados, 75)

    iqr = q3 - q1

    limite_inferior = q1 - multiplicador * iqr
    limite_superior = q3 + multiplicador * iqr

    anomalias = [
        valor for valor in dados
        if valor < limite_inferior or valor > limite_superior
    ]

    return anomalias

vetor = [45, 50, 55, 60, 48, 52, 51, 98, 49, 53]

resultado = detectar_anomalias(vetor, 1.5)

print("Anomalias encontradas:", resultado)