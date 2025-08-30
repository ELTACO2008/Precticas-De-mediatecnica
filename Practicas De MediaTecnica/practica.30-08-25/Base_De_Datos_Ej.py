import sqlite3

con = sqlite3.connect("tienda.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, precio REAL)")

cur.execute("INSERT INTO productos (nombre, precio) VALUES ('camiseta', 25000)")
cur.execute("INSERT INTO productos (nombre, precio) VALUES ('zapatos', 80000)")
con.commit()

cur.execute("SELECT * FROM productos")
print(cur.fetchall())

con.close()