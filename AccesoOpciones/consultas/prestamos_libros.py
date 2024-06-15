
# Importamos la biblioteca sqlite3 para trabajar con la base de datos

import sqlite3

# Definimos una funcion para poder usarla en el codigo original

def prestamos_libros():

    # Conectamos con la base de dartos y le damos el nombre "prestamos_libros"

    with sqlite3.connect("C:/Users/POWER/Libros.db") as prestamos_libros:
        
        try:

            # Generamos un cursor para manejar la base de datos

            consulta_cursor = prestamos_libros.cursor()

            # Solicitamos al usuario que ingrese la fecha de prestamo

            fecha_prestamo = str(input("ingresa la fecha de prestamo en el formato (DD-MM-YY): "))

            # Solicitamos al usuario que ingrese la fecha de devolucion

            fecha_devolucion = str(input("ingresa una fecha de devolucion en el formato (DD-MM-YY)"))

            # Solicitamos al usuario que ingrese el nombre del propietario

            nombre_propietario = str(input("ingresa el nombre del propietario: "))

            # Solicitamos al usuario que ingrese el titulo del libro

            titulo_libro = str(input("Ingresa el nombre del libro: "))

            # Con el cursor y el metodo execute, seleccionamos el campo "LibroID" de la "Tabla_libros" y con la condicion establecemos la key foranea a "TituloLibro"

            consulta_cursor.execute("SELECT LibroID FROM Tabla_libros WHERE TituloLibro = ?",(titulo_libro,))

            # Con una nueva variable llamada "Libro" y el metodo fetchone, accedemos a una sola fila que es "TituloLibro"

            libro = consulta_cursor.fetchone()

            # Usamos una condicion que pase en la variable anterior 

            if libro:

                # Generamos una nueva variable que almacena el "libro_id" obtenido

                libro_id = libro[0]

                # Realizamos la consulta que inserta en "Prestados" los parametros antes propuestos con el "LibroID"

                consulta_cursor.execute("INSERT INTO Prestados (LibroID,FechaPrestamo,FechaDevolucion,NombrePropietario ) VALUES (?,?,?,?)",(libro_id,fecha_prestamo,fecha_devolucion,nombre_propietario))

                # Subimos los cambios a la base de datos

                prestamos_libros.commit()

                # Mensaje de exito

                print("Datos ingresados correctamente")

        # Manejo de Excepcion de un error en la base de datos

        except ValueError as value:

            print(f"Los datos no se pueden ingresar: {value}")
