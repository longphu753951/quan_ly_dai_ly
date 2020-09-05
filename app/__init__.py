from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "Q\x87\xd5 v\x1f\x9e\xe4v\xc7\x8d\xbdI\xb8\xbf\xda!V"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/quan_ly_dai_ly?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)

admin = Admin(app=app, name="QUAN LY DAI LY", template_mode="bootstrap3")

login = LoginManager(app=app)
