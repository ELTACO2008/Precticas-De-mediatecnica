"""Medos con Strings"""

animal = "Chanchito Feliz"
# El metodo convierte en mayuscula
print(animal.upper())

# El metodo convierte en minuscula
print(animal.lower())

# El metodo convierte le primera letra a mayuscula
print(animal.capitalize())

# El metodo convierte las primeras letras de cada palabra a mayusculas
print(animal.title())

# el metodo remueve los espacios a la izquierda y a la derecha del string
animal= "chanChito Feliz"
print(animal.strip())

# vamos a encadenar metodos
# encadenamos el metodo strip y el metodo capitalizeel
# el metodo remueve los espacios a la izquiera y derecha del string
# metodo convierte la primera letra a mayuscula
animal = "   chanChito Feliz    "
print(animal.lstrip())
print(animal.rstrip())

# el metodo find devuelve el indice de donde se encuentra una
# cadena de caractener en el string
animal = "chanChito Feliz"
print(animal.find("Ch"))

# el metodo find devuelve el indice de donde se encuentra una 
# cadena de caracteres en el string. Que ocurre cuando la 
# cadena no existe en el string
animal = "chanChito Feliz"
print(animal.find("CH"))

# el metodo freplace reemplaza una cadena por un caracter 
# o caracteres en el string
animal = "chanChito Feliz"
print(animal.replace("nCh", "j"))

# el metodo in, me indica un valor de verdad
# True o False, si se encuentra o no una cadena
# en el string
animal = "chanChito Feliz"
print("Ch" in animal)

# el metodo not in, me indica si una cadena no
# se encuentra en el string
animal = "chanChito Feliz"
print("Ch" not in animal)
