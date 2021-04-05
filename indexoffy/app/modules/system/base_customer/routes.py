# coding=utf-8

from app import db
from flask import Blueprint, jsonify

from app.api.utils.responses import BaseResponse
from app.api.utils.decorators import BaseDecorator

from app.modules.system.base_customer.controllers import ControlerBaseCustomer

mod_base_customer = Blueprint('base_customers', __name__, url_prefix='/base_customers')


class ViewBaseCustomer(object):
    """
    """
    def __init__(self):
        super().__init__()

    @mod_base_customer.route('/', methods=['GET'])
    @BaseDecorator.system
    @BaseDecorator.validate_token_system
    def get_all(user, data):
        return ControlerBaseCustomer(data=data, base_customer=user).get_all()

    @mod_base_customer.route('/', methods=['POST'])
    @BaseDecorator.system
    @BaseDecorator.validate_token_system
    def post(user, data):
        return ControlerBaseCustomer(data=data, base_customer=user).post()

    @mod_base_customer.route('/<id>', methods=['GET'])
    @BaseDecorator.system
    @BaseDecorator.validate_token_system
    def get(user, data, id):
        return ControlerBaseCustomer(data=data, base_customer=user).get(model_id=id)

    @mod_base_customer.route('/<id>', methods=['PUT'])
    @BaseDecorator.system
    @BaseDecorator.validate_token_system
    def put(user, data, id):
        return ControlerBaseCustomer(data=data, base_customer=user).put(model_id=id)
