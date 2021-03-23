# coding=utf-8

import inspect

from app import db
from flask import jsonify
from app.models.base_log import BaseLog


class BaseResponse(object):
    """ Base View to Response common to all Webservices.
    """
    def __init__(self, token=None, data=None, model_class="model_class", function="function", operation="Error"):
        """Constructor
        """
        if not data:
            self.base_log_data = {
                "base_customer": 0,
                "user_name": "No name",
                "user_email": "No email",
                "operation": operation,
                "model_class": model_class,
                "function": function,
                "model_id": 0,
                "params": str({}),
                "args":  str({}),
                "api_token": None,
                "ip_address": None
            }
        else:
            self.base_log_data = {
                "base_customer": data['user'].base_customer,
                "user_name": data['user'].name,
                "user_email": data['user'].email,
                "operation": operation,
                "model_class": model_class,
                "function": function,
                "model_id": 0,
                "params": str(data['params']),
                "args":  str(data['args']),
                "api_token": None,
                "ip_address": None
            }

    def successfully_fetched(self, result=None):
        """ 
        """
        
        status = 200
        try:
            self.base_log_data["message"] = "successfully_fetched"
            self.base_log_data["status"] = status
            self.base_log_data["result"] = str(result)

            base_log = BaseLog(**self.base_log_data)
            db.session.add(base_log)
            db.session.commit()
        except Exception as error:
            print(error)

        return jsonify({"message": "successfully fetched", "data": result}), status
    
    def server_error(self, result=None):
        """ 
        """
        status = 500
        try:
            self.base_log_data["message"] = "server_error"
            self.base_log_data["status"] = status
            self.base_log_data["result"] = str(result)

            base_log = BaseLog(**self.base_log_data)
            db.session.add(base_log)
            db.session.commit()
        except Exception as error:
            print(error)

        return jsonify({"message": "error", "data":{}}), status

    def user_dont_exist(self, result=None):
        """ 
        """
        status = 404
        try:
            self.base_log_data["message"] = "user_dont_exist"
            self.base_log_data["status"] = status
            self.base_log_data["result"] = str(result)

            base_log = BaseLog(**self.base_log_data)
            db.session.add(base_log)
            db.session.commit()
        except Exception as error:
            print(error)

        return jsonify({"message": "user don't exist", "data":{}}), status

    def token_is_missing(self, result=None):
        """ 
        """
        status = 401
        try:
            self.base_log_data["message"] = "token_is_missing"
            self.base_log_data["status"] = status
            self.base_log_data["result"] = str(result)

            base_log = BaseLog(**self.base_log_data)
            db.session.add(base_log)
            db.session.commit()
        except Exception as error:
            print(error)

        return jsonify({'message': 'token is missing', 'data': {}}), status

    def token_is_invalid(self, result=None):
        """ 
        """
        status = 401
        try:
            self.base_log_data["message"] = "token_is_invalid"
            self.base_log_data["status"] = status
            self.base_log_data["result"] = str(result)

            base_log = BaseLog(**self.base_log_data)
            db.session.add(base_log)
            db.session.commit()
        except Exception as error:
            print(error)

        return jsonify({'message': 'token is invalid', 'data': {}}), status

    def permission_denied(self, result=None):
        """ 
        """
        status = 401
        try:
            self.base_log_data["message"] = "permission_denied"
            self.base_log_data["status"] = status
            self.base_log_data["result"] = str(result)

            base_log = BaseLog(**self.base_log_data)
            db.session.add(base_log)
            db.session.commit()
        except Exception as error:
            print(error)

        return jsonify({'message': 'permission denied', 'data': {}}), status