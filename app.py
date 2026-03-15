from flask import Flask, render_template, request

app = Flask(__name__)

products = []

@app.route("/", methods=["GET","POST"])
def index():

    if request.method == "POST":
        name = request.form["name"]
        qty = request.form["qty"]
        price = request.form["price"]

        products.append([name, qty, price])

    return render_template("index.html", products=products)

app.run(debug=True)