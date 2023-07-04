# Requisitos Ejercicio 4

1. - En la vista de Listado:

    Agrega los elementos o campos necesarios dentro de un formulario. OK
    Considera los campos que permitan realizar un filtro sobre los registros de las tareas pendientes del usuario actual.OK
    Asegúrate de que los registros correspondientes, como las etiquetas, estén cargados correctamente.
    Determina las columnas que consideres convenientes para la tabla. OK

2. - Genera una vista de Creación de Tareas:

    Presenta los datos del formulario correspondiente en esta vista. OK
    Incluye una lista desplegable para seleccionar la etiqueta a la que corresponde la tarea. OK
    Asegúrate de que esta vista comparta el mismo template que la vista de Edición de Tareas. OK

3. - Implementa la funcionalidad de guardar un nuevo registro de Tarea en la vista de Creación:

    Realiza la validación de los datos tanto en el template como en el formulario antes de guardar. OK
    Después de guardar exitosamente, redirecciona al usuario a la vista de Listado. OK
    Asegúrate de que el nuevo registro se refleje correctamente en la vista de Listado. OK

4. - Realiza modificaciones en el modelo y migraciones:

    Añade un nuevo campo de texto grande para que los usuarios puedan registrar observaciones sobre la tarea.OK
    Asegúrate de realizar la migración correspondiente para actualizar el modelo en la base de datos. OK

4. a. En relacion ha la migracion, se ejecuto el siguiente comando:

```bash
python manage.py makemigrations
```
Debido a que desde un inicio plantee el modelo con el campo observaciones, no fue necesario realizar la modificacion del mismo.
De haber sido necesario, se hubiera ejecutado el siguiente comando:

```bash
python manage.py migrate
```

