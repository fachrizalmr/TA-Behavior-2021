<?php
// koneksi
include "../connect.php";
date_default_timezone_set('Asia/Jakarta');
$hariNow = date("l");
$hari = 0;
if ($hariNow == 'Monday') {
    $hari = 1;
} else if ($hariNow == 'Tuesday') {
    $hari = 2;
} else if ($hariNow == 'Wednesday') {
    $hari = 3;
} else if ($hariNow == 'Thursday') {
    $hari = 4;
} else if ($hariNow == 'Friday') {
    $hari = 5;
} else if ($hariNow == 'Saturday') {
    $hari = 6;
} else {
    $hari = 7;
}
//tangkap parameter status yang dikirim dari ajax
$waktu = date("H:i:s");
$idlampu = 2;
$status = $_GET['status'];
if ($status == "ON") {
    mysqli_query($connect, "INSERT INTO tbdataset SET waktu='$waktu',hari='$hari',idlampu='$idlampu',status=1");
    echo "ON";
} else {
    mysqli_query($connect, "INSERT INTO tbdataset SET waktu='$waktu',hari='$hari',idlampu='$idlampu',status=0");
    echo "OFF";
}
