from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# Sample Data
products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

# TODO: Implement homepage route that returns a welcome message

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Product API", "resource_endpoint": "/products"})

# TODO: Implement GET /products route that returns all products or filters by category

# methods parameter is an array of all methods that can be used for the API
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    if category:
        filtered = [product for product in products if product["category"] == category]
        return jsonify(filtered), 200
    return jsonify(products), 200

# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>")
def get_product_by_id(id):
    for product in products:
        if product["id"] == id:
            return jsonify(product), 200
    return jsonify({"message": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
