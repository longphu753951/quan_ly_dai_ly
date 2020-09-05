from flask_admin import BaseView, expose
from flask import redirect
from app import db, admin
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DECIMAL
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, current_user, logout_user


class User(db.Model, UserMixin):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tenDangNhap = Column(String(50), nullable=False)
    tenUser = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    matKhau = Column(String(50), nullable=False)
    loaiTaiKhoan = Column(Boolean, nullable=False)

    def __str__(self):
        return self.tenDangNhap


class Quan(db.Model):
    __tablename__ = "Quan"
    maQuan = Column(Integer, primary_key=True, autoincrement=True)
    tenQuan = Column(String(50), nullable=False)
    soDaiLiHienCo = Column(Integer, nullable=False)
    soDaiLiToiDa = Column(Integer, nullable=False)

    def __str__(self):
        return self.tenDangNhap


class LoaiDaiLy(db.Model):
    __tablename__ = "LoaiDaiLy"
    maLoai = Column(Integer, primary_key=True, autoincrement=True)
    tenLoai = Column(String(20), nullable=False)
    tienNoToiDa = Column(DECIMAL, nullable=False)

    def __str__(self):
        return self.tenDangNhap


class DonVi(db.Model):
    __tablename__ = "MaDonVi"
    maDonVi = Column(Integer, primary_key=True, autoincrement=True)
    tenDonVi = Column(String(20), nullable=False)
    vietTat = Column(String(10), nullable=False)

    def __str__(self):
        return self.tenDangNhap

    def is_accessible(self):
        return current_user.is_authenticated


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
