from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

@app.route("/", methods=["GET","POST"])
def index():

    if request.method == "POST":
        name = request.form["name"]
        qty = request.form["qty"]
        price = request.form["price"]

        cursor.execute(
            "INSERT INTO products (name, quantity, price) VALUES (%s,%s,%s)",
            (name, qty, price)
        )
        conn.commit()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run()
