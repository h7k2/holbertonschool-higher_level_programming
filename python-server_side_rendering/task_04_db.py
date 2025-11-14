from flask import Flask, render_template, request
import json
import csv
import sqlite3

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
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except Exception:
        return None

def read_sql_products(db_path, prod_id=None):
    products = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        if prod_id is not None:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id=?", (prod_id,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
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
    elif source == 'sql':
        products = read_sql_products('products.db', prod_id)
    else:
        error = "Wrong source"
        products = []

    if products is None:
        error = "Could not read data file."
        products = []

    # If SQL and id is provided but not found, handle error
    if not error and prod_id is not None and source != 'sql':
        filtered = [p for p in products if p['id'] == prod_id]
        if filtered:
            products = filtered
        else:
            error = "Product not found"
            products = []

    # For SQL, if id is provided but not found
    if not error and source == 'sql' and prod_id is not None and not products:
        error = "Product not found"
        products = []

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)