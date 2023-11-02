<?php
// used to get mysql database connection
class Database{
    // specify your own database credentials
    private $host = "randion.es";
    private $db_name = "ncrespipomar_login_system";
    private $username = "ncrespipomar";
    private $password = "Secretos.2023";
    public $conn;
    // get the database connection
    public function getConnection(){
        $this->conn = null;
        try{
            // CAMBIADO O CAMBIAR CON EL NOMBRE DE LA BASE DE DATOS QUE VAMOS A UTILIZAR
            $this->conn = new PDO("pgsql:host=" . $this->host . ";dbname=" . $this->db_name, $this->username, $this->password);
        }catch(PDOException $exception){
            echo "Connection error: " . $exception->getMessage();
        }
        return $this->conn;
    }
}
?>