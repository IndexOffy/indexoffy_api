# Import flask dependencies
from flask import Blueprint, redirect, url_for

mod_home = Blueprint('', __name__, url_prefix='')

# Set the route and accepted methods
@mod_home.route('/', methods=['GET'])
def home():
    return redirect("/api/doc/")