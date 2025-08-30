while True:
    day = input("Ingresa un día de la semana >>> ").lower()

    match day:
        case "sabado" | "domingo":
            print(f"{day} es fin de semana.")
        case "lunes" | "martes" | "miercoles" | "jueves" | "viernes":
            print(f"{day} es un día laboral.")
        case _:
            print("El texto ingresado no corresponde a un día de la semana.")

    salir = input("¿Quieres salir? (si/no) >>> ").lower()
    if salir == "si":
        print("Programa finalizado.")
        break
