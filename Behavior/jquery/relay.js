function relay1(value){
    if(value==true) value="ON";
    else value= "OFF";
    document.getElementById('relay1').innerHTML = value;

    // ajax untuk merubah nilai status Mode

    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function(){
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
            // terima respond dari web setelah berhasil merubah nilai  
            document.getElementById('relay1').innerHTML = xmlhttp.responseText;
        }
    }
    // execute file PHP untuk merubah nilai di database
    xmlhttp.open("GET", "sendRelay/relay1.php?status=" + value, true);
    xmlhttp.send();

}

function relay2(value){
    if(value==true) value="ON";
    else value= "OFF";
    document.getElementById('relay2').innerHTML = value;

    // ajax untuk merubah nilai status Mode

    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function(){
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
            // terima respond dari web setelah berhasil merubah nilai  
            document.getElementById('relay2').innerHTML = xmlhttp.responseText;
        }
    }
    // execute file PHP untuk merubah nilai di database
    xmlhttp.open("GET", "sendRelay/relay2.php?status=" + value, true);
    xmlhttp.send();

}

function relay3(value){
    if(value==true) value="ON";
    else value= "OFF";
    document.getElementById('relay3').innerHTML = value;

    // ajax untuk merubah nilai status Mode

    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function(){
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
            // terima respond dari web setelah berhasil merubah nilai  
            document.getElementById('relay3').innerHTML = xmlhttp.responseText;
        }
    }
    // execute file PHP untuk merubah nilai di database
    xmlhttp.open("GET", "sendRelay/relay3.php?status=" + value, true);
    xmlhttp.send();

}

function relay4(value){
    if(value==true) value="ON";
    else value= "OFF";
    document.getElementById('relay4').innerHTML = value;

    // ajax untuk merubah nilai status Mode

    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function(){
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
            // terima respond dari web setelah berhasil merubah nilai  
            document.getElementById('relay4').innerHTML = xmlhttp.responseText;
        }
    }
    // execute file PHP untuk merubah nilai di database
    xmlhttp.open("GET", "sendRelay/relay4.php?status=" + value, true);
    xmlhttp.send();

}
