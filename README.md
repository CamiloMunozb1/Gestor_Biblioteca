# Biblioteca Personal
Este proyecto es un sistema de gestión de una biblioteca personal que utiliza SQLite como base de datos y Python para la lógica del programa. Permite a los usuarios gestionar autores, libros y registros de préstamos.

# Requisitos
Pitón 3.x
Biblioteca sqlite3(incluida en la biblioteca estándar de Python)

# Funcionalidades
1. Ingrese un autor nuevo : Permite al usuario ingresar un nuevo autor en la base de datos.
2. Ingrese un ejemplar nuevo y su estado : Permite al usuario ingresar un nuevo libro junto con su estado físico.
3. Ingrese los datos de un préstamo : Permite al usuario registrar los datos de un préstamo de un libro.
4. Eliminar un libro : Permite al usuario eliminar un libro de la base de datos.
5. Eliminar un registro de préstamo : Permite al usuario eliminar un registro de préstamo.
6. Salir : Cierra el sistema de gestión de la biblioteca.

# manejo de errores
El sistema maneja dos tipos principales de errores:
1. ValueError : Cuando la entrada del usuario no es válida (no es un número).
2. sqlite3.Error : Cualquier error relacionado con la base de datos SQLite.

# Contribuir
Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:
1. Haz un fork del repositorio.
2. Crea una rama para tu característica o corrección de errores ( git checkout -b feature/nueva-caracteristica).
3. Realiza tus cambios y confirma tus commits ( git commit -am 'Agrega nueva característica').
4. Sube tu rama ( git push origin feature/nueva-caracteristica).
5. Abra una solicitud de extracción.

# licencia
Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo LICENSEpara más detalles.
