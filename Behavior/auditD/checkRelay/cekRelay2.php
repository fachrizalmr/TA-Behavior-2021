<?php
include "./connect.php";

$sql = mysqli_query($connect, "select * from tbdataset where idlampu = 2 order by id desc");
$data = mysqli_fetch_array($sql);

$status2 = $data['status'];
