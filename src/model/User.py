from flask_login import UserMixin
from database import db

class User(db.model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), nullable=False, unique=True)
	password = db.Column(db.String(80), nullable=True)
	cart = db.relationship("CartItem", backref='user', lazy=True)