# Importing necessary Flask modules
from flask import Flask, request, jsonify
from flask_cors import CORS  # Enables CORS 
from flask_sqlalchemy import SQLAlchemy  # for working with SQL databases

# Initializing Flask app
app = Flask(__name__)

# Enable CORS so frontend can communicate with backend
CORS(app)

# Set up SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

# Initialize SQLAlchemy with Flask app
db = SQLAlchemy(app)

# Define a Product model for the database
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)           # Unique ID for each product
    name = db.Column(db.String(80))                        # Product name
    description = db.Column(db.String(200))                # Description of the product
    price = db.Column(db.Float)                            # Product price

# Defining route to fetch products via API call
@app.route("/api/products")
def get_products():
    # Get the query parameter from the URL
    query = request.args.get("q", "").lower()
    
    # to find matching product names
    results = Product.query.filter(Product.name.ilike(f"%{query}%")).all()
    
    # Returns the matched products in JSON format
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "description": p.description,
        "price": p.price
    } for p in results])

# This function adds sample products to the database 
def seed_db():
    sample_products = [
    {"name": "Laptop", "description": "Gaming laptop with 16GB RAM", "price": 99999},
    {"name": "Laptop", "description": "Asus TUF gaming with 16GB RAM", "price": 105000},
    {"name": "Laptop", "description": "Asus Rog Strix g16-RTX 4060", "price": 200000},
    {"name": "Laptop", "description": "Dell G15 ", "price": 100000},
    {"name": "Laptop", "description": "HP Pavillion Gaming ", "price": 75000},
    {"name": "Laptop", "description": "HP Victus- RTX 3050", "price": 60000},
    {"name": "Smartphone", "description": "S23 Ultra ", "price": 125000},
      {"name": "Smartphone", "description": "Iphone 14 pro", "price": 100000},
        {"name": "Smartphone", "description": "Pixel 8 pro ", "price": 60000},
          {"name": "Smartphone", "description": "Pixel 7 pro ", "price": 40000},
    {"name": "Headphones", "description": "One plus nord Buds-2", "price": 2000},
      {"name": "Headphones", "description": "Galaxy buds-2", "price": 13000},
        {"name": "Headphones", "description": "Boat Rokerz", "price": 1999},
          {"name": "Headphones", "description": "Realme buds-2", "price": 699},
    {"name": "Smartwatch", "description": "Fitness smartwatch with heart rate monitor", "price": 7999},
     {"name": "Smartwatch", "description": "Dizo watch-2", "price": 2999},
      {"name": "Smartwatch", "description": "Realme watch-4", "price": 4999},
       {"name": "Smartwatch", "description": "Galaxy watch-4 LTE", "price": 40000},
    {"name": "Tablet", "description": "10-inch Android tablet", "price": 21999},
    {"name": "Bluetooth Speaker", "description": "Portable speaker with 12-hour battery", "price": 3499},
    {"name": "Wireless Mouse", "description": "Ergonomic mouse with fast response", "price": 1499},
    {"name": "Keyboard", "description": "Redragon Kumara-K552", "price": 2599},
    {"name": "Keyboard", "description": "Cosmic byte", "price": 3999},
    {"name": "Camera", "description": "DSLR camera with 24MP lens", "price": 74999}
]

    
    # Add each sample product to the database 
    for item in sample_products:
        db.session.add(Product(**item))
    
    # Commit the session to save changes
    db.session.commit()

# Entry point of the application
if __name__ == "__main__":
    # Creates an application context so databases operations can run
    with app.app_context():
        db.create_all()  
        
        # Seed database only if it's empty
        if not Product.query.first():
            seed_db()
    
    # Run the app in debug mode 
    app.run(debug=True)
