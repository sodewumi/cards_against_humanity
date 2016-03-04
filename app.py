from flask import Flask
import jinja2

app = Flask(__name__)
app.secret_key = 'public key'
app.jinja_env .undefined = jinja2.StrictUndefined

@app.route("/")
def index():
	return "Hello World"


if __name__ == "__main__":
	app.run(debug=True)
