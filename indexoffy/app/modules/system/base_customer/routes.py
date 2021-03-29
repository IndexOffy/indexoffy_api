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
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def get_all(data, user):
        return BaseResponse().invalid_data()

    @mod_base_customer.route('/', methods=['POST'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def post(data, user):
        return ControlerBaseCustomer(data=data, user=user).post()

    @mod_base_customer.route('/<id>', methods=['GET'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def get(data, user, id):
        return ControlerBaseCustomer(data=data, user=user).get(model_id=id)

    @mod_base_customer.route('/<id>', methods=['PUT'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def put(data, user, id):
        return ControlerBaseCustomer(data=data).put(model_id=id)
