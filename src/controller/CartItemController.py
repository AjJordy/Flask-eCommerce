from flask_login import login_required
from flask import jsonify, request
from application import application
from database import db
from model.CartItem import CartItem
from model.User import User
from model.Product import Product


@application.route('/api/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
	user = User.query.get(int(current_user.id))
	product = Product.query.get(product_id)
	if user and product:
		cart_item = CartItem(user_id=user.id, product_id=product.id)
		db.session.add(cart_item)
		db.session.commit()
		return jsonify({'message': 'Item added to the cart successfully'})
	return jsonify({'message': 'Failed to add item to the cart'}), 400


@application.route('/api/cart/remove/<int:product_id>', method=['DELETE'])
@login_required
def remove_from_cart(product_id):
	cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
	if cart_item:
		db.session.delete(cart_item)
		db.session.commit()
		return jsonify({'message': 'Item removed from the cart successfully'})
	return jsonify({'message': 'Failed to remove item to the cart'}), 400


@application.route('/api/cart', methods=['GET'])
@login_required
def view_cart():
	user = User.query.get(int(current_user.id))
	cart_items = user.cart
	cart_content = []
	for cart_item in cart_items:
		product = Product.query.get(cart_item.product_id) # TODO: CHANGE TO GET BETTER PERFORMANCE
		cart_content.append({
			'id': cart_item.id,
			'user_id': cart_item.user_id,
			'product_id': cart_item.product_id,
			'product_name': product.name,
			'product_price': product.price
		})
	return jsonify(cart_content)
	

@application.route('/api/cart/checkout', methods=['POST'])
@login_required
def checkout():
	user = User.query.get(int(current_user.id))
	cart_items = user.cart
	for cart_item in cart_items:
		db.session.delete(cart_item)
	db.session.commit()
	return jsonify({'message': 'Checkout successfully'})