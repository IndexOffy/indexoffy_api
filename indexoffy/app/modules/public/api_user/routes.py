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
        """
        """
        response = BaseResponse(
            data=data,
            model_class=str(__name__),
            function="get_all_admin",
            operation=str(['GET'])
        )
        try:
            users = User.query.all()
            if users:
                result = users_schema.dump(users)
                return response.successfully_fetched(result=result)
        except:
            return BaseResponse().server_error()
        
        return BaseResponse().user_dont_exist()

    @mod_user.route('/<id>', methods=['GET'])
    @BaseDecorator.validate_token_admin
    def get_user_admin(data, *args, **kwargs):
        """
        """
        response = BaseResponse(
            data=data,
            model_class=str(__name__),
            function="get_user_admin",
            operation=str(['GET'])
        )
        try:
            user = User.query.filter(User.id == data['args']['id']).first()
            if user:
                result = user_schema.dump(user)
                return response.successfully_fetched(result=result)
        except:
            return BaseResponse().server_error()

        return BaseResponse().user_dont_exist()