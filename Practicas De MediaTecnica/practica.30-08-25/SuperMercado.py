import sqlite3
import datetime

# ¡Aquí vamos a hacer la base de datos!
conn = sqlite3.connect('supermercado.db')
cursor = conn.cursor()

# ¡Estas son las tasas de IVA de Colombia! El 19% es el normal, el 5% es para cositas especiales.
iva_lacteos = 0.05
iva_bebidas = 0.19
iva_carnicos = 0.05
iva_limpieza = 0.19
iva_otros = 0.19

def calcular_iva(categoria, precio):
    """Calcula el precio con IVA y el porcentaje de IVA aplicado."""
    if categoria == 'Lacteos':
        iva_rate = iva_lacteos
    elif categoria == 'Bebidas':
        iva_rate = iva_bebidas
    elif categoria == 'Carnicos':
        iva_rate = iva_carnicos
    elif categoria == 'Limpieza':
        iva_rate = iva_limpieza
    else:
        iva_rate = iva_otros
    
    precio_con_iva = precio * (1 + iva_rate)
    return precio_con_iva, iva_rate * 100

def insertar_producto(nombre, categoria, precio):
    """Inserta un nuevo producto en la base de datos."""
    precio_con_iva, porcentaje_iva = calcular_iva(categoria, precio)
    cursor.execute(
        '''INSERT INTO productos (nombre, categoria, precio_sin_iva, precio_con_iva, porcentaje_iva)
           VALUES (?, ?, ?, ?, ?)''', (nombre, categoria, precio, precio_con_iva, porcentaje_iva))
    conn.commit()

def poblar_base_de_datos():
    """Borra la tabla y la vuelve a crear para que esté perfecta cada vez que empezamos."""
    cursor.execute("DROP TABLE IF EXISTS productos")
    print("¡Base de datos lista para empezar de nuevo! ✨")
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    categoria TEXT,
                    precio_sin_iva REAL,
                    precio_con_iva REAL,
                    porcentaje_iva REAL)''')
    
    products_to_add = [
        # Cárnicos (IVA 5%) - ¡Se venden por kilos!
        ('Carne de res', 'Carnicos', 15000),
        ('Pechuga de pollo', 'Carnicos', 12000),
        ('Salchichas', 'Carnicos', 8500),
        ('Costillas de cerdo', 'Carnicos', 18000),
        ('Chorizo', 'Carnicos', 7000),
        ('Lomo de cerdo', 'Carnicos', 17500),
        ('Pescado Tilapia', 'Carnicos', 11000),
        ('Jamón', 'Carnicos', 9800),
        ('Filete de pescado', 'Carnicos', 14500),
        ('Carne molida', 'Carnicos', 13000),

        # Lácteos (IVA 5%) - ¡Unidades!
        ('Leche entera', 'Lacteos', 4500),
        ('Yogurt de fresa', 'Lacteos', 2800),
        ('Queso costeño', 'Lacteos', 6000),
        ('Mantequilla', 'Lacteos', 5200),
        ('Avena en leche', 'Lacteos', 3100),
        ('Crema de leche', 'Lacteos', 4800),
        ('Cuajada', 'Lacteos', 5500),
        ('Kumys', 'Lacteos', 2900),
        ('Queso mozarella', 'Lacteos', 7000),
        ('Leche deslactosada', 'Lacteos', 4800),

        # Bebidas (IVA 19%) - ¡Litros!
        ('Coca-Cola 2L', 'Bebidas', 6500),
        ('Sprite 1.5L', 'Bebidas', 5800),
        ('Postobón Uva', 'Bebidas', 5000),
        ('Colombiana 3L', 'Bebidas', 8000),
        ('Jugo Hit', 'Bebidas', 2500),
        ('Agua con gas', 'Bebidas', 2000),
        ('Gaseosa Naranja', 'Bebidas', 4500),
        ('Té Hatsu', 'Bebidas', 3200),
        ('Gaseosa Limón', 'Bebidas', 4200),
        ('Gaseosa Manzana', 'Bebidas', 5100),

        # Limpieza (IVA 19%) - ¡Unidades!
        ('Detergente en polvo', 'Limpieza', 18000),
        ('Blanqueador 1L', 'Limpieza', 5000),
        ('Jabón de barra', 'Limpieza', 3000),
        ('Limpiador de pisos', 'Limpieza', 12000),
        ('Ambientador', 'Limpieza', 7500),
        ('Papel higiénico x4', 'Limpieza', 8500),
        ('Desinfectante', 'Limpieza', 10500),
        ('Lavaloza', 'Limpieza', 6000),
        ('Toallas de cocina', 'Limpieza', 9000),
        ('Cloro 2L', 'Limpieza', 8500),

        # Otros (IVA 19%) - ¡Unidades!
        ('Pan tajado', 'Otros', 4000),
        ('Arroz 1kg', 'Otros', 3500),
        ('Pasta', 'Otros', 2500),
        ('Azúcar 500g', 'Otros', 2200),
        ('Aceite 1L', 'Otros', 11000),
        ('Café 500g', 'Otros', 15000),
        ('Frijoles 500g', 'Otros', 3800),
        ('Lentejas 500g', 'Otros', 3000),
        ('Sal 500g', 'Otros', 1500),
        ('Harina de trigo', 'Otros', 3300)
    ]
    for producto in products_to_add:
        insertar_producto(producto[0], producto[1], producto[2])
    print("¡Inventario cargado! ¡Ya podemos empezar a vender! 🛒")

def mostrar_productos_por_categoria(categoria):
    """Muestra los productos de una categoría para que el cliente elija."""
    print("\n" + "=" * 40)
    print(f"Productos en la categoría: {categoria.upper()}")
    print("=" * 40)
    cursor.execute("SELECT id, nombre FROM productos WHERE categoria = ?", (categoria,))
    resultados = cursor.fetchall()
    
    if resultados:
        for fila in resultados:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}")
    else:
        print("Uy, no encontré productos en esta categoría. 🤔")
    print("=" * 40)
    return resultados

def obtener_detalle_producto(id_producto):
    """Busca y trae toda la información de un producto por su ID."""
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    return cursor.fetchone()

### **¡Aquí empieza la caja registradora!**
def caja_registradora():
    """Este es el menú para empezar a hacer una factura."""
    poblar_base_de_datos()
    
    factura_activa = []
    subtotal_factura = 0.0
    iva_total_factura = 0.0

    print("\n" + "=" * 40)
    print("       ¡BIENVENIDO AL SUPERMERCADO! 🏪")
    print("       ¡Vamos a generar una nueva factura!")
    print("=" * 40)

    while True:
        print("\nCategorías disponibles: Carnicos, Lacteos, Bebidas, Limpieza, Otros")
        categoria_buscada = input("Ingrese la categoría del producto (o 'terminar' para finalizar la factura): ").capitalize()

        if categoria_buscada.lower() == 'terminar':
            break

        productos_encontrados = mostrar_productos_por_categoria(categoria_buscada)
        
        if productos_encontrados:
            try:
                eleccion_producto = input("Ingrese el ID del producto que va a llevar: ")
                id_producto = int(eleccion_producto)
                
                detalle = obtener_detalle_producto(id_producto)
                
                if detalle:
                    nombre, categoria, precio_sin_iva, precio_con_iva, porcentaje_iva = detalle[1], detalle[2], detalle[3], detalle[4], detalle[5]
                    
                    unidad_medida = 'unidades'
                    if categoria == 'Carnicos':
                        unidad_medida = 'kilos'
                    elif categoria == 'Bebidas':
                        unidad_medida = 'litros'

                    cantidad_str = input(f"¿Cuántos {unidad_medida} va a llevar de {nombre}?: ")
                    try:
                        cantidad = float(cantidad_str)
                        if cantidad <= 0:
                            print("¡Ups! La cantidad debe ser mayor a cero. 🤔")
                            continue
                        
                        precio_total_producto = precio_sin_iva * cantidad
                        precio_total_con_iva = precio_con_iva * cantidad
                        iva_del_producto = precio_total_con_iva - precio_total_producto

                        subtotal_factura += precio_total_producto
                        iva_total_factura += iva_del_producto

                        factura_activa.append({
                            'nombre': nombre,
                            'cantidad': cantidad,
                            'unidad': unidad_medida,
                            'precio_sin_iva': precio_sin_iva,
                            'iva_individual': iva_del_producto,
                            'total_con_iva': precio_total_con_iva
                        })
                        print("¡Listo! Artículo agregado a la factura. ✅")

                    except ValueError:
                        print("¡Oh no! Ingresa un número válido para la cantidad. 😅")
                else:
                    print("¡Ese ID no existe! Revisa bien la lista. 🧐")

            except ValueError:
                print("¡Oh no! Ingresa un número válido para el ID. 😅")
        
        # Le doy la opción de seguir agregando o terminar
        continuar = input("¿Quiere agregar otro producto? (s/n): ").lower()
        if continuar == 'n':
            break

    # Imprimir la factura final
    print("\n" + "*" * 40)
    print("          ¡FACTURA GENERADA! 🧾")
    print("*" * 40)
    print(f"Fecha y Hora: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("-" * 40)
    
    if not factura_activa:
        print("¡La factura está vacía! ¡Vuelve pronto!")
    else:
        for item in factura_activa:
            print(f"{item['nombre']} - Cantidad: {item['cantidad']} {item['unidad']}")
            print(f"  Precio sin IVA: ${item['precio_sin_iva']:.2f} / Total: ${item['total_con_iva']:.2f}")
    
    print("-" * 40)
    print(f"Subtotal: ${subtotal_factura:.2f}")
    print(f"Total IVA: ${iva_total_factura:.2f}")
    print("=" * 40)
    gran_total = subtotal_factura + iva_total_factura
    print(f"GRAN TOTAL: ${gran_total:.2f}")
    print("=" * 40)
    print("¡Gracias por su compra! ¡Vuelva pronto! 👋")

# Iniciar el programa de la caja registradora
if __name__ == "__main__":
    caja_registradora()

# Cerrar la conexión al salir del programa
conn.close()