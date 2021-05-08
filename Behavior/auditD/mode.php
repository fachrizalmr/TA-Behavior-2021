<?php
// koneksi
include "connect.php";

//tangkap parameter action yang dikirim dari ajax
$action = $_GET['action'];
if ($action == "Mode Behavior") {
    mysqli_query($connect, "update mode set action = 1");
    echo "Mode Behavior";
} else {
    mysqli_query($connect, "update mode set action = 0");
    echo "Mode Manual";
}
