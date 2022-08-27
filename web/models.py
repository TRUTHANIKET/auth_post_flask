from . import db
from flask_login import UserMixin


class Note(db.model):
    id=db.column(db.Integer,primary_key=True)
    data=db.column(db.String(10000))
    date=db.column(db.DateTime(timezone=True),default=func.now())
    user_id=db.column(db.Integer,db.ForeignKey('user.id'))


class User(db.model,UserMixin):
    id=db.column(db.Integer,primary_key=True)
    email=db.column(db.String(150),unique=True)
    password=db.column(db.String(150))
    name=db.column(db.String(100))
    notes=db.relationship('Note')


