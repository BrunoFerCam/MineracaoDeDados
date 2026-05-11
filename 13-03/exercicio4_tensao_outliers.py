import numpy as np

tensoes = np.array([110, 115, 120, 118, 112, 220, 116, 114, 119, 12])

q1 = np.percentile(tensoes, 25)
q3 = np.percentile(tensoes, 75)

iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

anomalias = [valor for valor in tensoes if valor < limite_inferior or valor > limite_superior]

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Limite Inferior:", limite_inferior)
print("Limite Superior:", limite_superior)
print("Valores anômalos:", anomalias)