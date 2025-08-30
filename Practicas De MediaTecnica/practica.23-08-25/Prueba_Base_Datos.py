import sqlite3

conn = sqlite3.connect('mi_base_de_datos.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS empleados
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                email TEXT)''')

def insertarempleado(nombre, email):
    cursor.execute(
        ''' INSERT INTO  empleados (nombre, email) VALUES (?, ?) ''', (nombre,email))
    conn.commit()

insertarempleado('Maria', 'maria@gmail.com')
print("- ")
insertarempleado('samuel', 'samuel@gmail.com')

def imprimirResultado():
    print('*' * 25)
    cursor.execute("SELECT * FROM empleados")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    
imprimirResultado()

def actualizarempleado(email, nombre):
    cursor.execute(
        ''' update empleados SET email = ? WHERE nombre = ? ''', (email, nombre))
    conn.commit()

actualizarempleado('nuevoemail@ffff.com', 'Maria')

imprimirResultado()

def eliminarEmpleado(nombreEliminar):
    cursor.execute(
        ''' delete from empleados WHERE nombre = ? ''', (nombreEliminar,))
    conn.commit()

eliminarEmpleado('Maria')

conn.close()