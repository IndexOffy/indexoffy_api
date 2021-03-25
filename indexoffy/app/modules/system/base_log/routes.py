# coding=utf-8

from app import db
from flask import Blueprint, jsonify

from app.api.utils.decorators import BaseDecorator

mod_base_log = Blueprint('base_logs', __name__, url_prefix='/base_logs')


class ViewBaseLog(object):
    """
    """
    def __init__(self):
        super().__init__()

    @mod_base_log.route('/<id>', methods=['GET'])
    @BaseDecorator.validate_token_system
    def get(system, id):
        return jsonify({"message": "successfully", "data": system}), 200

    @mod_base_log.route('/<id>', methods=['POST'])
    @BaseDecorator.validate_token_system
    def post(system, id):
        return jsonify({"message": "successfully", "data": system}), 201

    @mod_base_log.route('/<id>', methods=['PUT'])
    @BaseDecorator.validate_token_system
    def put(system, id):
        return jsonify({"message": "successfully", "data": system}), 201
