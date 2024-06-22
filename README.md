# Biblioteca Personal
Este proyecto es un sistema de gestión de una biblioteca personal que utiliza SQLite como base de datos y Python para la lógica del programa. Permite a los usuarios gestionar autores, libros y registros de préstamos.

# Requisitos
Pitón 3.x
Biblioteca sqlite3(incluida en la biblioteca estándar de Python)

# Funcionalidades
Ingrese un autor nuevo : Permite al usuario ingresar un nuevo autor en la base de datos.
Ingrese un ejemplar nuevo y su estado : Permite al usuario ingresar un nuevo libro junto con su estado físico.
Ingrese los datos de un préstamo : Permite al usuario registrar los datos de un préstamo de un libro.
Eliminar un libro : Permite al usuario eliminar un libro de la base de datos.
Eliminar un registro de préstamo : Permite al usuario eliminar un registro de préstamo.
Salir : Cierra el sistema de gestión de la biblioteca.

# manejo de errores
El sistema maneja dos tipos principales de errores:
ValueError : Cuando la entrada del usuario no es válida (no es un número).
sqlite3.Error : Cualquier error relacionado con la base de datos SQLite.

# Contribuir
Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:
Haz un fork del repositorio.
Crea una rama para tu característica o corrección de errores ( git checkout -b feature/nueva-caracteristica).
Realiza tus cambios y confirma tus commits ( git commit -am 'Agrega nueva característica').
Sube tu rama ( git push origin feature/nueva-caracteristica).
Abra una solicitud de extracción.

# licencia
Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo LICENSEpara más detalles.
