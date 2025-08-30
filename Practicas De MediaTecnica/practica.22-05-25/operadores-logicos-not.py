"""Practica con operadores logicos"""


# Los operadores que veremos: and,or y not
# and - ambos verdaderos

gas = True
encendido = True
if not gas or not encendido:
    print("Puedes avanzar -Not true- not True")
else:
    print("NO puedes avanzar -not true -not true")

gas = False
encendido = True
if not gas or encendido:
    print("Puedes avanzar -Not true- not True")

gas = False
encendido = False
if gas or encendido:
    print("Puedes avanzar -Not true- not True")







        
        