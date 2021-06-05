<?php
$connect = mysqli_connect('localhost', 'root', '', 'dbbehavior');
$behavior;

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
$mode = mysqli_query($connect, "select * from mode order by id desc");
while ($row = mysqli_fetch_array($mode)) {
    $behavior = $row['action'];
}
if ($behavior == 1) {
    $sql = mysqli_query($connect, "select * from tbdatapredik where hari = '$hari'");
    $result = array();
} else {
    $sql = mysqli_query($connect, "select * from tbdataset where hari = '$hari' order by id desc");
    $result = array();
}

while ($row = mysqli_fetch_assoc($sql)) {
    $data[] = $row;
}

echo json_encode(array("result" => $data));
