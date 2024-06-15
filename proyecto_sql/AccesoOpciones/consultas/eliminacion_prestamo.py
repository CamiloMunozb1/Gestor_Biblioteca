
# Importamos la biblioteca sqlite3 para trabajar con la base de datos

import sqlite3

# Definimos una funcion para poder usarla en el codigo original

def eliminacion_prestamo():

    # Conectamos con la base de dartos y le damos el nombre "eliminacion_prestamo"

    with sqlite3.connect("C:/Users/POWER/Libros.db") as elimiminacion_prestamo:

        try:

            # Generamos un cursor para manejar la base de datos

            consulta_cursor = elimiminacion_prestamo.cursor()

            # Solicitamos al usuario que ingrese el nombre del ID libro a eliminar

            eliminar_prestamo = int(input("Ingrese el ID del prestamo: "))

            # Con el cursor y el metodo execute, ingresamos la consulta que elimina de "Prestados" el prestamo que se desea realizar

            consulta_cursor.execute("DELETE FROM Prestados WHERE PrestamoID = ?",(eliminar_prestamo,))

            # Subimos los cambios a la base de datos

            elimiminacion_prestamo.commit()

            # Mensaje de  exito

            print("Registro eliminado con exito")

        # Manejo de Excepcion de un error en la base de datos

        except ValueError as value:
            
            print(f"La entrada no es valida {value}")