
# Importamos la biblioteca sqlite3 para trabajar con la base de datos

import sqlite3

# Definimos una funcion para poder usarla en el codigo original

def ejemplar_estado():

    # Conectamos con la base de dartos y le damos el nombre "ejemplar_estado"

    with sqlite3.connect("C:/Users/POWER/Libros.db") as ejemplar_estado:

        try:

            # Generamos un cursor para manejar la base de datos

            consulta_cursor = ejemplar_estado.cursor()

            # Solicitamos al usuario que ingrese el titulo del libro

            titulo_libro = str(input("ingresa el titulo del libro: "))

            # Solicitamos al usuario que ingrese el estado del libro

            estado_libro = str(input("ingresa el estado del libro: "))

            # Solicitamos al usuario que ingrese el nombre del autor

            nombre_autor = str(input("ingresa el nombre del autor: "))

            # Con el cursor y el metodo execute, seleccionamos el campo "AutorID" de la tabla "DatosAutor" y con la condicion establecemos la clave foranea a "nombre_autor"

            consulta_cursor.execute("SELECT AutorID FROM DatosAutor WHERE NombreAutor = ?",(nombre_autor,))

            # Con una nueva variable llamada "autor" y el metodo fetchone, accedemos a una sola fila que es "NombreAutor"

            autor = consulta_cursor.fetchone()

            # Usamos una condicion que pase en la variable anterior 

            if autor:

                # Generamos una nueva variable que almacena el "AutorID" obtenido

                autor_id = autor[0]

                # Realizamos la consulta que inserte a "Tabla_Libros" los parametros antes propuestos junto con el del "AutorID"

                consulta_cursor.execute("INSERT INTO Tabla_libros (TituloLibro,AutorID,Estado) VALUES (?,?,?)",(titulo_libro, autor_id,estado_libro))

                # Subimos los cambios a la base de datos

                ejemplar_estado.commit()

                # Mensaje de exitp

                print("Titulo del libro y estado agregados correctamente")

            else:

                # Manejo de exepcion si no se encuentra un autor

                print("Autor no encontrado")
        
        # Manejo de excepcion si se encuentra un erroor en las entradas del usuario

        except ValueError as value:

            print(f"no es una entrada valida: {value}")