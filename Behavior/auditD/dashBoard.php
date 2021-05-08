<!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  <link rel="shortcut icon" type="image/jpg" href="../images/switch.png" />
  <title>DashBoard DataSet</title>
</head>

<body>
  <div class="container" style="text-align: center; margin-top: 50px;">
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
            <span class="form-control" id="clock"></span>
          </li>
        </ul>
      </div>
      <div class="card-body">
        <table class="table table-sm table-bordered" style="width:100%"></table>
      </div>
    </div>
  </div>
  <!-- Optional JavaScript -->
  <!-- jQuery first, then Popper.js, then Bootstrap JS -->
  <script type="text/javascript" src="../jquery/time.js"></script>
  <script src="https://code.jquery.com/jquery-3.5.1.js" integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc=" crossorigin="anonymous"></script>
  <script type="text/javascript" src="../jquery/fungsi.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

</body>

</html>