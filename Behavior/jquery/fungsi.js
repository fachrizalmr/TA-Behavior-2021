$(document).ready(function() {
    selesai();
});
 
function selesai() {
	setTimeout(function() {
		update();
		selesai();
	}, 200);
}
 
function update() {
	$.getJSON("dataSet.php", function(data) {
		$("table").empty();
        $("table").append("<thead><tr><th>NO.</th><th>User</th><th>ID Lampu</th><th>Waktu</th><th>Status</th></thead>");
		var no = 1;
		$.each(data.result, function() {
			var cek = this['idlampu'];
			var pengguna;
			if (cek == 1 ){
				pengguna = "Fachri";
			}else if (cek == 2 ){
				pengguna = "Rahel";
			}else if (cek == 3 ){
				pengguna = "Nando";
			}else if (cek == 4 ){
				pengguna = "Anya";
			}else {
				pengguna = "Unknown";
			}
			$("table").append("<tr><td>"+(no++)+"</td><td>"+pengguna+"</td><td>"+this['idlampu']+"</td><td>"+this['waktu']+"</td><td>"+this['status']+"</td></tr>");
		});
	});
}