from flask import render_template
from app import create_app
from app.extensions import cache


app = create_app()


@app.route("/home")
@app.route("/")
@cache.cached()
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
