<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabla de conversión de tipos de datos</title>

    <style>
        body {
            font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
        }

        caption {
            padding: 1rem;
            color: #fff;     
            background: rgb(92,91,91);
            font-weight: bold;
        }

        table {
            width: 100%;
            border: 1px solid rgb(92,91,91);
            background-color: #8ac1e5;
            border-collapse: collapse;
        }

        th {
            color: #fff;
        }

        th, td {
            padding: 0.5rem 0rem;
            width: 20%;
            vertical-align: top;
            border: 1px solid rgb(92,91,91);
            text-align: center;
        }
    </style>
</head>

<?php
# Datos fijos y a tratar de la tabla

// Títulos de la tabla
$titleTable = [
    'Valor de $var',
    '(int) $var',
    '(bool) $var',
    '(string) $var',
    '(float) $var',
];


// datos a comprobar
$values = [
    null,
    true,
    false,
    0,
    3.8,
    "0",
    "10",
    "6 metros",
    "hola"
];

// datos los cuales queremos comprobar
$whatValues = [
    "intval",
    "boolval", //
    "strval", //
    "floatval",
];
?>


<body>
    <!-- tabla -->
        <table>
            <caption>Tabla de conversión de tipos de datos, ejemplos</caption>
            <thead>
                <tr>
                    <?php
                    printTitle($titleTable);
                    ?>
                </tr>
            </thead>
            <tbody>
                <?php
                pintValues($values, $whatValues);
                ?>
            </tbody>
        </table>
</body>

</html>

<!-- Codigo -->
<?php

// imprime los títulos
function printTitle($titleTable) {
    foreach ($titleTable as $title) {
        echo "<th> $title </th>";
    }
}

// imprime los valores de la tabla
function pintValues($values, $whatValues) {
    foreach ($values as $value) {
        echo "<tr>";

        seeValue($value);
        printValue($whatValues, $value);

        echo "</tr>";
    }
}

// imprime los valores internos de la tabla 
function printValue($whatValues, $value) {

    foreach ($whatValues as $whatValue) {
        //comprobar que los datos salan en pantalla incluso si son null 
        if ($whatValue === "boolval" or $whatValue === "strval") {
            $convertedValue = var_export($whatValue($value), true);
        } else {
            $convertedValue = $whatValue($value);
        }

        echo "<td>$convertedValue</td>";
    }
}

// imprime y controla los valores a tratar que se impriman bien
function seeValue($value) {
    if ($value === false) {
        $value = 'falso';
    } elseif ($value === null) {
        $value = 'null';
    } else {
        $value = $value;
    }
    echo "<td>$value</td>";
}
?>
