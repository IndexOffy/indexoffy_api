# coding=utf-8

from app import db
from flask import Blueprint, jsonify

from app.api.utils.decorators import BaseDecorator
from app.modules.system.base_error.controllers import ControlerBaseError

mod_base_error = Blueprint('base_errors', __name__, url_prefix='/base_errors')


class ViewBaseError(object):
    """
    """
    def __init__(self):
        super().__init__()

    @mod_base_error.route('/', methods=['GET'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def get_all(user, data):
        return ControlerBaseError(data=data).get()

    @mod_base_error.route('/', methods=['POST'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def post(user, data):
        return ControlerBaseError(data=data).post()

    @mod_base_error.route('/<id>', methods=['GET'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def get(user, data, id):
        return ControlerBaseError(data=data).get(model_id=id)

    @mod_base_error.route('/<id>', methods=['PUT'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def put(user, data, id):
        return ControlerBaseError(data=data).put(model_id=id)
