# coding=utf-8

from app import db
from flask import Blueprint, jsonify

from app.api.utils.decorators import BaseDecorator

mod_base_customer = Blueprint('base_customers', __name__, url_prefix='/base_customers')


class ViewBaseCustomer(object):
    """
    """
    def __init__(self):
        super().__init__()

    @mod_base_customer.route('/', methods=['GET'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def get_all(user, data):
        return jsonify({"message": "successfully", "data": "get_all"}), 200

    @mod_base_customer.route('/', methods=['POST'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def post(user, data):
        return jsonify({"message": "successfully", "data": "post"}), 201

    @mod_base_customer.route('/<id>', methods=['GET'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def get(user, data, id):
        return jsonify({"message": "successfully", "data": "get"}), 200

    @mod_base_customer.route('/<id>', methods=['PUT'])
    @BaseDecorator.validate_token_system
    @BaseDecorator.system
    def put(user, data, id):
        return jsonify({"message": "successfully", "data": "put"}), 201




