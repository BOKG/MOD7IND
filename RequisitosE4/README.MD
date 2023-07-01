# Requisitos Ejercicio 4

1. - En la vista de Listado:

    Agrega los elementos o campos necesarios dentro de un formulario.
    Considera los campos que permitan realizar un filtro sobre los registros de las tareas pendientes del usuario actual.
    Asegúrate de que los registros correspondientes, como las etiquetas, estén cargados correctamente.
    Determina las columnas que consideres convenientes para la tabla.

2. - Genera una vista de Creación de Tareas:

    Presenta los datos del formulario correspondiente en esta vista.
    Incluye una lista desplegable para seleccionar la etiqueta a la que corresponde la tarea.
    Asegúrate de que esta vista comparta el mismo template que la vista de Edición de Tareas.

3. - Implementa la funcionalidad de guardar un nuevo registro de Tarea en la vista de Creación:

    Realiza la validación de los datos tanto en el template como en el formulario antes de guardar.
    Después de guardar exitosamente, redirecciona al usuario a la vista de Listado.
    Asegúrate de que el nuevo registro se refleje correctamente en la vista de Listado.

4. - Realiza modificaciones en el modelo y migraciones:

    Añade un nuevo campo de texto grande para que los usuarios puedan registrar observaciones sobre la tarea.
    Asegúrate de realizar la migración correspondiente para actualizar el modelo en la base de datos.