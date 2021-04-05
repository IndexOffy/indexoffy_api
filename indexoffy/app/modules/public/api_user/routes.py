# coding=utf-8

from app import db
from flask import Blueprint, jsonify

from app.api.utils.responses import BaseResponse
from app.api.utils.decorators import BaseDecorator

from app.modules.public.api_user.controllers import ControlerUser

mod_user = Blueprint('users', __name__, url_prefix='/users')


class ViewUser(object):
    """
    """
    def __init__(self):
        super().__init__()

    @mod_user.route('/', methods=['GET'])
    @BaseDecorator.system
    @BaseDecorator.validate_token
    def get_all(user, data):
        return BaseResponse(base_customer=user, data=data).method_not_allowed()

    @mod_user.route('/', methods=['POST'])
    @BaseDecorator.system
    @BaseDecorator.validate_token
    def post(user, data):
        return BaseResponse(base_customer=user, data=data).method_not_allowed()

    @mod_user.route('/<id>', methods=['GET'])
    @BaseDecorator.system
    @BaseDecorator.validate_token
    def get(user, data, id):
        return ControlerUser(base_customer=user, data=data).get(model_id=id)

    @mod_user.route('/<id>', methods=['PUT'])
    @BaseDecorator.system
    @BaseDecorator.validate_token
    def put(user, data, id):
        return BaseResponse(base_customer=user, data=data).method_not_allowed()