# Import flask dependencies
from flask import Blueprint, jsonify, redirect, url_for

from app.models.api_user import ApiUser

mod_user = Blueprint('user', __name__, url_prefix='/user')

# Set the route and accepted methods
@mod_user.route('/code/', methods=['GET'])
def user():
    return jsonify({"message": "code"})