horarios = [2, 9, 15, 22]

for hora in horarios:

    if 0 <= hora < 6:
        turno = "Madrugada"
    elif 6 <= hora < 18:
        turno = "Comercial"
    else:
        turno = "Noite"

    print(hora, turno)