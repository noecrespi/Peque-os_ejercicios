<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Argoritmo de ordenacion</title>
</head>

<?php
$nums = [2, 5, 1, 11, 3, 0,];
$numsRandom = array();
?>

<body>
    <header>
        <div>
            <h1>Algoritmos de ordenación</h1>
        </div>
    </header>
    <hr>

    <main>
        <!-- ordenacion con lista predeterminada -->
        <div>
            <h3>Ordenar con la lista predeterminada</h3>
            <div>
                <!-- Ordena con la lista creada y predeterminada -->
                <p> Lista:
                    <?php
                    // lista de numeros predeterminada
                    printNums($nums);
                    ?>
                </p>

                <p>¿Con que tipo de ordenación quieres ordenar en burjuja o en ordenacion directa?</p>
                <!-- Ordenación burbuja -->
                <form method="post" action="">
                    <input type="submit" name="bubble" value="Ordenación burbuja">
                    <input type="submit" name="direct" value="Ordenación directa">
                </form>
            </div>

            <!-- Resultados de los botones -->
            <div>
                <p>
                    Resultado,
                    <?php
                    if (isset($_POST['bubble'])) {
                        $nums = BubbleOrder($nums);
                        echo "ordenación burbuja: ";
                        printNums($nums);
                    } elseif (isset($_POST['direct'])) {
                        $nums = directOrder($nums);
                        echo "ordenación directa: ";
                        printNums($nums);
                    }
                    ?>
                </p>
            </div>
        </div>
        <hr>

        <!-- Ordenar una lista de numeros aleatoria, el usuario elige la longitud de ella  -->
        <div>
            <h3>Ordenar una lista con números aleatorios</h3>
            <div>
                <p>¿Cuantos numeros quiere que tenga la nueva lista autogenerada, si no te gusta vuelve a clicar crear?</p>
                <form method="post" action="">
                    <input type="number" name="longNums">
                    <input type="submit" name="random" value="crear">
                </form>
                
                <!-- crea la lista ordenada, lo ordena he imprime los valores   -->
                <?php
                if (isset($_POST['random'])) {
                    $nums = randomNums($numsRandom);
                    printNums($nums);
                }
                ?>
            </div>
            <hr>

            <!-- Ordenar una lista con los numeros que el usuario ponga -->
            <div>
                <h3> Ordenar una lista con los numeros que el usuario quiera con una longitud </h3>

                <!-- crear un imput para que el usuario pueda añadir numeros a una lista -->
            </div>
    </main>
    <hr>

    <footer>
        <div>
            <p>Hecho por Noelia Crespi Pomar</p>
        </div>
    </footer>
</body>

</html>


<?php
/**
 * Imprime una lista de números.
 *
 * @param array $nums La lista de números a imprimir.
 */
// Imprime los numeros
function printNums($nums)
{
    $longNums = count($nums);

    for ($i = 0; $i < $longNums; $i++) {
        echo $nums[$i] . " ";
    }
}


/**
 * Genera una lista de números aleatorios.
 *
 * Esta función genera una lista de números aleatorios de una longitud especificada.
 *
 * @param int $longNums La longitud de la lista de números aleatorios a generar que le pasamos por el formulario.
 * @return array Un nuevo array con los números generados.
 */
// Genera una lista de numeros aleatorios
function randomNums($longNums)
{
    // Crea un array vacío para ir guardando los números aleatorios
    $numsRandom = array();
    $longNums = isset($_POST['longNums']) ? (int)$_POST['longNums'] : 0;

    // Genera un número aleatorio entre 0 y 100 y lo añade al array nums

    for ($i = 0; $i < $longNums; $i++) {
        $numsRandom[] = rand(0, 100);
    }

    return infOrderlist($numsRandom);

}


/**
 * Ordena e muestra los mensajes y una lista de números en orden ascendente utilizando el método de selección directa.
 *
 * Este método toma una lista de números aleatorios, la ordena utilizando el método
 * de selección directa y devuelve un nuevo array con los números ordenados en orden ascendente.
 *
 * @param array $numsRandom El array de números aleatorios a ordenar.
 * @param echo muestra informacion de la lista de numeros aleatorios y la lista ordenada con sus respectivos textos y numeros.
 * @return array Un nuevo array con los números ordenados en orden ascendente.
 */
function infOrderlist ($numsRandom){
    echo "Lista generada automaticamente:";
    printNums($numsRandom);
    echo "<br> Lista ordenada:";

    $copyNums = $numsRandom;
    // Crear un array vacío para ir guardando los números ordenados
    $defNums = array();

    for ($i = 0; $i < count($numsRandom); $i++) {
        // Busca el número mínimo
        $minValue = min($copyNums);
        // Busca el índice del número mínimo
        $minIndex = array_search($minValue, $copyNums);

        // Añade el número mínimo al array defNums
        $defNums[] = $minValue;
        // Elimina el número mínimo del array copyNums
        array_splice($copyNums, $minIndex, 1);
    }

    return $defNums;
}


/**
 * Ordena un array de números utilizando el algoritmo de ordenación burbuja.
 *
 * Este método ordena el array de números proporcionado utilizando el algoritmo
 * de ordenación burbuja y devuelve un nuevo array con los números ordenados.
 *
 * @param array $nums El array de números a ordenar.
 * @return array Un nuevo array con los números ordenados en orden ascendente.
 */

// Ordenación burbuja
function BubbleOrder($nums)
{
    // copia del array de nums, de esta manera si fastidiamos el array original, tenemos una copia de seguridad
    $defNums = $nums;

    // cuenta la longitud del array
    $longNums = count($nums);

    // recorrer el array 
    for ($num = 0; $num <= $longNums - 1; $num++) {
        for ($i = 0; $i < $longNums - $num - 1; $i++) {

            // si 1r numero es mayor que el 2ndo, cambialos de posicion
            if ($defNums[$i] > $defNums[$i + 1]) {
                //añade el numero al array defNums
                // Intercambia los elementos en la lista ordenada
                $temp = $defNums[$i];
                $defNums[$i] = $defNums[$i + 1];
                $defNums[$i + 1] = $temp;
            }
        };
    }
    return $defNums;
}


/**
 * Ordena un array de números utilizando el algoritmo de selección directa.
 *
 * Este método ordena el array de números proporcionado utilizando el algoritmo
 * de selección directa y devuelve un nuevo array con los números ordenados.
 * De esta forma se mantiene un codigo limpio, si hacemos modificaciones en el 
 * array original, tenemos una copia de seguridad. En este caso no seria  
 * necesario, pero es una buena practica ya que no sabemos si en un futuro se  
 * necesitara y si se eliminan datos indeseados por error de esta manera se 
 * puede recuperar los datos.
 *
 * @param array $nums El array de números a ordenar.
 * @return array Un nuevo array con los números ordenados en orden ascendente.
 */
function directOrder($nums)
{
    // Copia del array original de nums
    $copyNums = $nums;
    // Crear un array vacío para ir guardando los números ordenados
    $defNums = array();

    for ($i = 0; $i < count($nums); $i++) {
        // Busca el número mínimo
        $minValue = min($copyNums);
        // Busca el índice del número mínimo
        $minIndex = array_search($minValue, $copyNums);

        // Añade el número mínimo al array defNums
        $defNums[] = $minValue;
        // Elimina el número mínimo del array copyNums
        array_splice($copyNums, $minIndex, 1);
    }
    return $defNums;
}
