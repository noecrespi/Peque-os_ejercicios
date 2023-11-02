<!DOCTYPE html>
<html>

<head>
    <title>Subir Archivos</title>
</head>

<body>
    <form action="" method="post" enctype="multipart/form-data">
        <label for="file">Selecciona archivos para cargar:</label>
        <input type="file" name="files[]" id="file" multiple>
        <input type="submit" value="Subir archivos">
    </form>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $targetDirectory = "uploads/"; // Directorio donde se guardarán los archivos
        $uploadedFiles = $_FILES["files"]; // Array con los archivos cargados

        if (!is_dir($targetDirectory)) {
            mkdir($targetDirectory, 0755, true); // Crea el directorio si no existe
        }

        foreach ($uploadedFiles["name"] as $key => $name) {
            $targetFile = $targetDirectory . basename($name); // Ruta donde se guardará el archivo
            $tmpFile = $uploadedFiles["tmp_name"][$key]; // Nombre temporal del archivo

            if (move_uploaded_file($tmpFile, $targetFile)) {
                echo "El archivo '$name' se ha subido correctamente.<br>";
            } else {
                echo "Hubo un problema al subir el archivo '$name'.<br>";
            }
        }
    }
    ?>

</body>

</html>