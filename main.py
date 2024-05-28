from flask import Flask, render_template, redirect

app = Flask(__name__)

LINKS = {123456: "https://google.com"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/go/<int:code>")
def go(code):
    if code in LINKS:
        return redirect(LINKS[code])
    else:
        return "Link not found"

if __name__ == '__main__':
    app.run()