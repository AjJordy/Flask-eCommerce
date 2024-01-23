from flask import request
from flask_login import login_user, login_required, logout_user

from application import application, login_manager
from model.User import User


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


@application.route('/login', methods=["POST"])
def login():
	data = request.json
	user = User.query.filter_by(username=data.get("username")).first()

	if user and data.get("password") == user.password:
		login_user(user)
		return jsonify({"message":"Logged successfully"})
	return jsonify({"message":"Unauthorized. Invalid credentials"}), 401


@application.route('/logout', methods=["POST"])
@login_required
def logout():
	logout_user()
	return jsonify({"message":"Logout successfully"})


@application.route('/api/products/add', methods=["POST"])
@login_required
def add_product():
	data = request.json
	if 'name' in data and 'price' in data:
		product = Product(name=data['name'], price=data['price'], description=data.get('description', ""))
		db.session.add(product)
		db.session.commit()
		return jsonify({"message":"Product added successfully"})
	return jsonify({"message":"Invalid product data"}), 400