# Import flask and template operators
from flask import Flask, render_template, redirect
from flask_swagger_ui import get_swaggerui_blueprint

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_alembic import Alembic

# Define the WSGI application object
app = Flask(__name__)

SWAGGER_URL = '/api/doc'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "IndexOffy"
    }
)

# Configurations
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.modules.mod_home.controllers import mod_home
from app.modules.mod_user.controllers import mod_user

# Register blueprint(s)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
app.register_blueprint(mod_home)
app.register_blueprint(mod_user)

from app.models.api_token import ApiToken
from app.models.api_user import ApiUser
from app.models.base_customer import BaseCustomer

# Build the database:
# This will create the database file using SQLAlchemy
db.init_app(app)
migrate.init_app(app, db)
db.create_all()
