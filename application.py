from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/<string:name>")
def greeting(name):
    return render_template("greeting.html", name=name)

if __name__ == "__main__":
    app.run()
