sensor_anterior = 80
sensor_atual = 100

delta = sensor_atual - sensor_anterior

evolucao_percentual = (delta / sensor_anterior) * 100

tendencia = "Crescimento" if delta > 0 else "Queda"

print("Delta:", delta)
print("Evolução %:", evolucao_percentual)
print("Tendência:", tendencia)