# Import flask dependencies
from flask import Blueprint, redirect, url_for

mod_api = Blueprint('', __name__, url_prefix='')

# Set the route and accepted methods
@mod_api.route('/', methods=['GET'])
def home():
    return redirect("/doc/")