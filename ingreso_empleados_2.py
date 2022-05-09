# Desde la terminal descargo el paquete/librería de conexion con la siguiente sentecia:
# pip install mysql-connector-python

import mysql.connector
import datetime

nombres = input("Ingresa tus nombres: ")
apellidos = input('Ingresa tus apellidos: ')
dui = input('Ingresa el número de DUI: ')
fecha_y_hora = datetime.datetime.now()
# para extraer solo la fecha
solo_fecha = datetime.datetime.strftime(fecha_y_hora, '%Y-%m-%d')

# para extraer solo la hora
solo_hora = datetime.datetime.strftime(fecha_y_hora, '%H:%M:%S')

try:
    conexion = mysql.connector.connect(user='root', password='Pass123', host='localhost', database='empresa', port='3306')

except Exception as err:
    print('ERROR al conectar a la base de datos')

cursor = conexion.cursor()

sql = "INSERT INTO empleados(nombres, apellidos, dui, fecha_registro, hora_registro) VALUES (%s, %s, %s, %s, %s);"

# creamos cadena
cadena = (nombres, apellidos, dui, solo_fecha, solo_hora)

cursor.execute(sql, cadena)

# actualizamos la BDD
conexion.commit()

print('Se ha creado un nuevo registro.')