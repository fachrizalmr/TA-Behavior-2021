<?php
include "checkRelay/cekRelay1.php";
include "checkRelay/cekRelay2.php";
include "checkRelay/cekRelay3.php";
include "checkRelay/cekRelay4.php";
?>

<!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
  <link rel="shortcut icon" type="image/jpg" href="../images/switch.png" />
  <title>Control Section</title>
</head>

<body>
  <div class="container" style="text-align: center; margin-top: 150px;">
    <div class="card text-center">
      <div class="card-header">
        <ul class="nav nav-pills card-header-pills nav-fill">
          <li class="nav-item">
            <a class="nav-link" onclick="window.location.reload(true);">DashBoard</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="control.php">Control</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="../index.php">Back <img src="../images/back.png"></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="dashBoard.php" type="button">Dataset Mode</a>
          </li>
        </ul>
      </div>
      <div class="card-body">
        <div class="row form-group">
          <div class="col">
            <input type="text" name="pengguna" readonly class="form-control-plaintext text-primary" style="text-align:center;" value="Beri Perintah">
          </div>
          <div class="col">
            <span class="form-control" id="clock"></span>
          </div>
        </div>

        <div class="row form-group">
          <div class="col">
            <div class="card text-black bg-light mb-3" style="max-width: 18rem;">
              <div class="card-header">Relay 1</div>
              <div class="card-body">
                <div class="custom-control custom-switch">
                  <input type="checkbox" class="custom-control-input" id="customSwitch1" onchange="relay1(this.checked)" <?php if ($status1 == 1) {
                                                                                                                            echo "checked";
                                                                                                                          } ?>>
                  <label class="custom-control-label" for="customSwitch1"><span id="relay1">
                      <?php
                      if ($status1 == 1) {
                        echo "ON";
                      } else {
                        echo "OFF";
                      }
                      ?>
                    </span></label>
                </div>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card text-black bg-light mb-3" style="max-width: 18rem;">
              <div class="card-header">Relay 2</div>
              <div class="card-body">
                <div class="custom-control custom-switch">
                  <input type="checkbox" class="custom-control-input" id="customSwitch2" onchange="relay2(this.checked)" <?php if ($status2 == 1) {
                                                                                                                            echo "checked";
                                                                                                                          } ?>>
                  <label class="custom-control-label" for="customSwitch2"><span id="relay2">
                      <?php
                      if ($status2 == 1) {
                        echo "ON";
                      } else {
                        echo "OFF";
                      }
                      ?>
                    </span></label>
                </div>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card text-black bg-light mb-3" style="max-width: 18rem;">
              <div class="card-header">Relay 3</div>
              <div class="card-body">
                <div class="custom-control custom-switch">
                  <input type="checkbox" class="custom-control-input" id="customSwitch3" onchange="relay3(this.checked)" <?php if ($status3 == 1) {
                                                                                                                            echo "checked";
                                                                                                                          } ?>>
                  <label class="custom-control-label" for="customSwitch3"><span id="relay3">
                      <?php
                      if ($status3 == 1) {
                        echo "ON";
                      } else {
                        echo "OFF";
                      }
                      ?>
                    </span></label>
                </div>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card text-black bg-light mb-3" style="max-width: 18rem;">
              <div class="card-header">Relay 4</div>
              <div class="card-body">
                <div class="custom-control custom-switch">
                  <input type="checkbox" class="custom-control-input" id="customSwitch4" onchange="relay4(this.checked)" <?php if ($status4 == 1) {
                                                                                                                            echo "checked";
                                                                                                                          } ?>>
                  <label class="custom-control-label" for="customSwitch4"><span id="relay4">
                      <?php
                      if ($status4 == 1) {
                        echo "ON";
                      } else {
                        echo "OFF";
                      }
                      ?>
                    </span></label>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="card-footer text-muted">
        Telkom University | Muhammad Fachrizal Ramdani | 1103174125
      </div>
    </div>
  </div>

  <!-- Optional JavaScript -->
  <!-- jQuery first, then Popper.js, then Bootstrap JS -->
  <script type="text/javascript" src="../jquery/time.js"></script>
  <script type="text/javascript" src="../jquery/relay.js"></script>
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</body>

</html>