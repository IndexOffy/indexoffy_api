# coding=utf-8

from flask import jsonify
from app.models.base_log import BaseLog


class BaseResponse(object):
    """ Base View to create helpers common to all Webservices.
    """
    def __init__(self):
        """Constructor
        """
        pass

    def successfully_fetched(self, result, data):
        """ 
        """
        return jsonify({"message": "successfully fetched", "data": result}), 200
    
    def server_error(self):
        return jsonify({"message": "error", "data":{}}), 500

    def user_dont_exist(self):
        return jsonify({"message": "user don't exist", "data":{}}), 404

    def token_is_missing(self):
        return jsonify({'message': 'token is missing', 'data': {}}), 401

    def token_is_invalid(self):
        return jsonify({'message': 'token is invalid', 'data': {}}), 401