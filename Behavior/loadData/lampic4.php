<?php
include "../auditD/connect.php";
$behavior;
$mode = mysqli_query($connect, "select * from mode order by id desc");
while ($row = mysqli_fetch_array($mode)) {
    $behavior = $row['action'];
}
if ($behavior == 1) {
    $sql = mysqli_query($connect, "select * from tbposttugas where idlampu = '4' order by id desc");
} else {
    $sql = mysqli_query($connect, "select * from tbdataset where idlampu = '4' order by id desc");
}
$data = mysqli_fetch_array($sql);
$status = $data['status'];
if ($status == '1') {
    $lampic = '<img src="images/on.png">';
} else
    $lampic = '<img src="images/off.png">';
echo $lampic;
