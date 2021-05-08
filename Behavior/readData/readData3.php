<?php
include "../auditD/connect.php";
mysqli_query($connect, "ALTER TABLE mode AUTO_INCREMENT=1");
$behavior;
$mode = mysqli_query($connect, "select * from mode order by id desc");
while ($row = mysqli_fetch_array($mode)) {
    $behavior = $row['action'];
}
if ($behavior == 1) {
    $hasil = mysqli_query($connect, "select * from tbposttugas where idlampu = 3 order by id desc LIMIT 1");
} else {
    $hasil = mysqli_query($connect, "select * from tbdataset where idlampu = 3 order by id desc LIMIT 1");
}

while ($row = mysqli_fetch_assoc($hasil)) {
    if ($row["idlampu"] == "1") {
        $pengguna = "Fachri";
    } else if ($row["idlampu"] == "2") {
        $pengguna = "Rahel";
    } else if ($row["idlampu"] == "3") {
        $pengguna = "Nando";
    } else if ($row["idlampu"] == "4") {
        $pengguna = "Anya";
    } else {
        $pengguna = "Unknown";
    }
    echo "(Relay:", $row["idlampu"], ")  [S:", $row["status"], "] ", "                        #User: ", $pengguna;
}
