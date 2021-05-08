<?php
include "connect.php";

$sql = mysqli_query($connect, "select * from mode");
$data = mysqli_fetch_array($sql);

$action = $data['action'];
