<?php include "auditD/cekMode.php" ?>
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <link rel="shortcut icon" type="image/jpg" href="images/switch.png" />
    <title>Behavior</title>
    <script type="text/javascript" src="jquery/mode.js"></script>
    <script type="text/javascript" src="jquery/jquery.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function() {
            setInterval(function() {
                $("#cekmode").load("loadData/cekmode.php");
                $("#lampic1").load("loadData/lampic1.php");
                $("#cekuser1").load("loadData/cekuser1.php");
                $("#cekwaktu1").load("loadData/cekwaktu1.php");
                $("#cekstatus1").load("loadData/cekstatus1.php");
                $("#lampic2").load("loadData/lampic2.php");
                $("#cekuser2").load("loadData/cekuser2.php");
                $("#cekwaktu2").load("loadData/cekwaktu2.php");
                $("#cekstatus2").load("loadData/cekstatus2.php");
                $("#lampic3").load("loadData/lampic3.php");
                $("#cekuser3").load("loadData/cekuser3.php");
                $("#cekwaktu3").load("loadData/cekwaktu3.php");
                $("#cekstatus3").load("loadData/cekstatus3.php");
                $("#lampic4").load("loadData/lampic4.php");
                $("#cekuser4").load("loadData/cekuser4.php");
                $("#cekwaktu4").load("loadData/cekwaktu4.php");
                $("#cekstatus4").load("loadData/cekstatus4.php");
            }, 1000);
        });
    </script>
</head>

<body>
    <div class="container" style="text-align: center; margin-top: 50px;">
        <h2>Monitoring Penyaluran Energi Listrik Ke <b>RELAY 4 Channel</b></h2>

        <div class="card text-center">
            <div class="card-header">
                Tugas Akhir 2021 [<b style="color:crimson;">INGAT SIDANG JULI BOS !!!</b>]
                <a href="auditD/dashBoard.php" type="button">Dataset Mode</a>
            </div>
            <div class="card-body">
                <h5 class="card-title">
                    <div class="custom-control custom-switch">
                        <input type="checkbox" class="custom-control-input" id="customSwitch1" onchange="mode(this.checked)" <?php if ($action == 1) echo "checked"; ?>>
                        <label class="custom-control-label" for="customSwitch1">
                            <span id="mode">
                                <?php if ($action == 1) {
                                    echo "Mode Behavior";
                                } else {
                                    echo "Mode Manual";
                                } ?>
                            </span>
                        </label>
                    </div>
                </h5>
                <div class="table-responsive" style="margin-top:15px;">
                    <table class="table">
                        <caption>list of device activity</caption>
                        <thead>
                            <tr>
                                <th scope="col">Relay ID</th>
                                <th>=</th>
                                <th scope="col">Pengguna</th>
                                <th scope="col">Waktu</th>
                                <th scope="col">Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>1</td>
                                <td><span id="lampic1"></td>
                                <td><span id="cekuser1"></td>
                                <td><span id="cekwaktu1"></td>
                                <td><span id="cekstatus1"></td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td><span id="lampic2"></td>
                                <td><span id="cekuser2"></td>
                                <td><span id="cekwaktu2"></td>
                                <td><span id="cekstatus2"></td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td><span id="lampic3"></td>
                                <td><span id="cekuser3"></td>
                                <td><span id="cekwaktu3"></td>
                                <td><span id="cekstatus3"></td>
                            </tr>
                            <tr>
                                <td>4</td>
                                <td><span id="lampic4"></td>
                                <td><span id="cekuser4"></td>
                                <td><span id="cekwaktu4"></td>
                                <td><span id="cekstatus4"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="card-footer text-muted">
                Telkom University | Muhammad Fachrizal Ramdani | 1103174125 <a href="behaviorM.php" target="popup" type="button">Please Run This Page For Preprocessing</a>
            </div>
        </div>

    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</body>

</html>