# Import flask dependencies
from flask import Blueprint, jsonify, redirect, url_for, request

from app.modules.api.base import BaseApi
from app.models.user import User

mod_user = Blueprint('users', __name__, url_prefix='/users')

# Set the route and accepted methods

class ViewUser(BaseApi):

    @mod_user.route('/', methods=['GET'])
    def user():
        return jsonify({"message": "code"})