
# Importamos biblioteca sqlite3 para trabajar con la base de datos SQL

import sqlite3

# Definimos una funcion para poder usarla en el codigo original

def ingreso_autor():

    # Conectamos con la base de datos y le damos el nombre "ingreso_autor"

    with sqlite3.connect("C:/Users/POWER/Libros.db") as ingreso_autor:

        try:

            # Generamos un cursor para manejar la base de datos

            consulta_cursor = ingreso_autor.cursor() 

            # Se le pide al usuario que ingrese el nombre de autor

            nombre_autor = str(input("ingresa el nombre del autor: "))

            # Con el cursor y el metodo execute, ingresamos la consulta que inserta a la tabla "DatosAutor" y al campo "NombreAutor" un valor que es la entrada del usuario

            consulta_cursor.execute("INSERT INTO DatosAutor (NombreAutor) VALUES (?) ", (nombre_autor,))

            # Con el modulo commit, subimos los cambios a la base de datos

            ingreso_autor.commit()

            # Mensaje de exito 

            print("Autor agregado correctamente")
        
        # Manejo de excepciones si el usuario no ingresa una opcion valida

        except ValueError as value:

            print(f"no es una entrada valida: {value}")
        
        # Manejo de excepciones si se presenta un error en la base de datos

        except sqlite3.Error as error:

            print(f"No es valida la entrada: {error}")



