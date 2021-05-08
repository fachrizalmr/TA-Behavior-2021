<?php
include "../auditD/connect.php";
$behavior;
$mode = mysqli_query($connect, "select * from mode order by id desc");
while ($row = mysqli_fetch_array($mode)) {
    $behavior = $row['action'];
}
if ($behavior == 1) {
    $sql = mysqli_query($connect, "select * from tbposttugas where idlampu = '2' order by id desc");
} else {
    $sql = mysqli_query($connect, "select * from tbdataset where idlampu = '2' order by id desc");
}
while ($row = mysqli_fetch_assoc($sql)) {
    if ($row["idlampu"] == "2") {
        $pengguna = "Rahel";
    } else {
        $pengguna = "Unknown";
    }
}
echo $pengguna;
