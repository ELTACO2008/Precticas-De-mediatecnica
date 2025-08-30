aseo = 1.12
hogar = 1.20
ferreteria = 1.15
alimentos = 1.10
vestuario = 1.20
otros = 1.19

nombre_supermercado = ("Dijite el nombre del supermercado: ")
nombre_cliente = input("Dijite el nombre del cliente: ")

while True:
 tipo_identificacion_input = input("Dijite el tipo de targeta de identidad cc, ti , otros: ")
 if tipo_identificacion_input == "cc":
    tipo_identificacion = "Cedula de ciudadania"
    break
 if tipo_identificacion_input == "ti":
    tipo_identificacion = "Targeta de Identidad"
    break
 if tipo_identificacion_input == "otros":
    tipo_identificacion = "otros"
    break
 else: 
  print("Dijite una entrada validad porfavor")


 filas = 10
 columnas = int(input("Cuantas columnas quieres?"))

 matriz = []

 for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = input(f"Ingresa el valor para la fila {i+1}, columna {j+1}: ")
        fila.append(valor)
    matriz.append(fila)

 print("\nMatriz generada: ")
 for fila in matriz:
    print(fila)

 for fila in matriz:
    if fila[0]==20:
        print(matriz)




























#pedir adicional el nombre del cliente y el documento y el tipo - esto es fila de titulos va primero en la factura
#Y el nombre del supermercado (SOlo se pueden 10 productos)

#Despues poner el contedino de todos los productos abajo de la factura
#Total bruto antes del iva, el iva y el total a pagar