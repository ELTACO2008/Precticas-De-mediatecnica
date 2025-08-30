# Valores fijos
SUBSIDIO_TRANSPORTE = 200000  # Valor aproximado 2025 (mensual)
HORAS_SEMANA = 48
SEMANAS_MES = 30

# Recargos según ley colombiana
RECARGO_EXTRA_DIURNA = 1.25
RECARGO_EXTRA_NOCTURNA = 1.75
RECARGO_DOMINICAL = 1.75

# Lista de empleados (nombres ficticios)
empleados = [
    ["Carlos Pérez", "Operario", 2300000, 0, 10, 0, True],
    ["María López", "Operario", 2300000, 0, 10, 0, True],
    ["Andrés Gómez", "Operario", 2300000, 0, 10, 0, True],
    ["Laura Torres", "Operario", 2300000, 0, 10, 0, True],
    ["Pedro Ramírez", "Operario", 2300000, 0, 10, 0, True],

    ["Luisa Martínez", "Operario", 2100000, 12, 0, 0, True],
    ["Jorge Sánchez", "Operario", 2100000, 12, 0, 0, True],
    ["Camila Díaz", "Operario", 2100000, 12, 0, 0, True],
    ["Felipe Castro", "Operario", 2100000, 12, 0, 0, True],
    ["Sofía Morales", "Operario", 2100000, 12, 0, 0, True],

    ["Miguel Rojas", "Operario", 1800000, 6, 6, 0, True],
    ["Valentina Ruiz", "Operario", 1800000, 6, 6, 0, True],
    ["Daniel Herrera", "Operario", 1800000, 6, 6, 0, True],
    ["Paula Ortega", "Operario", 1800000, 6, 6, 0, True],
    ["Esteban Gil", "Operario", 1800000, 6, 6, 0, True],

    ["Sara Jiménez", "Operario", 2000000, 0, 0, 8, True],
    ["Ricardo Peña", "Operario", 2000000, 0, 0, 8, True],
    ["Natalia Vargas", "Operario", 2000000, 0, 0, 8, True],

    ["Alejandro Mejía", "Gerente", 10000000, 0, 0, 0, False],
    ["Carolina Suárez", "Secretaria", 3000000, 0, 0, 0, False],
]

# Función para calcular pago semanal
def calcular_pago(emp):
    nombre, cargo, sueldo_mensual, horas_d, horas_n, horas_dom, tiene_subsidio = emp
    
    sueldo = (sueldo_mensual / SEMANAS_MES) * 7
    valor_hora = sueldo / HORAS_SEMANA
    subsidio = (SUBSIDIO_TRANSPORTE / SEMANAS_MES) * 7 if tiene_subsidio else 0

    pago_extra_diurna = horas_d * valor_hora * RECARGO_EXTRA_DIURNA
    pago_extra_nocturna = horas_n * valor_hora * RECARGO_EXTRA_NOCTURNA
    pago_dominical = horas_dom * valor_hora * RECARGO_DOMINICAL

    total = sueldo + subsidio + pago_extra_diurna + pago_extra_nocturna + pago_dominical
    return {
        "nombre": nombre,
        "cargo": cargo,
        "sueldo": sueldo,
        "subsidio": subsidio,
        "extra_diurna": pago_extra_diurna,
        "extra_nocturna": pago_extra_nocturna,
        "dominical": pago_dominical,
        "total": total
    }

# Función para imprimir colilla estilo factura
def imprimir_colilla(empleado):
    datos = calcular_pago(empleado)
    ancho_linea = 60
    print("\n" + "-" * ancho_linea)
    print(f"Empleado: {datos['nombre']:<20} Cargo: {datos['cargo']:<15}")
    print("-" * ancho_linea)
    print(f"{'Sueldo base (semanal):':30} ${datos['sueldo']:>15,.0f}")
    if datos['subsidio'] > 0:
        print(f"{'Subsidio transporte:':30} ${datos['subsidio']:>15,.0f}")
    if datos['extra_diurna'] > 0:
        print(f"{'Pago extra diurna:':30} ${datos['extra_diurna']:>15,.0f}")
    if datos['extra_nocturna'] > 0:
        print(f"{'Pago extra nocturna:':30} ${datos['extra_nocturna']:>15,.0f}")
    if datos['dominical'] > 0:
        print(f"{'Pago dominical:':30} ${datos['dominical']:>15,.0f}")
    print("-" * ancho_linea)
    print(f"{'TOTAL SEMANAL:':30} ${datos['total']:>15,.0f}")
    print("-" * ancho_linea)

# Función listado general de empleados (versión compacta)
def listado_general():
    print("\n" + "="*130)
    print(f"{'LISTADO GENERAL DE EMPLEADOS (SEMANALES)':^130}")
    print("="*130)

    print(
        f"{'N°':<3} {'Nombre':<20} {'Cargo':<15} {'Sueldo ($)':>12} "
        f"{'H.D':>4} {'H.N':>4} {'H.Dom':>5} "
        f"{'Extra D ($)':>12} {'Extra N ($)':>12} {'Dominical ($)':>14} "
        f"{'Subsidio ($)':>12} {'Total ($)':>12}"
    )
    print("-"*130)

    total_empresa = 0
    for i, emp in enumerate(empleados, start=1):
        datos = calcular_pago(emp)
        total_empresa += datos['total']
        print(
            f"{i:<3} {datos['nombre']:<20} {datos['cargo']:<15} ${datos['sueldo']:>11,.0f} "
            f"{emp[3]:>4} {emp[4]:>4} {emp[5]:>5} "
            f"${datos['extra_diurna']:>11,.0f} ${datos['extra_nocturna']:>11,.0f} ${datos['dominical']:>13,.0f} "
            f"${datos['subsidio']:>11,.0f} ${datos['total']:>11,.0f}"
        )

    print("="*130)
    print(f"{'TOTAL NÓMINA EMPRESA (SEMANAL)':<115} ${total_empresa:,.0f}")

# Función para imprimir todas las colillas
def todas_colillas():
    for emp in empleados:
        imprimir_colilla(emp)

# Menú principal
def menu():
    while True:
        print("\n" + "=" * 50)
        print(" MENÚ DE OPCIONES ".center(50, "="))
        print("1. Listado general de empleados")
        print("2. Colilla de un empleado en particular")
        print("3. Todas las colillas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listado_general()
        elif opcion == "2":
            listado_general()
            try:
                num = int(input("Ingrese el número del empleado: "))
                if 1 <= num <= len(empleados):
                    imprimir_colilla(empleados[num-1])
                else:
                    print("Empleado no válido.")
            except ValueError:
                print("Entrada inválida, por favor ingrese un número.")
        elif opcion == "3":
            todas_colillas()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar menú
menu()