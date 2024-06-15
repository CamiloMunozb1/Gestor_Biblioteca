
# Importamos la biblioteca sqlite3 para trabajar con la base de datos

import sqlite3

# Definimos una funcion para poder usarla en el codigo original

def eliminacion_libros():

    # Conectamos con la base de dartos y le damos el nombre "eliminacion_libro"

    with sqlite3.connect("C:/Users/POWER/Libros.db") as eliminacion_libro:

        try:

            # Generamos un cursor para manejar la base de datos

            consulta_cursor = eliminacion_libro.cursor()

            # Solicitamos al usuario que ingrese el nombre del libro a eliminar

            libro_eliminar = str(input("Ingrese el nombre del libro a eliminar: "))

            # Con el cursor y el metodo execute, ingresamos la consulta que elimina de "Tabla_libros" el libro que se desea eliminar

            consulta_cursor.execute("DELETE FROM Tabla_libros WHERE TituloLibro = ?",(libro_eliminar,))

            # Subimos los cambios a la base de datos

            eliminacion_libro.commit()

            # Mensaje de  exito

            print("Titulo eliminado correctamente")
        
        # Manejo de Excepcion de un error en la base de datos

        except ValueError as value:
            
            print(f"la entrada no es valida: {value}")
