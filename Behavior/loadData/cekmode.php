<?php
include "../auditD/connect.php";
$mode = mysqli_query($connect, "select * from mode order by id desc");
while ($row = mysqli_fetch_array($mode)) {
    $behavior = $row['action'];
}
if ($behavior == 1) {
    echo "Behavior";
} else {
    echo "Manual";
}
