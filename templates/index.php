<?php include("conexion.php") ?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PROYECTO SPAM</title>
    <link rel="icon" href="../static/spam.ico" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <link rel="stylesheet" href="../templates/estilos.css">

</head>

<body>
<!--SELECT id, duration, protocol_type, service, flag, src_bytes, class FROM prueba WHERE class = 'anomaly'"!-->
    <nav id="tablaRegistros" class='p-auto margin-top: 100px;'>
        <div class="row d-flex flex-wrap">
            <div class="card" id='cajitaProducto'>
                <div class="card-body">
                    <table class="table">
                        <thead>
                            <tr>
                                <th scope="col">id</th>
                                <th scope="col">Duration</th>
                                <th scope="col">Protocol_Type</th>
                                <th scope="col">Service</th>
                                <th scope="col">Flag</th>
                                <th scope="col">src_Bytes</th>
                                <th scope="col">Class</th>
                                <!--<th scope="col"></th>
                                <th scope="col"></th>!-->

                            </tr>
                        </thead>
                        <tbody>
                        <?php
                            $query = "SELECT
                                            prueba.id, 
                                            prueba.duration, 
                                            prueba.protocol_type, 
                                            prueba.service, 
                                            prueba.flag, 
                                            prueba.src_bytes, 
                                            prueba.class 
                                        FROM prueba 
                                            WHERE prueba.class = 'anomaly' 
                                            LIMIT 10
                                            ";
                            
                        $result=mysqli_query($conn,$query);
                        while($row=mysqli_fetch_assoc($result)){?>
                            <tr>
                                <td><?php echo $row['id'] ?></td>
                                <td><?php echo $row['duration'] ?></td>
                                <td><?php echo $row['protocol_type'] ?></td>
                                <td><?php echo $row['service'] ?></td>
                                <td><?php echo $row['flag'] ?></td>
                                <td><?php echo $row['src_bytes'] ?></td>
                                <td><?php echo $row['class'] ?></td>
                                <!--<td>
                                <a class="btn rounded-pill btn-outline-secondary" type="button">
                                    <img id="img1" src="../static/delete.ico" alt="" width="25" height="25"
                                        class="d-inline-block align-text-top" /></a>
                                </td>
                                <td>
                                <a class="btn rounded-pill btn-outline-secondary" type="button">
                                    <img id="img1" src="../static/editar.ico" alt="" width="25" height="25"
                                        class="d-inline-block align-text-top" /></a>
                                </td>!-->
                            </tr>  
                            <?php } 
                                    mysqli_close($conn);?>
                            
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </nav>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
        crossorigin="anonymous"></script>
</body>

</html>