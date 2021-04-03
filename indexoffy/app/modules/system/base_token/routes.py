# coding=utf-8

from app import db
from flask import Blueprint, jsonify

from app.api.utils.responses import BaseResponse
from app.api.utils.decorators import BaseDecorator
from app.modules.system.base_token.controllers import ControlerBaseToken

mod_base_token = Blueprint('base_tokens', __name__, url_prefix='/base_tokens')


class ViewBaseToken(object):
    """
    """
    def __init__(self):
        super().__init__()

    @mod_base_token.route('/', methods=['GET'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def get_all(data, user):
        return BaseResponse().invalid_data()

    @mod_base_token.route('/', methods=['POST'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def post(data, user):
        return ControlerBaseToken(data=data, base_customer=user).post()

    @mod_base_token.route('/<id>', methods=['GET'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def get(data, user, id):
        return ControlerBaseToken(data=data, base_customer=user).get(model_id=id)

    @mod_base_token.route('/<id>', methods=['PUT'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def put(data, user, id):
        return ControlerBaseToken(data=data, base_customer=user).put(model_id=id)
