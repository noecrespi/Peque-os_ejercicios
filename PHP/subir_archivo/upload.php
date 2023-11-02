<!DOCTYPE html>
<html>

<head>
    <title>Formulario de Carga de Archivos</title>
</head>

<body>
    <h2>Subir un archivo</h2>
    <form action="upload.php" method="post" enctype="multipart/form-data">
        <input type="file" name="archivo" id="archivo">
        <input type="submit" value="Subir Archivo" name="submit">
    </form>
    <?php
    // Verificar si se ha enviado un archivo
    if (isset($_FILES['archivo'])) {
        $file = $_FILES['archivo']; // Obtenemos el archivo a subir

        // Comprobar si no hubo errores al cargar el archivo
        if ($file['error'] === UPLOAD_ERR_OK) {
            $nombre_temporal = $file['tmp_name']; // Obtenemos el nombre temporal del archivo
            $nombre_archivo = basename($file['name']);  // Obtenemos el nombre del archivo 
            //besename() es un metodo para obtener el nombre del archivo sin su extensión

            // Definir la ubicación donde se guardará el archivo (ajusta esta ruta según tus necesidades)
            $directorio_destino = 'archivos_subidos/';
            $ruta_destino = $directorio_destino . $nombre_archivo;// Ruta donde se guardará el archivo

            // Mover el archivo cargado al directorio de destino
            if (move_uploaded_file($nombre_temporal, $ruta_destino)) {
                echo "El archivo se ha subido correctamente.";
            } else {
                echo "Hubo un error al subir el archivo.";
            }
        } else {
            echo "Error al cargar el archivo. Código de error: " . $file['error'];
        }
    }
    ?>
</body>

</html>