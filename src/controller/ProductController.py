from flask_login import login_required
from flask import jsonify, request
from application import application
from database import db
from model.Product import Product


@application.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_details(product_id: int):
	product = Product.query.get(product_id)
	if product:		
		return jsonify({
			"id": product.id,
			"name": product.name,
			"price": product.price,
			"description": product.description
		})
	return jsonify({"message": "Product not found"}), 404


@application.route('/api/products/update/<int:product_id>', methods=['PUT'])
@login_required
def update_product_details(product_id: int):
	product = Product.query.get(product_id)
	if not product:		
		return jsonify({"message": "Product not found"}), 404
	
	data = request.json
	if 'name' in data:
		product.name = data['name']
	
	if 'price' in data:
		product.price = data['price']

	if 'description' in data:
		product.description = data['description']
	
	db.session.commit()
	return jsonify({"message": "Product updated successfully"})


@application.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id: int):
	product = Product.query.get(product_id)
	if product:
		db.session.delete(product)
		db.session.commit()
		return jsonify({"message": "Product delete successfully"})
	return jsonify({"message": "Product not found"}), 404


@application.route('/api/products', methods=['GET'])
def get_product_details(product_id: int):
	products = Product.query.all()
	product_list = []
	for product in products:
		product_list.append({
			"id": product.id,
			"name": product.name,
			"price": product.price,
			"description": product.description
		})
	return jsonify(product_list)