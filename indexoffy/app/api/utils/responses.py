# coding=utf-8

import inspect

from app import db
from flask import jsonify
from app.models.base_log import BaseLog


class BaseResponse(object):
    """ Base View to Response common to all Webservices.
    """
    def __init__(self, data=None, model_class=None, function=None):
        """Constructor
        """
        base_log_data = BaseLog.default(self)

        if data:
            base_log_data['base_customer'] = data['user'].base_customer,
            base_log_data['user_name'] = data['user'].name,
            base_log_data['user_email'] = data['user'].email,
            base_log_data['operation'] = data['request'].environ['REQUEST_METHOD'],
            base_log_data['model_class'] = model_class,
            base_log_data['function'] = function,
            base_log_data['args'] = str(data['request'].view_args),
            base_log_data['route'] = data['request'].url,

        self.base_log_data = base_log_data

    def create_log(self):
        try:
            base_log = BaseLog(**self.base_log_data)
            db.session.add(base_log)
            db.session.commit()
        except Exception as error:
            pass

    def successfully_fetched(self, result=None, params=None):
        status = 200
        try:
            self.base_log_data["message"] = "successfully_fetched"
            self.base_log_data["status"] = status
            self.base_log_data["result"] = result
            self.base_log_data["params"] = params
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify({"message": "successfully fetched", "data": result}), status
    
    def server_error(self, result=None, params=None):
        status = 500
        try:
            self.base_log_data["message"] = "server_error"
            self.base_log_data["status"] = status
            self.base_log_data["result"] = result
            self.base_log_data["params"] = params
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify({"message": "error", "data":{}}), status

    def user_dont_exist(self, result=None, params=None):
        status = 404
        try:
            self.base_log_data["message"] = "user_dont_exist"
            self.base_log_data["status"] = status
            self.base_log_data["result"] = result
            self.base_log_data["params"] = params
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify({"message": "user don't exist", "data":{}}), status

    def token_is_missing(self, result=None, params=None):
        status = 401
        try:
            self.base_log_data["message"] = "token_is_missing"
            self.base_log_data["status"] = status
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify({'message': 'token is missing', 'data': {}}), status

    def token_is_invalid(self, result=None, params=None):
        status = 401
        try:
            self.base_log_data["message"] = "token_is_invalid"
            self.base_log_data["status"] = status
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify({'message': 'token is invalid', 'data': {}}), status

    def permission_denied(self, result=None, params=None):
        status = 401
        try:
            self.base_log_data["message"] = "permission_denied"
            self.base_log_data["status"] = status
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify({'message': 'permission denied', 'data': {}}), status

    def invalid_data(self, result=None, params=None):
        status = 422
        try:
            self.base_log_data["message"] = "invalid_data"
            self.base_log_data["status"] = status
            self.base_log_data["result"] = result
            self.base_log_data["params"] = params
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify({'message': 'invalid data', 'data': {}}), status
