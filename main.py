from flask import Flask, render_template, redirect, request
import random

app = Flask(__name__)

LINKS = {1234: "https://google.com"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<int:code>")
def go(code):
    if code in LINKS:
        return redirect(LINKS[code])
    else:
        return render_template("created.html", code="Invalid code")
    
@app.route("/create", methods=["POST"])
def add():
    code = random.randint(1111, 9999)
    link = request.form["url"]
    LINKS[code] = link
    return render_template("created.html", code=code)

if __name__ == '__main__':
    app.run(host="0.0.0.0")