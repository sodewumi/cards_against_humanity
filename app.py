import jinja2
from flask import Flask, session, flash, redirect, url_for, request, get_flashed_messages, jsonify, render_template
from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = secrets.DB_CONN_STRING
app.secret_key = "public for now"
# db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)