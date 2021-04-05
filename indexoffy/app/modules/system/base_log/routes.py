# coding=utf-8

from app import db
from flask import Blueprint, jsonify

from app.api.utils.responses import BaseResponse
from app.api.utils.decorators import BaseDecorator
from app.modules.system.base_log.controllers import ControlerBaseLog

mod_base_log = Blueprint('base_logs', __name__, url_prefix='/base_logs')


class ViewBaseLog(object):
    """
    """
    def __init__(self):
        super().__init__()

    @mod_base_log.route('/', methods=['GET'])
    @BaseDecorator.system
    @BaseDecorator.validate_token_system
    def get_all(user, data):
        return ControlerBaseLog(data=data, base_customer=user).get_all()

    @mod_base_log.route('/', methods=['POST'])
    @BaseDecorator.system
    @BaseDecorator.validate_token_system
    def post(user, data):
        return ControlerBaseLog(base_customer=user,data=data).post()

    @mod_base_log.route('/<id>', methods=['GET'])
    @BaseDecorator.system
    @BaseDecorator.validate_token_system
    def get(user, data, id):
        return ControlerBaseLog(base_customer=user, data=data).get(model_id=id)

    @mod_base_log.route('/<id>', methods=['PUT'])
    @BaseDecorator.system
    @BaseDecorator.validate_token_system
    def put(user, data, id):
        return BaseResponse().method_not_allowed()