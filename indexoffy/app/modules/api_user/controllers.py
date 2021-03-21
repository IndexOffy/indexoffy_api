# Import flask dependencies
from flask import Blueprint, jsonify, redirect, url_for, request

from app import db
from app.modules.api.base import BaseApi
from app.modules.api.utils.responses import BaseResponse

from app.models.user import User, user_schema, users_schema

mod_user = Blueprint('users', __name__, url_prefix='/users')

# Set the route and accepted methods

class ViewUser(BaseApi):


    @mod_user.route('/', methods=['GET'])
    @BaseApi.validate_token
    def get_user(data):
        try:
            user = User.query.filter(User.code == data['params'].get('code')).first()
            if user:
                result = user_schema.dump(user)
                BaseResponse().successfully_fetched(result, data)
        except:
            return BaseResponse().server_error()

        return BaseResponse().user_dont_exist()

    @mod_user.route('/all', methods=['GET'])
    @BaseApi.validate_token_admin
    def get_all_admin(data):
        try:
            users = User.query.all()
            if users:
                result = users_schema.dump(users)
            BaseResponse().successfully_fetched(result)
        except:
            return BaseResponse().server_error()
        
        return BaseResponse().user_dont_exist()

    @mod_user.route('/<id>', methods=['GET'])
    @BaseApi.validate_token_admin
    def get_user_admin(data, *args, **kwargs):
        try:
            user = User.query.filter(User.id == data['params']['id']).first()
            if user:
                result = user_schema.dump(user)
                BaseResponse().successfully_fetched(result)
        except:
            return BaseResponse().server_error()

        return BaseResponse().user_dont_exist()