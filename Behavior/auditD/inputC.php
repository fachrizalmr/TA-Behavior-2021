<?php
include "connect.php";
date_default_timezone_set('Asia/Jakarta');

$acak = rand(1, 4);
$profile = '';
if ($acak == 1) {
    $profile = "Agung";
} else if ($acak == 2) {
    $profile = "Bajeng";
} else if ($acak == 3) {
    $profile = "Fachri";
} else if ($acak == 4) {
    $profile = "Fachrizal";
} else if ($acak == 5) {
    $profile = "Inna";
} else if ($acak == 6) {
    $profile = "Nando";
} else if ($acak == 7) {
    $profile = "Narta";
} else if ($acak == 8) {
    $profile = "Erpan";
} else {
    $acak = "Unknown";
}

$pengguna     = $acak;
$idlampu      = $_POST['idlampu'];
$waktu        = date('D/H:i');
$status       = $_POST['status'];

$query = "INSERT INTO tbdataset SET pengguna='$pengguna',idlampu='$idlampu',waktu='$waktu',status='$status'";
mysqli_query($connect, $query);
header("location:dashBoard.php");
