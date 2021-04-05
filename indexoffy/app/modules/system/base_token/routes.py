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
    @BaseDecorator.system
    @BaseDecorator.validate_token_system
    def get_all(user, data):
        return ControlerBaseToken(data=data, base_customer=user).get_all()

    @mod_base_token.route('/', methods=['POST'])
    @BaseDecorator.system
    @BaseDecorator.validate_token_system
    def post(user, data):
        return ControlerBaseToken(data=data, base_customer=user).post()

    @mod_base_token.route('/<id>', methods=['GET'])
    @BaseDecorator.system
    @BaseDecorator.validate_token_system
    def get(user, data, id):
        return ControlerBaseToken(data=data, base_customer=user).get(model_id=id)

    @mod_base_token.route('/<id>', methods=['PUT'])
    @BaseDecorator.system
    @BaseDecorator.validate_token_system
    def put(user, data, id):
        return ControlerBaseToken(data=data, base_customer=user).put(model_id=id)
