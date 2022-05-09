import mysql.connector
# importarmos el conector

# Iniciamos un try
try:
    #creamos la variable conexion de mysql
    conexion = mysql.connector.connect(user='root', password='Pass123', host='localhost', database='empresa', port='3306')

except Exception as err:
    print('ERROR al conectar a la base de datos')

else:
    print('CONEXION A LA BDD SATISFACTORIA')

# creamos un cursor
cursor = conexion.cursor()

# creeamos la query
sql = "INSERT INTO empleados(nombres, apellidos, dui) VALUES('Will', 'Smith', '0123458')"

# ejecutamos la query
cursor.execute(sql)

# actualizamos la BDD
conexion.commit()

# cerramos la conexion
conexion.close()
