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

dados = [12, 15, 14, 13, 16, 12, 14, 150, 13, 15]

print(detectar_anomalias(dados, 1.5))