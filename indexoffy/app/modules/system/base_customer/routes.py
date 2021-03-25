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

    @mod_base_customer.route('/<id>', methods=['GET'])
    @BaseDecorator.validate_token_system
    def get(system, id):
        return jsonify({"message": "successfully", "data": system}), 200

    @mod_base_customer.route('/<id>', methods=['POST'])
    @BaseDecorator.validate_token_system
    def post(system, id):
        return jsonify({"message": "successfully", "data": system}), 201

    @mod_base_customer.route('/<id>', methods=['PUT'])
    @BaseDecorator.validate_token_system
    def put(system, id):
        return jsonify({"message": "successfully", "data": system}), 201
