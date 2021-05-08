<!DOCTYPE html>

<head>
    <link rel="shortcut icon" type="image/jpg" href="./images/switch.png" />
    <title>Preprocessing Model</title>
</head>

<body>
    <h1>Please Do Not Close This Page</h1>
</body>

</html>

<?php
$page = $_SERVER['PHP_SELF'];
$sec = "60";
header("Refresh: $sec; url=$page");
include "auditD/connect.php";
date_default_timezone_set('Asia/Jakarta');

function create_time_range($start, $end, $interval = '5 mins', $format = '24')
{
    $startTime = strtotime($start);
    $endTime   = strtotime($end);
    $returnTimeFormat = ($format == '12') ? 'H:i:s' : 'H:i:s';

    $current   = time();
    $addTime   = strtotime('+' . $interval, $current);
    $diff      = $addTime - $current;

    $times = array();
    while ($startTime < $endTime) {
        $times[] = date($returnTimeFormat, $startTime);
        $startTime += $diff;
    }
    $times[] = date($returnTimeFormat, $startTime);
    return $times;
}

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

$times = create_time_range('00:00', '24:00', '5 mins');
$waktu2 = $times;
$waktu1 = date("H:i:s");

for ($i = 0; $i <= 287; $i++) {
    mysqli_query($connect, "ALTER TABLE tbposttugas AUTO_INCREMENT=1");
    $v = $i + 1;
    $sql = "select * from tbdatapredik where hari = '$hari' and waktu = '$v'";
    $result = mysqli_query($connect, $sql);

    if ($waktu1 > $waktu2[$i]) {
        echo "<b>{$waktu1}</b>  {$waktu2[$i]} - {$waktu2[$i + 1]}";
        echo " <br>";
        // echo " ";
        // echo $i + 1 . " ";
        // echo  $hari . "<br>";
        if (mysqli_num_rows($result) > 0) {
            // output data of each row
            while ($row = mysqli_fetch_assoc($result)) {
                echo " - waktu " . $row["waktu"] . " " . $row["hari"] . " " . $row["idlampu"] . " " . $row["status"];
                $waktu         = $row['waktu'];
                $hari          = $row['hari'];
                $idlampu       = $row['idlampu'];
                $status        = $row['status'];

                $result1 = mysqli_query($connect, "SELECT waktu, hari, idlampu, status FROM tbposttugas where waktu = '$waktu' and hari = '$hari' and idlampu='$idlampu' and status='$status'");
                $total = mysqli_num_rows($result1);

                if ($total == 0) {
                    $query = "INSERT INTO tbposttugas SET waktu='$waktu',hari='$hari',idlampu='$idlampu',status='$status'";
                    mysqli_query($connect, $query);
                    echo " Post Data OK! <br>";
                } else {
                    echo " Done ! <br>";
                }
            }
        } else {
        }
        echo " <br>";
    } else {
        echo "Belum <br>";
        if (mysqli_num_rows($result) > 0) {
            // output data of each row
            while ($row = mysqli_fetch_assoc($result)) {
                echo "id: " . $row["id"] . " - waktu " . $row["waktu"] . " " . $row["hari"] . " " . $row["idlampu"] . " " . $row["status"] . "<br>";
            }
        } else {
        }
        echo " <br>";
    }
}

mysqli_close($connect);
