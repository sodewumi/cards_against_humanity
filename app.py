from flask import Flask
from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user


from models import connect_to_db

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = secrets.DB_CONN_STRING
app.secret_key = "public for now"
# db = SQLAlchemy(app)


app.run(debug=True)
login_manager = LoginManager()
login_manager.init_app(app)
