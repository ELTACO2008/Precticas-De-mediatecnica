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





