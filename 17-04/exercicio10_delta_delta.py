leituras = [100, 120, 160]

delta1 = leituras[1] - leituras[0]
delta2 = leituras[2] - leituras[1]

delta_delta = delta2 - delta1

alerta = 1 if delta_delta > 20 else 0

print("Delta 1:", delta1)
print("Delta 2:", delta2)
print("Delta do Delta:", delta_delta)
print("Alerta:", alerta)