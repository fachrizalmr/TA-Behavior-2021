<?php
include "auditD/connect.php";

$action = $_GET['action'];

mysqli_query($connect, "ALTER TABLE mode AUTO_INCREMENT=1");
$simpan = mysqli_query($connect, "update mode set action = '$action' where id = 1");
if ($simpan)
    echo "Mode Berubah";
else
    echo "Mode Gagal Berubah";
