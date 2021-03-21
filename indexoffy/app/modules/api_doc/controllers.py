# Import flask dependencies
from flask import Blueprint, redirect, url_for

mod_doc = Blueprint('', __name__, url_prefix='')

# Set the route and accepted methods
@mod_doc.route('/', methods=['GET'])
def home():
    return redirect("/docs/")