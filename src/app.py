from flask import Flask, render_template
from card import Card

app = Flask(__name__)

#tento seznam karet se musí načítat z cookies
cardset = []

@app.route("/")
@app.route("/cardlet", methods=["GET"])


def cardlet():
    return render_template("cardlet.html")

@app.route("/cards", methods=["GET", "POST"])
def cards():
    return render_template("cards.html", cardset=cardset)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")