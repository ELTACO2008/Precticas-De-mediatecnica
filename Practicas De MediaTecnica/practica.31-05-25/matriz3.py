import numpy as np

# Crear un array 

clientes = np.array([
    ["pedro", 25],
    ["carmen",21],
    ["manuel",31],
    ["camilo",29]
], dtype=object)

#mostrar toda la lista de clientes
print("lista de clientes")
print(clientes)

#mostrar el nombre del tercer cliente (indice 2)
print("\nNombre del tercer cliente: ")
print(clientes[2][0])