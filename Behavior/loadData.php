<?php
include "auditD/connect.php";

$waktu = $_GET['waktu'];
$hari = $_GET['hari'];
$idlampu = $_GET['idlampu'];
$status = $_GET['status'];

mysqli_query($connect, "ALTER TABLE tbdataset AUTO_INCREMENT=1");
$simpan = mysqli_query($connect, "insert into tbdataset(waktu,hari,idlampu,status)values('$waktu', '$hari', '$idlampu', '$status')");
if ($simpan)
    echo "Berhasil Dikirim";
else
    echo "Gagal Terkirim";
