import hashlib

from flask import render_template, redirect, request, url_for
from flask_login import login_user, login_required
from sqlalchemy import null
from sqlalchemy.sql.functions import user

from app import app, login, dao
from app.models import *


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/adduser", methods=["get", "post"])
@login_required
def add_user():
    if request.method == "POST":
        tenDangNhap = request.form.get("tenDangNhap")
        tenUser = request.form.get("tenUser")
        matKhau = request.form.get("matKhau")
        matKhauConf = request.form.get("matKhauConf")
        if matKhau.strip() != matKhauConf.strip():
            return render_template("/admin/adduser.html", err_msg="Mật khẩu không khớp")
        if dao.find_user(tenDangNhap):

            return render_template("/admin/adduser.html", err_msg="Tài khoản đã tồn tại")
        else:
            matKhau = str(hashlib.md5(matKhau.strip().encode("utf-8")).hexdigest())
            if dao.add_user(username=tenDangNhap, ten=tenUser, matKhau=matKhau):
                return redirect(url_for("adduser"))
            else:
                return render_template("/admin/adduser.html", err_msg="Đăng ký thành công")

    return render_template("/admin/adduser.html")


@app.route("/addstore", methods=["get", "post"])
def add_store():
    if request.method == "POST":
        tenDaiLy = request.form.get("tenDaiLy")
        email = request.form.get("email")
        sdt = request.form.get("sdt")
        address = request.form.get("diachi")
        quan_id = request.form.get("comp_select2")
        loaiDaiLy_id = request.form.get("comp_select")
        if not dao.kiem_tra_so_luong_dai_ly(quan_id):
            return render_template("/manager/add_store.html", loaiDaiLy=dao.load_loai_store(), quan=dao.load_quan(),
                                   err_msg="Số đại lý trong quận này đã đầy")
        dao.add_store(tenDaiLy=tenDaiLy, soDienThoai=sdt, email=email, diaChi=address, quan_id=quan_id,
                      loaiDaiLy_id=loaiDaiLy_id)
        dao.tang_so_dai_ly(quan_id)
    return render_template("/manager/add_store.html", loaiDaiLy=dao.load_loai_store(), quan=dao.load_quan())


@app.route('/login-admin', methods=["post", "get"])
def login_admin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = User.query.filter(User.tenDangNhap == username.strip(), User.matKhau == password).first()

        if user:
            if user.loaiTaiKhoan == 0:
                return redirect("/ManagerIndex")
            login_user(user=user)

    return redirect("/admin")


@app.route('/ManagerIndex', methods=["post", "get"])
def manager_index():

    return render_template("/manager/home_page.html")


@app.route('/ThuTien', methods=["post", "get"])
def thu_tien():
    if request.method == "POST":
        ma_daiLy = request.form.get("daiLy")
        email = request.form.get("email")
        sdt = request.form.get("sdt")
        diaChi = request.form.get("diaChi")
        ngayThuTien = request.form.get("ngayThuTien")
        tienThu = request.form.get("tienThu")
        if float(tienThu) > dao.search_Tien_No_Dai_ly_By_Id(ma_daiLy):
            return render_template("/manager/thu_tien.html", daiLy=dao.load_Dai_Ly(), err_msg="Số tiền thu vượt quá số tiền nợ")
        else:
            dao.thuTien(diaChi=diaChi, soDienThoai=sdt, email=email, ngayThu=ngayThuTien, soTienThu=tienThu,
                        maDaiLy=ma_daiLy)

    return render_template("/manager/thu_tien.html", daiLy=dao.load_Dai_Ly())


@app.route('/SearchStore', methods=["post", "get"])
def search_store():
    if request.method == "GET":
        quan_id = request.args.get("ChonQuan")
        return render_template("manager/search_store.html", quan=dao.load_quan(),
                               stores=dao.search_Dai_Ly_By_Quan(quan_id))


@login.user_loader
def user_load(user_id):
    return User.query.get(user_id)


if __name__ == '__main__':
    app.run(debug=True)
