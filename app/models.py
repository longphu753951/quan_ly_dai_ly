from flask_admin import BaseView, expose
from flask import redirect
from app import db, admin
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DECIMAL, DateTime
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, current_user, logout_user


class User(db.Model, UserMixin):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tenDangNhap = Column(String(50), nullable=False)
    tenUser = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    loaiTaiKhoan = Column(Integer, nullable=False, default=0)
    matKhau = Column(String(50), nullable=False)

    def __str__(self):
        return self.tenDangNhap


class Quan(db.Model):
    __tablename__ = "Quan"
    maQuan = Column(Integer, primary_key=True, autoincrement=True)
    tenQuan = Column(String(50), nullable=False)
    soDaiLiHienCo = Column(Integer, nullable=False)
    soDaiLiToiDa = Column(Integer, nullable=False)
    dailys = relationship('DaiLy', backref='Quan', lazy=True)

    def __str__(self):
        return self


class LoaiDaiLy(db.Model):
    __tablename__ = "LoaiDaiLy"
    maLoai = Column(Integer, primary_key=True, autoincrement=True)
    tenLoai = Column(String(20), nullable=False)
    tienNoToiDa = Column(Integer, nullable=False)
    dailys = relationship('DaiLy', backref='LoaiDaiLy', lazy=True)

    def __str__(self):
        return self


class DaiLy(db.Model):
    __tablename__ = "DaiLy"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tenDaiLy = Column(String(100), nullable=False)
    soDienThoai = Column(String(10), nullable=False)
    email = Column(String(30), nullable=False)
    diaChi = Column(String(100), nullable=False)
    tongTienNo = Column(Float, nullable=True)
    quan_id = Column(Integer, ForeignKey(Quan.maQuan), nullable=False)
    loaiDaiLy_id = Column(Integer, ForeignKey(LoaiDaiLy.maLoai), nullable=False)
    thutiens = relationship('ThuTien', backref='DaiLy', lazy=True)

    def __str__(self):
        return self


class CongNo(db.Model):
    __tablename__ = "CongNo"
    maCongNo = Column(Integer, primary_key=True, autoincrement=True)
    thang = Column(DateTime, nullable=False)
    noDau = Column(Float, nullable=False)
    phatSinh = Column(Float, nullable=True)
    noCuoi = Column(Float, nullable=True)

    def __str__(self):
        return self


class DonVi(db.Model):
    __tablename__ = "DonVi"
    maDonVi = Column(Integer, primary_key=True, autoincrement=True)
    tenDonVi = Column(String(20), nullable=False)
    vietTat = Column(String(10), nullable=False)

    def __str__(self):
        return self


class ThuTien(db.Model):
    __tablename__ = "ThuTien"
    maThu = Column(Integer, primary_key=True, autoincrement=True)
    soDienThoai = Column(String(10), nullable=False)
    email = Column(String(30), nullable=False)
    diaChi = Column(String(100), nullable=False)
    ngayThu = Column(DateTime, nullable=False)
    soTien = Column(Integer, nullable=False)
    ma_DaiLy = Column(Integer, ForeignKey(DaiLy.id), nullable=False)
    def __str__(self):
        return self

class MatHang(db.Model):
    __tablename__ = "MatHang"
    maMatHang = Column(Integer, primary_key=True, autoincrement=True)
    tenMatHang = Column(String(20), nullable=False)

    def __str__(self):
        return self


class DonViModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()

        return redirect("/admin")

    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view((DonViModelView(Quan, db.session)))
admin.add_view((DonViModelView(LoaiDaiLy, db.session)))
admin.add_view((DonViModelView(DonVi, db.session)))
admin.add_view(LogoutView(name="Logout"))

if __name__ == "__main__":
    db.create_all()
