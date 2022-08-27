from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import flask_login


db = SQLAlchemy()
DB_NAME="database.db"


def createapp():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    app.config['SECRET_KEY']="YEAH BUDDY "
    from .view import view
    from .auth import auth

    app.register_blueprint(view,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User,Note
    create_db(app)
    return app

def create_db(app):
    if not path('web/'+ DB_NAME):
        db.create_all(app=app)
        print('created database')
