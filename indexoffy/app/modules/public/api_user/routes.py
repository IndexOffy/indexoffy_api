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
    @BaseDecorator.validate_token
    @BaseDecorator.system
    def get_all(data, user):
        return BaseResponse().method_not_allowed()

    @mod_user.route('/', methods=['POST'])
    @BaseDecorator.validate_token
    @BaseDecorator.system
    def post(data, user):
        return BaseResponse().method_not_allowed()

    @mod_user.route('/<id>', methods=['GET'])
    @BaseDecorator.validate_token
    @BaseDecorator.system
    def get(data, user, id):
        return ControlerUser(base_customer=user, data=data).get(model_id=id)

    @mod_user.route('/<id>', methods=['PUT'])
    @BaseDecorator.validate_token
    @BaseDecorator.system
    def put(data, user, id):
        return BaseResponse().method_not_allowed()