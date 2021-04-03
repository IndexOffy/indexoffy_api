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
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def get_all(data, user):
        return ControlerBaseLog(data=data, base_customer=user).get_all()

    @mod_base_log.route('/', methods=['POST'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def post(data, user):
        return ControlerBaseLog(base_customer=user,data=data).post()

    @mod_base_log.route('/<id>', methods=['GET'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def get(data, user, id):
        return ControlerBaseLog(base_customer=user, data=data).get(model_id=id)

    @mod_base_log.route('/<id>', methods=['PUT'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def put(data, user, id):
        return BaseResponse().method_not_allowed()