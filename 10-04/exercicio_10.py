import pandas as pd
from sklearn.preprocessing import MinMaxScaler


df = pd.DataFrame(
    {
        "cliente": ["A", "B"],
        "saldo": [1_000_000, 1_000_010],
        "risco": [0.1, 0.9],
    }
)

print("Explicação:")
print(
    "Sem normalização, o saldo (na casa de milhões) domina a distância entre clientes. "
    "Como a diferença de saldo é só 10 reais, o modelo tende a considerar os dois quase iguais "
    "na dimensão financeira e pode subvalorizar o salto de risco de 0.1 para 0.9."
)

scaler = MinMaxScaler()
df_normalizado = df.copy()
df_normalizado[["saldo", "risco"]] = scaler.fit_transform(df[["saldo", "risco"]])

print("\nDados originais:")
print(df)

print("\nDados normalizados:")
print(df_normalizado)

print("\nApós normalizar, o saldo vira [0, 1] e o risco também vira [0, 1].")
print("A diferença de 10 reais continua existindo, mas fica proporcional à escala total.")
print("Assim, a variação forte do risco passa a ter peso comparável na análise.")
