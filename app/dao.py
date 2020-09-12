from app.models import *
from app import db
from flask import jsonify


def add_user(username, ten, matKhau):
    c = User(tenDangNhap=username, tenUser=ten, loaiTaiKhoan=0, matKhau=matKhau)
    db.session.add(c)
    db.session.commit()


def add_store(tenDaiLy, soDienThoai, email, diaChi, quan_id, loaiDaiLy_id):
    c = DaiLy(tenDaiLy=tenDaiLy, soDienThoai=soDienThoai, email=email, diaChi=diaChi, tongTienNo=0, quan_id=quan_id,
              loaiDaiLy_id=loaiDaiLy_id)
    db.session.add(c)
    db.session.commit()


def thuTien(diaChi, soDienThoai, email, ngayThu, soTienThu, maDaiLy):
    c = ThuTien(soDienThoai=soDienThoai, email=email, diaChi=diaChi, ngayThu=ngayThu, soTien=soTienThu,
                ma_DaiLy=maDaiLy)
    db.session.add(c)
    db.session.commit()


def find_user(username):
    a = User.query.filter_by(tenDangNhap=username).first()
    if a == None:
        return False
    else:
        return True


def load_loai_store():
    results = db.session.execute("SELECT * FROM quan_ly_dai_ly.loaidaily;")
    loaiDaiLy = [p for p in results]
    return loaiDaiLy


def load_quan():
    results = db.session.execute("SELECT * FROM quan_ly_dai_ly.quan;")
    quan = [p for p in results]
    return quan


def kiem_tra_so_luong_dai_ly(id):
    a = db.session.execute("SELECT soDaiLiHienCo FROM quan_ly_dai_ly.quan WHERE  (maQuan = " + id + ") ;")
    a = [p for p in a]
    b = db.session.execute("SELECT soDaiLiToiDa FROM quan_ly_dai_ly.quan WHERE  (maQuan = " + id + ") ;")
    b = [p for p in b]
    if a[0] == b[0]:
        return False
    return True


def tang_so_dai_ly(id):
    db.session.execute("UPDATE quan_ly_dai_ly.quan SET soDaiLiHienCo = soDaiLiHienCo +1 WHERE  (maQuan = " + id + ") ;")
    db.session.commit()


def tenLoaiDaiLy(id):
    a = db.session.execute("SELECT tenLoai FROM quan_ly_dai_ly.loaidaily WHERE maLoai=" + id + " ;")
    a = [p for p in a]
    return a[0]


def tenQuan(id):
    a = db.session.execute("SELECT tenQuan FROM quan_ly_dai_ly.quan WHERE maQuan=" + id + " ;")
    a = [p for p in a]
    return a[0]


def search_Dai_Ly_By_Quan(id):
    a = db.session.execute("SELECT * FROM quan_ly_dai_ly.daily ;")
    if id:
        a = db.session.execute("SELECT * FROM quan_ly_dai_ly.daily WHERE quan_id=" + id + " ;")
    a = [p for p in a]
    return a


def load_Dai_Ly():
    a = db.session.execute("SELECT * FROM quan_ly_dai_ly.daily ;")
    a = [p for p in a]
    return a


def search_Tien_No_Dai_ly_By_Id(id):
    a = db.session.execute("SELECT * FROM quan_ly_dai_ly.daily WHERE id =" + id + " ;")
    a = [p for p in a]
    return a[0][5]
