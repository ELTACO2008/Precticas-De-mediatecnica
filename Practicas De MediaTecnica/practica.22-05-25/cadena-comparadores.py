"""Cadena de Comparadores"""
# edad = 25
edad = int(input("Ingresa la edad del usuario: "))

# Normalmente el codigo seria

if edad >= 15 and edad <= 65:
    print("Puede ingresar a la piscina..-codigo tradicional")
else:
    print("NO puede ingresar ala pisina..-codigo cadena comparadores")  

# Cualquiera de los 2 codigos sirve   

if 15 <= edad <= 65:
    print("Puede ingresar ala pisina..-codigo cadena comparadores")
else:
    print("NO puede ingresar ala pisina..-codigo cadena comparadores")  