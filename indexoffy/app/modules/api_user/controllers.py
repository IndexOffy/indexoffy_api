# Import flask dependencies
from flask import Blueprint, jsonify, redirect, url_for, request

from app import db
from app.modules.api.base import BaseApi
from app.models.user import User, user_schema, users_schema

mod_user = Blueprint('users', __name__, url_prefix='/users')

# Set the route and accepted methods

class ViewUser(BaseApi):

    @mod_user.route('/', methods=['GET'])
    @BaseApi.validate_token
    def get_user_code(data):
        print(data)
        try:
            user = User.query.filter(User.code == data['params'].get('code')).first()
            if user:
                result = user_schema.dump(user)
                return jsonify({"message": "successfully fetched", "data": result}), 200
        except:
            return jsonify({"message": "error", "data":{}}), 500

        return jsonify({"message": "user don't exist", "data":{}}), 404

    @mod_user.route('/all', methods=['GET'])
    @BaseApi.validate_token_admin
    def get_all(data):
        try:
            users = User.query.all()
            if users:
                result = users_schema.dump(users)
            return jsonify({"message": "successfully fetched", "data": result}), 200
        except:
            return jsonify({"message": "error", "data":{}}), 500
        
        return jsonify({"message": "user don't exist", "data":{}}), 404

    @mod_user.route('/<id>', methods=['GET'])
    @BaseApi.validate_token_admin
    def get_user(data, *args, **kwargs):
        try:
            user = User.query.filter(User.id == data['params']['id']).first()
            if user:
                result = user_schema.dump(user)
                return jsonify({"message": "successfully fetched", "data": result}), 200
        except:
            return jsonify({"message": "error", "data":{}}), 500

        return jsonify({"message": "user don't exist", "data":{}}), 404