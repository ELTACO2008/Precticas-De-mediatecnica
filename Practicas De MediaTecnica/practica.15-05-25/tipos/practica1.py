total_factura = 0
total_iva_pagado = 0

print("Bienvenido a la tienda don Gustavo.")

while True:
    descripcion = input("Ingrese la descripción del producto (o 'terminar' para ver su factura total): ")

    if descripcion.lower() == 'terminar':
        break

    try:
        cantidad = int(input("Ingrese la cantidad: "))
        precio_unitario = float(input("Ingrese el precio unitario: "))

        categoria = input("Ingrese la categoría (lacteos, carnicos, gaseosas, otros): ").lower()
    except ValueError:
        print("Error: Ingrese números válidos para cantidad y precio.")
        continue

    if cantidad <= 0 or precio_unitario <= 0:
        print("Error: La cantidad y el precio deben ser mayores que cero.")
        continue

    if categoria == "lacteos":
        iva_porcentaje = 0.10  
    elif categoria == "carnicos":
        iva_porcentaje = 0.16  
    elif categoria == "gaseosas":
        iva_porcentaje = 0.12  
    else:
        iva_porcentaje = 0.20  

    iva = precio_unitario * iva_porcentaje
    precio_total_producto = (precio_unitario + iva) * cantidad

    print("\nInformación del producto:")
    print(f"Descripción: {descripcion}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio Unitario: ${precio_unitario:.2f}")  
    print(f"IVA ({iva_porcentaje*100:.0f}%): ${iva:.2f}")  
    print(f"Precio Total: ${precio_total_producto:.2f}") 

    total_factura += precio_total_producto
    total_iva_pagado += iva * cantidad

print("\n--- Factura Final ---")
print(f"Total IVA Pagado: ${total_iva_pagado:.2f}")
print(f"Total de la Factura: ${total_factura:.2f}")


while True:
    metodo_pago = input("\nSeleccione el método de pago (tarjeta o efectivo): ").lower()
    if metodo_pago == 'tarjeta':
        while True:
            numero_tarjeta = input("Ingrese el número de tarjeta (16 digitos numericos): ")
            if 16 <= len(numero_tarjeta) <= 16 and numero_tarjeta.isdigit():
                break
            else:
                print("Número de tarjeta inválido. Debe tener 16 digitos numericos.")

        while True:
            fecha_vencimiento = input("Ingrese la fecha de vencimiento (MM/AA): ")
            if len(fecha_vencimiento) == 5 and fecha_vencimiento[2] == '/' and fecha_vencimiento[:2].isdigit() and fecha_vencimiento[3:].isdigit():
                mes = int(fecha_vencimiento[:2])
                anio = int(fecha_vencimiento[3:])
                if 1 <= mes <= 12 and anio >= 23: 
                    break
                else:
                    print("Fecha de vencimiento inválida. Formato MM/AA y mes válido (01-12).")
            else:
                print("Formato de fecha de vencimiento inválido. Debe ser MM/AA.")

        while True:
            cvv = input("Ingrese el código de seguridad de 3 dígitos: ")
            if len(cvv) == 3 and cvv.isdigit():
                break
            else:
                print("Código de seguridad inválido. Debe tener 3 dígitos numéricos.")

        print(f"Pago con tarjeta registrado. Número: ****-****-****-{numero_tarjeta[-4:]}, Vencimiento: {fecha_vencimiento}")
        print("\n¡Gracias por su compra!")
        break
    elif metodo_pago == 'efectivo':
        print("\nPor favor, inserte el dinero por el orificio que parpadea en verde.")
        print("\n¡Gracias por su compra!")
        break
    else:
        print("Opción de pago inválida. Por favor, ingrese 'tarjeta' o 'efectivo'.")



 




