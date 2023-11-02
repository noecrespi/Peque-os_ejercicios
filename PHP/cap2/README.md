# Agenda telefónica

Debes programar una aplicación para mantener una pequeña agenda en una única página web programada en PHP.

La agenda almacenará únicamente dos datos de cada persona: su nombre y un número de teléfono. Además, no podrá haber nombres repetidos en la agenda.

En la parte superior de la página web debe figurar un sencillo formulario con dos cuadros de texto, uno para el nombre y otro para el número de teléfono. En la parte inferior se mostrará el contenido de la agenda. .

Cada vez que se envíe el formulario:

Si el nombre está vacío, se mostrará una advertencia.
Si el nombre que se introdujo no existe en la agenda, y el número de teléfono no está vacío, se añadirá a la agenda.
Si el nombre que se introdujo ya existe en la agenda y se indica un número de teléfono, se sustituirá el número de teléfono anterior.
Si el nombre que se introdujo ya existe en la agenda y no se indica número de teléfono, se eliminará de la agenda la entrada correspondiente a ese nombre.
No se puede utilizar cookies, sesiones, ficheros o bases de datos, para guardar los datos de la agenda.

El script se denominará 'agenda.php' y se guardará en nuestro repositorio bajo la carpeta "entregables_moodle", que crearemos en la raíz del repo, si aún no existe.



INSTRUCCIONES DE ENVÍO
Se enviará un único fichero zip conteniendo una copia del proyecto. Este fichero se nombrará de acuerdo con el siguiente convenio de denominación:

apel1_apel2_nom_agenda.zip

Asegúrate que el nombre no contenga la letra ñ, espacios, tildes ni caracteres especiales extraños. Así, por ejemplo, la alumna Begoña Sánchez Mañas, debería nombrar esta tarea como...

                                             sanchez_manas_begona_agenda.zip

Este fichero contendrá el fichero 'agenda.php' y un 'README.md' en donde se incluirá cualquier información que sea útil para el evaluador: usuario y contraseña si fuese necesario, fallos conocidos del script, apartados omitidos, etc.

CRITERIOS DE EVALUACIÓN
Criterio 1 (Máximo 1 punto. Ponderación 1)
Último commit está dentro del plazo de entrega:
No 0 puntos
No 1 punto
Criterio 2 (Máximo 3 puntos. Ponderación 1)
Sobre el seguimiento de los convenios de denominación.

Orientaciones:

No: 0 puntos
No en todos los apartados, de una manera desigual: de 1 a 2 puntos.
Totalmente: 3 puntos
Criterio 3 (Máximo 5 puntos, ponderación 1)
Sobre la documentación del código fuente:

El código está documentado de modo que es fácil de comprender: de 0 a 2 puntos.
Sigue las directrices del documentador PHPDoc. de 0 a 3 puntos.
Criterio 4 (Máximo 8 puntos. Ponderación 6)
Se valorará con un punto la consecución de cada uno de los siguientes ítems:

Generar el formulario de introducción de nuevo contacto.
Introducir los datos de la agenda como campos ocultos en el formulario.
Comprobar los datos enviados por el formulario, mostrando una advertencia cuando no se rellena el nombre.
Mostrar los contactos existentes en la agenda.
Introducir en la agenda los datos de un nuevo contacto.
Modificar el teléfono de un contacto ya existente.
Eliminar de la agenda un contacto.
Utilizar un array asociativo para guardar los datos de la agenda.
Criterio 5 (Máximo 2 puntos. Ponderación 1)
Subida al classroom.github

(0 puntos) No se ha subido al repositorio 'php_basico' del classroom.github.
(1 a 2 puntos) Se ha subido al repositorio indicado.
Criterio 6 (Máximo 3 puntos. Ponderación 2)
Despliegue en remoto
(0 puntos) No se despliega en remoto
(1 punto) El código se ha descargado del github, pero no se ejecuta correctamente.
(2 puntos) Se ha creado un virtualHost que ejecuta el script con el enlace moodle.nomcorporativo.randion.es/agenda.php
