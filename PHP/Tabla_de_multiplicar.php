<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabla de multiplicar del 1 al 10</title>

    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
        }

        caption {
            padding: 1rem;
            color: #fff;
            background: rgb(204, 170, 170);
            border: 1px solid rgb(92, 91, 91);
            font-weight: bold;
        }

        table {
            width: 100%;
            border: 1px solid rgb(92, 91, 91);
            background-color: #F4DDDE;
            border-collapse: collapse;
        }

        td {
            padding: 0.5rem 0rem;
            width: 0.090909%;
            vertical-align: top;
            border: 1px solid rgb(92, 91, 91);
            text-align: center;
        }
    </style>
</head>

<body>

    <table>
        <caption>Tabla de multiplicar</caption>
        <thead>
            <tr>
            <?php
            numsTitle();
            ?>
            </tr>
        </thead>
        <tbody>
            <?php
                multiUnoAlDiez(MAX_MULTIPLICADOR, MAX_NUM);
            ?>
        </tbody>
    </table>
</body>

</html>


<?php
// Numeros para la tabla

function numsTitle(){
    echo "<td>* </td>";
    for ($num1 = 1; $num1 <= 10; $num1++) {
        echo "<td>$num1</td>";
    }
}

const MAX_MULTIPLICADOR = 10;

const MAX_NUM = 10;

function multiUnoAlDiez($MAX_MULTIPLICADOR, $MAX_NUM){
    
    //$MAX_MULTIPLICADOR = 10;
    // Multiplicando
    for ($num = 1; $num <= MAX_MULTIPLICADOR; $num++) {
        echo "<tr>";
        echo "<td>$num</td>";
        // Multiplicador
        for ($i = 1; $i <= MAX_NUM; $i++) {
            $result = $num * $i;
            echo "<td>$result</td>";
        }
        echo "</tr>";
    }
}

?>