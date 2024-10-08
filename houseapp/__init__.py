import secrets
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

DB_NAME = 'homeapp.db'
app = Flask(__name__, template_folder = 'templates')

app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db = SQLAlchemy(app)
app.app_context().push()
bcrypt = Bcrypt(app)

# login_manager = LoginManager(app)


from houseapp import routes