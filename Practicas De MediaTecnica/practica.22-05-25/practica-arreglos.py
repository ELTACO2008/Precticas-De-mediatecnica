iva_hogar = 1.16  # IVA del 16% para productos del hogar
iva_aseo = 1.17    # IVA del 17% para productos de aseo
iva_herramientas = 1.18 # IVA del 18% para herramientas
iva_otros = 1.19   # IVA del 19% para otras categorías

# Diccionario para mapear los tipos de producto a sus tasas de IVA y mensajes descriptivos
ivas_por_tipo = {
    "Hogar": {"valor": iva_hogar, "mensaje": "16%"},
    "Aseo": {"valor": iva_aseo, "mensaje": "17%"},
    "Herramientas": {"valor": iva_herramientas, "mensaje": "18%"},
    "Otros": {"valor": iva_otros, "mensaje": "19%"}
}

# Lista para almacenar todos los productos que se van agregando
all_products = []
MAX_PRODUCTS = 6 # Set the maximum number of products

print("✨🛒 ¡Bienvenido al Generador de Facturas Simplificado! 🛒✨")
print("----------------------------------------------------------")

# --- Bucle principal para la entrada de productos ---
while True:
    if len(all_products) >= MAX_PRODUCTS:
        print(f"\n¡Has alcanzado el límite de {MAX_PRODUCTS} productos. No puedes agregar más!")
        break

    tipo_producto_options = list(ivas_por_tipo.keys())
    print("\n--- Selecciona el Tipo de Producto ---")
    for i, producto in enumerate(tipo_producto_options):
        print(f"  {i + 1}. {producto}")
    print("  0. Terminar y Generar Factura")

    while True:
        try:
            tipo_producto_choice = int(input("Ingresa tu opción por número: "))
            if tipo_producto_choice == 0:
                break # Sale del bucle de selección de tipo para terminar
            if 1 <= tipo_producto_choice <= len(tipo_producto_options):
                tipo_producto_seleccionado = tipo_producto_options[tipo_producto_choice - 1]
                break
            else:
                print("⚠️ Opción inválida. Por favor, selecciona un número de la lista.")
        except ValueError:
            print("❌ Entrada inválida. Debes ingresar un número entero.")
    
    if tipo_producto_choice == 0:
        break # Sale del bucle principal si el usuario eligió terminar

    nombre_articulo = input(f"📝 Ingresa el nombre del artículo para '{tipo_producto_seleccionado}': ")
    
    while True:
        try:
            precio_unitario = float(input(f"💲 Ingresa el precio unitario de '{nombre_articulo}': "))
            if precio_unitario >= 0: # Validar que el precio no sea negativo
                break
            else:
                print("⚠️ El precio unitario no puede ser negativo.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número válido para el precio.")

    while True:
        try:
            cantidad_articulo = int(input(f"🔢 Ingresa la cantidad de '{nombre_articulo}': "))
            if cantidad_articulo > 0: # Asegurar que la cantidad sea positiva
                break
            else:
                print("⚠️ La cantidad debe ser un número entero positivo.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número entero para la cantidad.")

    # Obtener la información del IVA según el tipo de producto seleccionado
    iva_info = ivas_por_tipo[tipo_producto_seleccionado]
    
    # Calcular precios
    precio_unitario_con_iva = iva_info["valor"] * precio_unitario
    subtotal_por_articulo = precio_unitario_con_iva * cantidad_articulo
    porcentaje_iva_aplicado = iva_info["mensaje"]

    # Almacenar la información del producto en un diccionario
    product_info = {
        "nombre": nombre_articulo,
        "precio_sin_iva_unitario": precio_unitario,
        "cantidad": cantidad_articulo,
        "tipo": tipo_producto_seleccionado,
        "iva_aplicado": porcentaje_iva_aplicado,
        "precio_total_unitario_con_iva": precio_unitario_con_iva,
        "subtotal_por_articulo": subtotal_por_articulo
    }
    all_products.append(product_info)

    # --- Confirmación de Producto Agregado ---
    print("\n--- ✅ Producto Agregado Exitosamente ---")
    print(f"Nombre: {nombre_articulo}")
    print(f"Tipo: {tipo_producto_seleccionado}")
    print(f"Precio Unitario (sin IVA): ${precio_unitario:.2f}")
    print(f"Cantidad: {cantidad_articulo}")
    print(f"IVA Aplicado: {porcentaje_iva_aplicado}")
    print(f"Precio Unitario (con IVA): ${precio_unitario_con_iva:.2f}")
    print(f"Subtotal por '{nombre_articulo}': ${subtotal_por_articulo:.2f}")
    print("------------------------------------------")


# --- Generación de Factura Final ---
if not all_products:
    print("\n😔 No se ingresaron productos. ¡Vuelve pronto!")
else:
    print("\n╔═══════════════════════════════════════════════════════════════════════════════════════════")
    print("║           📄✨ ¡FACTURA FINAL DE COMPRA! ✨📄                                               ")
    print("╠═══════════════════════════════════════════════════════════════════════════════════════════")
    # Adjusted column widths for better alignment
    print(f"║ {'Categoría':<15} {'Producto':<20} {'Cant.':<8} {'Precio Unit.':<13} {'IVA %':<8} {'IVA Monto':<11} {'Subtotal':<15} ")
    print(f"║ {'-'*15:<15} {'-'*20:<20} {'-'*8:<8} {'-'*13:<13} {'-'*8:<8} {'-'*11:<11} {'-'*15:<15} ")
    
    total_general_factura = 0
    for product in all_products:
        # Calculate the IVA amount for each item (unit IVA amount * quantity)
        monto_iva_por_articulo = product['precio_sin_iva_unitario'] * (ivas_por_tipo[product['tipo']]['valor'] - 1) * product['cantidad']
        
        # Adjusted padding for each column to ensure perfect alignment
        print(
            f"║ {product['tipo']:<15} "
            f"{product['nombre']:<20} "
            f"{product['cantidad']:<8} "
            f"${product['precio_sin_iva_unitario']:.2f}{'':<6} " # 13 total width, $ and 2 decimals, 6 remaining padding
            f"{product['iva_aplicado']:<8} "
            f"${monto_iva_por_articulo:.2f}{'':<4} " # 11 total width, $ and 2 decimals, 4 remaining padding
            f"${product['subtotal_por_articulo']:.2f}{'':<8} " # 15 total width, $ and 2 decimals, 8 remaining padding
        )
        total_general_factura += product['subtotal_por_articulo']

    print("╠═══════════════════════════════════════════════════════════════════════════════════════════")
    # Adjusted padding for the total line
    print(f"║ {'TOTAL GENERAL A PAGAR:':<73} ${total_general_factura:.2f}{'':<13} ")
    print("╚═══════════════════════════════════════════════════════════════════════════════════════════")
    print("\n¡Gracias por tu compra! ¡Vuelve pronto! 😊")