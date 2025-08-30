# practica de python
import datetime  # Importamos el módulo datetime

# Defino el iva de cada producto
iva_lacteos = 1.0
iva_gaseosas = 1.18
iva_carnicos = 1.16
iva_otros = 1.20

# Defino las banderas para los ciclos de clientes y ciclos de productos
bandera_clientes = True
bandera_productos = True

# Lista para guardar los productos de cada cliente
productos_del_cliente = []

# Inicializamos el contador de facturas
numero_factura = 0

# iniciamos el ciclo while para los clientes que llegan a pagar
# productos a la caja

while bandera_clientes == True:
    # Incrementamos el número de factura para cada cliente
    numero_factura += 1

    # Imprimo encabezado de titulos
    print(" ")
    print("========================")
    print("    NUEVO CLIENTE")
    print("========================")
    print(" ")

    # Solicitamos la información del cliente
    tipo_documento_input = input("Ingrese el tipo de documento (cc/ti/otro): ").lower()
    if tipo_documento_input == "cc":
        tipo_documento = "Cédula de Ciudadanía"
    elif tipo_documento_input == "ti":
        tipo_documento = "Tarjeta de Identidad"
    else:
        tipo_documento = tipo_documento_input.capitalize()  # Capitalizar otras entradas

    numero_documento = input("Ingrese el número de documento: ")
    nombre_persona = input("Ingrese el nombre de la persona: ").title()  # Capitalizar nombres

    # Iniciamos el ciclo while  para procesar los productos
    # que trae un cliente a la caja
    bandera_productos = True  # Reiniciamos la bandera para cada cliente
    acomulador_iva_cliente = 0
    acomulador_producto_cliente = 0
    productos_del_cliente = [] # Reiniciamos la lista de productos para cada cliente

    while bandera_productos == True:

        # Ingreso la informacion de cada producto, tipo, descripcion, precio y cantidad

        tipo_producto = int(input("Selecciona tipo producto:\n1. Lácteos\n2. Gaseosas\n3. Cárnicos\n4. Otros\nOpción: "))
        descripcion_producto = input("Ingrese la descripción del producto: ").capitalize()  # Capitalizar descripciones
        precio_producto = float(input("Ingrese el precio unitario del producto: ")) # Usar float para precios
        cantidad_producto = int(input("Ingrese la cantidad del producto: "))

        # Calculo precio total de productos sin iva

        precio_producto_sin_iva = precio_producto * cantidad_producto

        # Calculo el iva para cada tipo de producto

        if tipo_producto == 1:
            precio_producto_con_iva = precio_producto_sin_iva * iva_lacteos
            iva_aplicado = precio_producto_sin_iva * (iva_lacteos - 1)
        elif tipo_producto == 2:
            precio_producto_con_iva = precio_producto_sin_iva * iva_gaseosas
            iva_aplicado = precio_producto_sin_iva * (iva_gaseosas - 1)
        elif tipo_producto == 3:
            precio_producto_con_iva = precio_producto_sin_iva * iva_carnicos
            iva_aplicado = precio_producto_sin_iva * (iva_carnicos - 1)
        elif tipo_producto == 4:
            precio_producto_con_iva = precio_producto_sin_iva * iva_otros
            iva_aplicado = precio_producto_sin_iva * (iva_otros - 1)
        else:
            precio_producto_con_iva = 0
            iva_aplicado = 0

        # Acomulo el precio del producto con iva y el valor del iva para este cliente

        acomulador_iva_cliente += iva_aplicado
        acomulador_producto_cliente += precio_producto_con_iva

        # Guardo la información del producto en la lista
        productos_del_cliente.append({
            "descripcion": descripcion_producto,
            "precio_unitario": precio_producto,
            "cantidad": cantidad_producto,
            "precio_con_iva": precio_producto_con_iva,
            "iva_aplicado": iva_aplicado
        })

        # *** Esta es la parte que quieres conservar (mejorada visualmente) ***
        print("\n" + "=" * 20)
        print("  PRODUCTO AGREGADO")
        print("=" * 20)
        print(f"Producto: {descripcion_producto}")
        print(f"Precio Unitario: ${precio_producto:.2f}")
        print(f"Cantidad: {cantidad_producto}")
        print(f"Precio con IVA: ${precio_producto_con_iva:.2f}")
        print("-" * 20 + "\n")
        # *** Fin de la parte que quieres conservar ***

        hay_productos = input("¿Hay más productos? (s/n): ").lower()
        if hay_productos == "n":
            bandera_productos = False

    # Imprimo total para la factura del cliente (mejorado visualmente)
    print("\n" + "=" * 30)
    print("           FACTURA FINAL")
    print("=" * 30)
    print(f"Número de Factura: {numero_factura:04d}") # Formato con ceros a la izquierda
    print(f"Fecha y Hora: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 30)
    print(f"Cliente: {nombre_persona}")
    print(f"Tipo de Documento: {tipo_documento}")
    print(f"Número de Documento: {numero_documento}")
    print("-" * 30)
    print("DETALLE DE PRODUCTOS:")
    for producto in productos_del_cliente:
        print(f"- {producto['descripcion']} ({producto['cantidad']} x ${producto['precio_unitario']:.2f}) = ${producto['precio_con_iva']:.2f}")
    print("-" * 30)
    print(f"Subtotal: ${acomulador_producto_cliente - acomulador_iva_cliente:.2f}")
    print(f"Total IVA Pagado: ${acomulador_iva_cliente:.2f}")
    print(f"TOTAL A PAGAR: ${acomulador_producto_cliente:.2f}")
    print("=" * 30 + "\n")

    hay_clientes = input("¿Hay más clientes? (s/n): ").lower()
    if hay_clientes == "n":
        bandera_clientes = False

    print("¡Gracias por su compra!")


















