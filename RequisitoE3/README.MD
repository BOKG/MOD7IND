# Requisitos Ejercicio 3

- Desde la administración de Django, agrega registros para las Etiquetas que sean estrictamente
necesarias de acuerdo a la historia del proyecto. OK

- Genera una vista que listen todas las tareas pendientes del usuario actual, por ahora sin filtrar,
ordenadas por fecha de vencimiento. En la parte superior, considera un botón “Agregar Tarea” con
la que se accederá a la ventana de Creación. Cada tarea tendrá sólo un botón de Ver, que
navegará hasta la vista de Visualización de Tarea. 

- Generar una vista de Visualización de Tarea, en donde se presenten todos los datos relacionados
con la tarea seleccionada. Aquí, en la parte superior y mediante botones, poner las acciones que
están disponibles: Editar la tarea, derivando a la vista de Edición de Tareas; Eliminar, que eliminará
el registro de Tarea (previa confirmación de parte del usuario); Completar, que cambiará el estado
de la tarea; Retornar, que volverá a la vista de Listado.

La vista de Visualización no debe, por ahora, cargar datos.

La vista Listado de todas las tareas pendientes, deberá mostrar los datos que se encuentren registrados
en la base de datos. Si no tuviera datos la tabla correspondiente, podrás agregar directamente en la base
de datos para ver reflejada la lista de tareas.


