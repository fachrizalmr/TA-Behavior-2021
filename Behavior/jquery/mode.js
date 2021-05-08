function mode(value){
    if(value==true) value="Mode Behavior";
    else value= "Mode Manual";
    document.getElementById('mode').innerHTML = value;

    // ajax untuk merubah nilai status Mode

    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function(){
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
            // terima respond dari web setelah berhasil merubah nilai  
            document.getElementById('mode').innerHTML = xmlhttp.responseText;
        }
    }
    // execute file PHP untuk merubah nilai di database
    xmlhttp.open("GET", "./auditD/mode.php?action=" + value, true);
    xmlhttp.send();

}