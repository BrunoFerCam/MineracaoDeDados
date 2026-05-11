import numpy as np

tempos = np.array([12, 15, 14, 13, 16, 12, 14, 150, 13, 15])

q1 = np.percentile(tempos, 25)
q3 = np.percentile(tempos, 75)

iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Limite Inferior:", limite_inferior)
print("Limite Superior:", limite_superior)