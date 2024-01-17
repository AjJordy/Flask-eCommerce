from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecomerce.db'

db = SQLAlchemy(app)


class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), nullable=False)
	price = db.Column(db.Float, nullable=False)
	description = db.Column(db.Text, nullable=True)


@app.route('/api/products/add', methods=["POST"])
def add_product():
	data = request.json
	if 'name' in data and 'price' in data:
		product = Product(name=data['name'], price=data['price'], description=data.get('description', ""))
		db.session.add(product)
		db.session.commit()
		return jsonify({"message":"Product added successfully"})
	return jsonify({"message":"Invalid product data"}), 400


@app.route('/api/products/delete/<int:>')
def delete_product():


@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == "__main__":
    app.run(debug=True)