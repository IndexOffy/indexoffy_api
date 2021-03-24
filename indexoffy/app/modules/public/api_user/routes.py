# Import flask dependencies
from flask import Blueprint, jsonify, redirect, url_for, request

from app import db
from app.api.utils.decorators import BaseDecorator
from app.api.utils.responses import BaseResponse

from app.models.user import User, user_schema, users_schema
from app.modules.public.api_user.controllers import ControlerUser

mod_user = Blueprint('users', __name__, url_prefix='/users')

# Set the route and accepted methods

class ViewUser(object):
    """
    """
    def __init__(self):
        super().__init__()

    @mod_user.route('/', methods=['GET'])
    @BaseDecorator.validate_token
    def get_user(data):
        return ControlerUser(data=data).get()

    @mod_user.route('/all', methods=['GET'])
    @BaseDecorator.validate_token_admin
    def get_all_admin(data):
        return ControlerUser(data=data).get_all()
