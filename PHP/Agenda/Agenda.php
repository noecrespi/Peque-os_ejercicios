<?php
// Define el array para la agenda
$agenda = array(
    "Felipe" => 666666666,
    "Anne" => 111111111,
    "Juan" => 888888888,
    "Julia" => 999999999
);

// Verifica si se ha enviado el formulario
if (isset($_POST['guardar'])) {
    $name = filter_input(INPUT_POST, 'nombre', FILTER_SANITIZE_SPECIAL_CHARS);
    $phone = filter_input(INPUT_POST, 'telefono', FILTER_SANITIZE_SPECIAL_CHARS);



    // CRUD (Create, Update, Delete)
    if (!array_key_exists($name, $agenda) && !empty($phone)) { // CREATE
        $agenda[$name] = $phone;
    } elseif (array_key_exists($name, $agenda) && !empty($phone)) { // UPDATE
        $agenda[$name] = $phone;
    } elseif (array_key_exists($name, $agenda) && empty($phone)) { // DELETE
        unset($agenda[$name]);
    }
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <style>
        /* estilo del boton */
        input[type="submit"] {
            background-color: green;
            color: white;
            padding: 5px;
            border-radius: 5px;
            border: none;
        }

        /* muestra el borde en rojo si el campo enviado está vacío y es obligatorio */
        input:focus:invalid {
            border: 2px solid red;
        }

        /* Estilo para la lista ce contactos */
        .format-diary {
            border: 1px solid black;
            width: 50%;
            margin: auto;
            padding: 10px;
        }

        .format-diary p {
            font-weight: bold;
        }
    </style>
</head>

<body>
    <header>
        <h1>Agenda telefónica</h1>
    </header>

    <main>
        <!-- Formulario para añadir contactos -->
        <form action="Agenda.php" method="post">
            <label for="nombre">Nombre</label>
            <input type="text" name="nombre" id="nombre" placeholder="Nombre" required>
            <label for="telefono">Teléfono</label>
            <input type="number" name="telefono" id="telefono" placeholder="Teléfono">
            <input type="submit" value="Guardar" name="guardar">
        </form>
    </main>
    <br>
    <!-- Lista de contactos -->
    <hr>
    <div class="format-diary">
        <p>Lista de contactos:</p>

        <?php
        //Mostrar la lista de contactos del array $agenda
        foreach ($agenda as $nombre => $telefono) {
            echo "Nombre: $nombre <br>Teléfono: $telefono <br><br>";
        }
        ?>
    </div>
</body>

</html>
