from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SECRET_KEY'] = "minha_chave_123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecomerce.db'
db = SQLAlchemy(app)