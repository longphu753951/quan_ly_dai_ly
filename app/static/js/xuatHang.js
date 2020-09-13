function DoiTien() {
    var a = document.getElementById("SoLuong");
    var b = document.getElementById("DonGia");
    var thanhTien = document.getElementById("ThanhTien");
    let c = a.value * b.value;
    thanhTien.value = c;
}