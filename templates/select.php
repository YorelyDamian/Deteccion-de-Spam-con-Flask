 <?php include("conexion.php") ?>
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
                            
                        $result = mysqli_query($conn,$query);
                        while($row=mysqli_fetch_assoc($result)){ ?>
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