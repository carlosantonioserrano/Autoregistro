import mysql.connector
# importarmos el conector

# Iniciamos un try
try:
    #creamos la variable conn que es la conexion de mysql
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='', port='')

except Exception as err:
    print('ERROR al conectar a la base de datos')

else:
    print('CONEXION A LA BDD SATISFACTORIA')

# creamos un cursor
cursor = conn.cursor()

# creeamos la query
sql = "SELECT * FROM empleados WHERE dui = '123457' "

# ejecutamos la query
cursor.execute(sql)

# guardo la consulta en una variable llamada datos con el metodo fecthall
datos = cursor.fetchall()

#para recorrer la consulta uso for
for fila in datos:
    print(fila)

# cerramos la conexion
conn.close()
