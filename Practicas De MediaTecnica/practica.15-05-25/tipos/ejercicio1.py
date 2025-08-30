contador = 1
while contador <= 10:

# ingresar informacion manual del trabajador 
    id = int(input("Ingrese el id: "))
    nombre = input("Ingrese el nombre del empleado: ")
    salario_mes = int(input("Ingrese el salario mensual: "))
    dia = int(input("Ingrese dias trabajados: "))


    # calcular salario dia dividiendo dia por mes (30)
    salario_dia = salario_mes / 30
    # calcular salario quincena
    salario_quincena = salario_dia * dia
    

    # Se imprime los datos del trabajador con su salario
    print(" ")
    print("Los datos para la nomina de: ", nombre)
    print("Su id es: ", id)
    print("Su salario quincenal es:", salario_quincena)
    print(" ")
    
    contador += 1


