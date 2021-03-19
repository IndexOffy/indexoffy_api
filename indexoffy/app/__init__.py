# Import flask and template operators
from flask import Flask, render_template, redirect
from flask_swagger_ui import get_swaggerui_blueprint

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

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
migrate = Migrate()

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.controllers import mod_auth
from app.mod_home.controllers import mod_home

# Register blueprint(s)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
app.register_blueprint(mod_home)
app.register_blueprint(mod_auth)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()