from flask import Flask, render_template
import jinja2
from models import connect_to_db

app = Flask(__name__)
app.secret_key = 'public key'
app.jinja_env.undefined = jinja2.StrictUndefined


@app.route("/")
def index():
    return render_template("login.html")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)
