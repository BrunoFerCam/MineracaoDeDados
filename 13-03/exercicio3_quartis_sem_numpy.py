dados = [100, 150, 200, 250, 300, 350]
dados.sort()

n = len(dados)
meio = n // 2

if n % 2 == 0:
    metade_inferior = dados[:meio]
    metade_superior = dados[meio:]
else:
    metade_inferior = dados[:meio]
    metade_superior = dados[meio + 1:]

def mediana(lista):
    tamanho = len(lista)
    meio = tamanho // 2

    if tamanho % 2 == 0:
        return (lista[meio - 1] + lista[meio]) / 2
    else:
        return lista[meio]

q1 = mediana(metade_inferior)
q3 = mediana(metade_superior)

print("Metade inferior:", metade_inferior)
print("Metade superior:", metade_superior)
print("Q1:", q1)
print("Q3:", q3)