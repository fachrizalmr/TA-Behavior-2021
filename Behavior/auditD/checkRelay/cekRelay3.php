<?php
include "./connect.php";

$sql = mysqli_query($connect, "select * from tbdataset where idlampu = 3 order by id desc");
$data = mysqli_fetch_array($sql);

$status3 = $data['status'];
