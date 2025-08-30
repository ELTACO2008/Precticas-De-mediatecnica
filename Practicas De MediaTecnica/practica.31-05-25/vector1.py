""""Ejemplo de vector"""

# Se ingresan los n elementos del vector

n = int(input("inserte el tamaño de la lista: "))
l = [None] * (n +1)
for i in range (1, n + 1, 1):
    l[i] = int(input("Ingrese un numero: "))

# Se imprime el contenido del vector

print(l[1:n+1])

# Se procede a listar en forma inversa
# el contenido de l

for i in range(n, 0, -1):
    print(l[i])

# Se imprime el contenido del vector
# en forma inversa

print(l[n+1:0-1])