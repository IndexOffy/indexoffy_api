# Import flask dependencies
from flask import Blueprint, jsonify, redirect, url_for, request

from app import db
from app.api.base import BaseApi
from app.api.utils.responses import BaseResponse

from app.models.user import User, user_schema, users_schema

mod_user = Blueprint('users', __name__, url_prefix='/users')

# Set the route and accepted methods

class ViewUser(BaseApi):


    @mod_user.route('/', methods=['GET'])
    @BaseApi.validate_token
    def get_user(data):
        """
        """
        response = BaseResponse(
            data=data,
            model_class=str(__name__),
            function="get_user",
            operation=str(['GET'])
        )
        try:
            user = User.query.filter(User.code == data['params'].get('code')).first()
            if user:
                result = user_schema.dump(user)
                return response.successfully_fetched(result=result)
        except:
            return BaseResponse().server_error()

        return BaseResponse().user_dont_exist()

    @mod_user.route('/all', methods=['GET'])
    @BaseApi.validate_token_admin
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
    @BaseApi.validate_token_admin
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