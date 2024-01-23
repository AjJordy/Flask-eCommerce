from flask_sqlalchemy import SQLAlchemy
from application import application

application.config['SECRET_KEY'] = "minha_chave_123"
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecomerce.db'
db = SQLAlchemy(application)