import sqlite3
import datetime

# Conectar a la base de datos (se crea el archivo si no existe)
conn = sqlite3.connect('inventario_supermercado.db')
cursor = conn.cursor()

def crear_tabla_productos():
    """Borra la tabla y la vuelve a crear para asegurar la estructura correcta.
    Ahora usa la combinación de codigo y categoria como clave primaria para permitir
    codigos duplicados en diferentes categorías."""
    cursor.execute("DROP TABLE IF EXISTS productos")
    cursor.execute('''CREATE TABLE productos
                      (codigo INTEGER,
                      nombre TEXT,
                      categoria TEXT,
                      unidad TEXT,
                      existencia REAL,
                      precio REAL,
                      iva REAL,
                      PRIMARY KEY (codigo, categoria))''') # Clave primaria compuesta
    conn.commit()
    print("Base de datos lista para empezar.")

def agregar_producto():
    """Función para agregar un nuevo producto al inventario.
    Ahora valida el codigo y la categoría al instante para evitar duplicados."""
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    
    # Definimos la lista de categorías válidas y sus IVAs correspondientes
    categorias_validas = ['Lacteos', 'Carnicos', 'Limpieza', 'Otros']
    ivas_por_categoria = {
        'Lacteos': 19,
        'Carnicos': 5,
        'Limpieza': 19,
        'Otros': 19
    }
    
    try:
        while True:
            codigo = int(input(f"Ingrese el codigo del producto: "))
            
            # Mostramos las categorías y sus IVAs
            print("Categorías disponibles y sus IVAs:")
            for cat, iva in ivas_por_categoria.items():
                print(f"- {cat}: {iva}%")
            
            categoria = input("Ingrese la categoría: ").capitalize()
            if categoria in categorias_validas:
                # --- Validación instantánea de codigo repetido ---
                cursor.execute("SELECT COUNT(*) FROM productos WHERE codigo = ? AND categoria = ?", (codigo, categoria))
                if cursor.fetchone()[0] > 0:
                    print(f"\nError: El codigo {codigo} ya existe en la categoría {categoria}. Por favor, ingrese un codigo diferente.")
                    continue # Volvemos a pedir el codigo
                else:
                    break # El codigo es válido, salimos del bucle
            else:
                print("Categoría no válida. Por favor, elija una de la lista.")

        nombre = input("Ingrese el nombre del producto: ")
        unidad = input("Ingrese la unidad de medida (Ej: unidad, kg, litro): ")
        existencia = float(input("Ingrese la cantidad en existencia: "))
        precio = float(input("Ingrese el precio del producto: "))
        
        # Le asignamos el IVA predefinido para la categoría elegida
        iva = ivas_por_categoria[categoria]
        print(f"IVA asignado para {categoria}: {iva}%")
        
        # Insertar los datos en la base de datos
        cursor.execute('''INSERT INTO productos (codigo, nombre, categoria, unidad, existencia, precio, iva)
                          VALUES (?, ?, ?, ?, ?, ?, ?)''', (codigo, nombre, categoria, unidad, existencia, precio, iva))
        conn.commit()
        print(f"\nProducto '{nombre}' agregado correctamente.")
    except ValueError:
        print("\nError: Por favor, ingrese un número válido en los campos numéricos.")
    except sqlite3.IntegrityError:
        print(f"\nError: El codigo {codigo} ya existe en la categoría {categoria}. Use un codigo diferente.")

def eliminar_producto():
    """Función para eliminar un producto por su codigo y categoría."""
    print("\n--- ELIMINAR UN PRODUCTO ---")
    try:
        categoria = input("Ingrese la categoría del producto a eliminar: ").capitalize()
        codigo = int(input(f"Ingrese el codigo del producto en la categoría {categoria}: "))
        
        # Buscamos el producto para confirmar antes de eliminar
        cursor.execute("SELECT nombre FROM productos WHERE codigo = ? AND categoria = ?", (codigo, categoria))
        producto_a_eliminar = cursor.fetchone()
        
        if producto_a_eliminar:
            confirmar = input(f"¿Está seguro de que desea eliminar '{producto_a_eliminar[0]}'? (s/n): ").lower()
            if confirmar == 's':
                cursor.execute("DELETE FROM productos WHERE codigo = ? AND categoria = ?", (codigo, categoria))
                conn.commit()
                print(f"\nProducto '{producto_a_eliminar[0]}' eliminado correctamente.")
            else:
                print("Operación cancelada.")
        else:
            print("Producto no encontrado. Revisa la categoría y el codigo.")
    except ValueError:
        print("\nError: Por favor, ingrese un código numérico válido.")

def ver_inventario_completo():
    """Función para ver todos los productos en el inventario."""
    print("\n--- INVENTARIO COMPLETO ---")
    cursor.execute("SELECT * FROM productos ORDER BY categoria, codigo")
    productos = cursor.fetchall()
    
    if not productos:
        print("El inventario está vacío. Vamos a agregar productos.")
    else:
        # Encabezado de la tabla para que se vea ordenado.
        print("-" * 100)
        print(f"{'CÓDIGO':<8} {'NOMBRE':<25} {'CATEGORÍA':<15} {'UNIDAD':<10} {'EXISTENCIA':<10} {'PRECIO':<10} {'IVA (%)':<8}")
        print("-" * 100)
        
        for p in productos:
            # Mostramos los datos de cada producto.
            print(f"{p[0]:<8} {p[1]:<25} {p[2]:<15} {p[3]:<10} {p[4]:<10.2f} ${p[5]:<9.2f} {p[6]:<8.0f}")
        print("-" * 100)

def ver_inventario_por_categoria():
    """Función para ver productos de una categoría específica."""
    print("\n--- VER INVENTARIO POR CATEGORÍA ---")
    categoria_buscada = input("Ingrese la categoría que desea ver: ").capitalize()
    
    cursor.execute("SELECT * FROM productos WHERE categoria = ? ORDER BY codigo", (categoria_buscada,))
    productos = cursor.fetchall()
    
    if not productos:
        print(f"No se encontraron productos en la categoría '{categoria_buscada}'.")
    else:
        print("-" * 100)
        print(f"{'CÓDIGO':<8} {'NOMBRE':<25} {'CATEGORÍA':<15} {'UNIDAD':<10} {'EXISTENCIA':<10} {'PRECIO':<10} {'IVA (%)':<8}")
        print("-" * 100)
        for p in productos:
            print(f"{p[0]:<8} {p[1]:<25} {p[2]:<15} {p[3]:<10} {p[4]:<10.2f} ${p[5]:<9.2f} {p[6]:<8.0f}")
        print("-" * 100)

def crear_factura():
    """Función para generar una factura y actualizar el inventario."""
    print("\n--- CREAR NUEVA FACTURA ---")
    factura_activa = []
    subtotal_factura = 0.0
    iva_total_factura = 0.0
    
    # Definimos la lista de categorías válidas para la caja
    categorias_validas = ['Lacteos', 'Carnicos', 'Limpieza', 'Otros']

    while True:
        # Validamos que la categoría sea una de las opciones permitidas
        while True:
            categoria_producto = input(f"Ingrese la categoría del producto ({', '.join(categorias_validas)} o '0' para terminar): ").capitalize()
            if categoria_producto == '0':
                break
            if categoria_producto in categorias_validas:
                break
            else:
                print("Categoría no válida. Por favor, elija una de la lista.")

        if categoria_producto == '0':
            break

        codigo_producto = input(f"Ingrese el código del producto en la categoría {categoria_producto}: ")

        try:
            codigo = int(codigo_producto)
            cursor.execute("SELECT * FROM productos WHERE codigo = ? AND categoria = ?", (codigo, categoria_producto))
            producto = cursor.fetchone()

            if producto:
                # Extraemos los datos del producto
                nombre, unidad, existencia, precio, iva_porcentaje = producto[1], producto[3], producto[4], producto[5], producto[6]
                
                # Pedimos la cantidad según la unidad de medida
                cantidad_solicitada_str = input(f"¿Cuántos {unidad} de {nombre} va a llevar?: ")
                try:
                    cantidad_solicitada = float(cantidad_solicitada_str)

                    if cantidad_solicitada <= 0:
                        print("La cantidad debe ser mayor a cero.")
                        continue

                    # Verificar si hay suficiente stock
                    if cantidad_solicitada > existencia:
                        print(f"\nNo hay suficiente stock.")
                        print(f"Stock disponible de {nombre}: {existencia} {unidad}")
                        continue
                    
                    # Calcular los valores para la factura
                    precio_total_sin_iva = precio * cantidad_solicitada
                    iva_del_producto = precio_total_sin_iva * (iva_porcentaje / 100)
                    total_con_iva = precio_total_sin_iva + iva_del_producto

                    # Agregar a la lista de la factura
                    factura_activa.append({
                        'nombre': nombre,
                        'cantidad': cantidad_solicitada,
                        'unidad': unidad,
                        'precio_unitario': precio,
                        'iva_individual': iva_del_producto,
                        'total_con_iva': total_con_iva
                    })

                    # Sumar a los totales de la factura
                    subtotal_factura += precio_total_sin_iva
                    iva_total_factura += iva_del_producto

                    # Actualizar el stock en la base de datos
                    nueva_existencia = existencia - cantidad_solicitada
                    cursor.execute("UPDATE productos SET existencia = ? WHERE codigo = ? AND categoria = ?", (nueva_existencia, codigo, categoria_producto))
                    conn.commit()

                    print(f"Producto '{nombre}' agregado a la factura. Stock actualizado.")
                
                except ValueError:
                    print("Error: Por favor, ingrese una cantidad numérica válida.")

            else:
                print("Producto no encontrado. Revisa la categoría y el código.")
        
        except ValueError:
            print("Error: Por favor, ingrese un código numérico.")

    # Imprimir la factura final
    print("\n" + "*" * 40)
    print("          FACTURA GENERADA")
    print("*" * 40)
    print(f"Fecha y Hora: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("-" * 40)
    
    if not factura_activa:
        print("La factura está vacía. Vuelve a intentar.")
    else:
        for item in factura_activa:
            print(f"- {item['nombre']}: {item['cantidad']:.2f} {item['unidad']} a ${item['precio_unitario']:.2f} c/u")
            print(f"  IVA: ${item['iva_individual']:.2f} | Total del ítem: ${item['total_con_iva']:.2f}")
    
    print("-" * 40)
    print(f"Subtotal: ${subtotal_factura:.2f}")
    print(f"Total IVA: ${iva_total_factura:.2f}")
    print("=" * 40)
    gran_total = subtotal_factura + iva_total_factura
    print(f"GRAN TOTAL: ${gran_total:.2f}")
    print("=" * 40)
    print("Gracias por su compra. Vuelva pronto.")


def menu_principal():
    """El menú principal del programa."""
    crear_tabla_productos() # Aseguramos que la tabla exista
    while True:
        print("\n" + "=" * 40)
        print("    SISTEMA DE GESTIÓN DE SUPERMERCADO")
        print("=" * 40)
        print("1. Agregar un nuevo producto al inventario")
        print("2. Ver inventario completo")
        print("3. Ver inventario por categoría")
        print("4. Crear una factura (ir a la caja)")
        print("5. Eliminar un producto")
        print("6. Salir")
        
        opcion = input("Ingrese su opción: ")
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            ver_inventario_completo()
        elif opcion == '3':
            ver_inventario_por_categoria()
        elif opcion == '4':
            crear_factura()
        elif opcion == '5':
            eliminar_producto()
        elif opcion == '6':
            print("\nSaliendo del programa. Adiós.")
            break
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

# ¡Iniciamos el programa!
if __name__ == "__main__":
    menu_principal()

# Cerramos la conexión a la base de datos al finalizar.
conn.close()
