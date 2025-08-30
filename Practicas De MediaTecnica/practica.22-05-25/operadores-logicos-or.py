"""Practica con operadores logicos"""


# Los operadores que veremos: and,or y not
# and - ambos verdaderos

gas = True
encendido = True
if gas or encendido:
    print("Puedes avanzar -True-True")
else: 
    print("NO Puedes avanzar -false-false")

# and -falso verdadero

gas = False
encendido = True
if gas or encendido:
    print("Puedes avanzar - False-True")
else: 
    print("NO Puedes avanzar -false-True")

# and -falso falso

gas = False
encendido = False
if gas or encendido:
    print("Puedes avanzar - False-False") 
else: 
    print("NO Puedes avanzar -false-false")
        