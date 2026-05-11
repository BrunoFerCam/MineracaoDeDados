emails = [
    "ana@gmail.com",
    "joao@empresa.com.br",
    "maria@yahoo.com",
    "suporte@corp.com.br"
]

for email in emails:
    dominio = email.split("@")[1]

    flag_empresarial = 1 if dominio.endswith(".com.br") else 0

    print(email, dominio, flag_empresarial)