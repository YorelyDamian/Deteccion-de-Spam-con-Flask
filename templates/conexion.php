<?php
session_start();        
        $usuario = "root";
        $contras = "Y121200gm";
        $servidor = "localhost";
        $bd = "machineglearning";

        $conn = mysqli_connect($servidor,
        $usuario,
        $contras,
        $bd) OR DIE
        ("Problemas al conectar al Servidor de Base de Datos".mysqli_connect_error()
        );
        mysqli_set_charset($conn, "uft8");
?>