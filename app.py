"""
Smart Restaurant Management Dashboard
DevOps + Docker + Jenkins Demonstration Project
"""

from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

# Sample in-memory order storage
orders = []

# Homepage
@app.route("/")
def home():
    return render_template("index.html")


# Menu page
@app.route("/menu")
def menu():
    food_items = [
        {"name": "Burger", "price": 12},
        {"name": "Pizza", "price": 18},
        {"name": "Pasta", "price": 15},
        {"name": "Fries", "price": 7},
    ]

    return render_template("menu.html", items=food_items)


# Orders page
@app.route("/orders", methods=["GET", "POST"])
def manage_orders():

    if request.method == "POST":

        customer = request.form.get("customer")
        item = request.form.get("item")

        if customer and item:
            orders.append({
                "customer": customer,
                "item": item
            })

    return render_template("orders.html", orders=orders)


# Analytics page
@app.route("/analytics")
def analytics():

    total_orders = len(orders)

    return render_template(
        "analytics.html",
        total_orders=total_orders
    )


# API endpoint
@app.route("/api/orders")
def api_orders():
    return jsonify(orders)


# Intentional Bandit issue for demonstration
def insecure_function():
    """
    Intentional insecure code for Bandit scan.
    """
    subprocess.Popen("dir", shell=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)