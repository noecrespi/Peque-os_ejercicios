<!DOCTYPE html>
<html>
<head>
    <title>Juego de Adivinar el Número</title>
</head>


    <?php
    session_start();

    if (!isset($_SESSION['numero_secreto'])) {
        $_SESSION['numero_secreto'] = rand(1, 50);
    }

    if (!isset($_SESSION['intentos'])) {
        $_SESSION['intentos'] = 0;
    }

    $mensaje = '';
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $_SESSION['intentos']++;
        if ($_SESSION['intentos'] > 6) {
            $mensaje = 'Has superado el límite de intentos. El número era: ' . $_SESSION['numero_secreto'];
            session_destroy();
        } else {
            $adivinanza = $_POST['numero_adivinado'];
            if ($adivinanza == $_SESSION['numero_secreto']) {
                $mensaje = '¡Felicidades! Has adivinado el número.';
                session_destroy();
            } elseif ($adivinanza < $_SESSION['numero_secreto']) {
                $mensaje = 'El número es mayor.';
            } else {
                $mensaje = 'El número es menor.';
            }
        }
    }

    ?>

    <body>
        <h1>Juego de Adivinar el Número</h1>
        <p>Bienvenido al juego de adivinar el número (del 1 al 50) con 6 intentos.</p>
        <p><?php echo $mensaje; ?></p>
        
        <form method="post" action="">
            <label for="numero_adivinado">Introduce tu adivinanza: </label>
            <input type="number" id="numero_adivinado" name="numero_adivinado" min="1" max="50" required>
            <input type="submit" value="Adivinar">
        </form>
    </body>
    </html>

