from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json_products(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception:
        return None

def read_csv_products(filepath):
    products = []
    try:
        with open(filepath, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert id and price to appropriate types
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except Exception:
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    prod_id = request.args.get('id', type=int)
    error = None
    products = []

    if source == 'json':
        products = read_json_products('products.json')
    elif source == 'csv':
        products = read_csv_products('products.csv')
    else:
        error = "Wrong source"
        products = []

    if products is None:
        error = "Could not read data file."
        products = []

    # Filter by id if provided
    if not error and prod_id is not None:
        filtered = [p for p in products if p['id'] == prod_id]
        if filtered:
            products = filtered
        else:
            error = "Product not found"
            products = []

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)