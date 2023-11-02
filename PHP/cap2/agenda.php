<!doctype html>
<html>

<head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <title>Agenda telefónica</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <?php

    /**
     * Inicializa la agenda, si no existe, la crea.
     *
     * Si se encuentra en la URL un parámetro llamado 'agenda', se asigna su valor a la variable $agenda.
     * Si no se encuentra el parámetro, se crea un array vacío y se asigna a $agenda.
     */
    if (isset($_GET['agenda']))
        $agenda = $_GET['agenda'];
    else
        $agenda = array();


    /** 
     * CRUD (Create, Update, Delete)
     * Gestiona la creación, actualización o eliminación de un contacto en la agenda.
     *
     * @param array $agenda El array que almacena la lista de contactos.
     *
     * La función verifica si se ha enviado el formulario para guardar un contacto. Si es así, procesa los datos del formulario
     * para determinar si se debe crear un nuevo contacto, actualizar uno existente o eliminar un contacto. También maneja la validación
     * del campo de nombre y muestra un mensaje de error si el nombre está vacío.
     */
    
    if (isset($_GET['guardar'])) {
        // rescatar los datos del formulario
        $name = filter_input(INPUT_GET, 'nombre', FILTER_SANITIZE_SPECIAL_CHARS);
        $phone = filter_input(INPUT_GET, 'telefono', FILTER_SANITIZE_SPECIAL_CHARS);

        if (empty($name)) { // compruebo si el campo nombre está vacío
            echo "<div style='background-color: rgb(128, 0, 4); text-align: center;'><h5 style='color: white;'>Es obligatorio añadir el nombre</h5></div> <br/>";
        } elseif (empty($phone)) {  // DELETE
            unset($agenda[$name]);
        } else { // CREATE or UPDATE
            $agenda[$name] = $phone;
        }
    }


    /**
     * Imprime la lista de contactos.
     *
     * Esta función recibe un array de agenda de contactos y lo recorre para mostrar cada contacto en formato de nombre y teléfono.
     *
     * @param array $agenda Un array que contiene los contactos de la agenda.
     */
    function printContacts($agenda)
    {
        foreach ($agenda as $name=> $phone) {
            echo "Nombre: $name<br>Teléfono: $phone <br><br>";
        }
    }

    /**
     * Imprime los contactos en campos ocultos del formulario.
     *
     * Esta función toma un array $agenda y genera campos ocultos en un formulario HTML
     * para cada contacto presente en la agenda. Cada campo oculto contendrá el nombre
     * del contacto como índice y su número de teléfono como valor.
     *
     * @param array $agenda El array de contactos a imprimir en campos ocultos.
     */
    function contactsHidden($agenda)
    {
        foreach ($agenda as $name=> $phone) {
            echo '<input type="hidden" name="agenda[' . $name. ']" ';
            echo 'value="' . $phone . '"/>';
        }
    }
    ?>

    <header>
        <h1>Agenda telefónica</h1>
    </header>

    <main>
        <!-- Formulario para añadir contactos -->
        <form>
            <?php
            contactsHidden($agenda);
            ?>
            <label for="nombre"> Nombre
                <input type="text" name="nombre" id="nombre" placeholder="Nombre" require/>
            </label>
            <label> Teléfono
                <input type="number" name="telefono" id="telefono" placeholder="Teléfono" />
            </label>
            <input type="submit" name="guardar" value="Guardar" />
        </form>
        <br>

        <!-- Lista de contactos -->
        <hr>
        <div class="format-diary">
            <p>Lista de contactos:</p>
            <?php
            printContacts($agenda);
            ?>
        </div>
    </main>

</body>

</html>