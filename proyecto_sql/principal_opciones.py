# Importamos biblioteca sqlite3 para trabajar con la base de datos SQL

import sqlite3

# Importamos la primera consulta para ingresar el nombre de un autor

from AccesoOpciones.consultas.ingreso_autor import ingreso_autor

# Importamos la segunda consulta para ingresar un nuevo libro y su estado fisico

from AccesoOpciones.consultas.ejemplar_estado import ejemplar_estado

# Importamos la tercera consulta para ingresar los datos de los prestamos de un libro

from AccesoOpciones.consultas.prestamos_libros import prestamos_libros

# Importamos la cuarta consulta para elimimar el titulo de un libro

from AccesoOpciones.consultas.eliminacion_libros import eliminacion_libros

# Importamos la quinta consulta para eliminar los datos de un prestamo
from AccesoOpciones.consultas.eliminacion_prestamo import eliminacion_prestamo


while True:

    # Menu de opciones para el usuario

    print("""
        BIENVENIDO A SU LIBRERIA PERSONAL
        ESCOJA UNA OPCION:
        1. Ingrese un autor nuevo
        2. Ingrese un ejemplar nuevo y su estado
        3. Ingrese los datos de un prestamo
        4. Eliminar un libro
        5. Eliminar un registro de prestamo
        6. Salir
        """)
    try:

        # Se pide un ingreso al usuario

        usuario_inout = int(input("ingresa una opcion: "))

        # Se valida la entrada del usuario y la opcion elegida posterior ejecuta la primera cpnsulta

        if usuario_inout == 1:
            ingreso_autor()

        # Se valida la entrada del usuario y la opcion elegida posterior ejecuta la segunda consulta

        elif usuario_inout == 2:
            ejemplar_estado()

        # Se valida la entrada del usuario y la opcion elegida posterior ejecuta la tercera consulta

        elif usuario_inout == 3:
            prestamos_libros()
        
        # Se valida la entrada del usuario y la opcion elegida posterior ejecuta la cuarta consulta

        elif usuario_inout == 4:
            eliminacion_libros()

        # Se valida la entrada del usuario y la opcion elegida posterior ejecuta la quinta consulta

        elif usuario_inout == 5:
            eliminacion_prestamo()

        # Se valida la entrada del usuario y la opcion elegida y sale del programa 

        elif usuario_inout == 6:

            # Mensaje de despedida del programa y sale de este

            print("Gracias por usar su biblioteca personal")
            break
    
    # Manejo de excepciones si el usuario no ingresa una opcion valida

    except ValueError:

        # Mensaje de error

        print("La entrada es incorrecta")
    
    # Manejo de excepciones si se presenta un error en la base de datos

    except sqlite3.Error as error:
        print(f"error en la base de datos {error}")




