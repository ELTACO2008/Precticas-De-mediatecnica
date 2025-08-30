# lISTA DE CLIENTES CON SUS DATOS: id, NOMBRE Y EDAD

CLIENTES = [
    ["id", "nombre", "edad"],
    [1, "laura", 27],
    [2, "mateo", 34],
    [3, "camila", 29]
]

# Mostrar l nombre del tercer cliente (indice 2 en la lista)

print("El nombre del cliente es: ", CLIENTES[2][1])
print("\n" + "-" * 30 + "\n")

# Mostrar solo las edades de los clientes (excluyendo encabezado)

print("Edades de los clientes: ")
for columna in CLIENTES[1:]:
    print(f"- {columna[2]}")
print("\n" + "-" * 30 + "\n")

# Buscar y mostrar los datos del cliente con ID 2 

print("Datos del cliente con ID 2")
for fila in CLIENTES[1:]:
    if fila[0] == 2:
        print(f"ID: {fila[0]}, NOMBRE: {fila[1]}, EDAD: {fila[2]}")