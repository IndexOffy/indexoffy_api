# coding=utf-8

import inspect

from app import db
from flask import jsonify
from app.models.base_log import BaseLog


class BaseResponse(object):
    """ Base View to Response common to all Webservices.
    """
    def __init__(self, data=None, base_customer=None, model_class=None, function=None):
        """Constructor
        """
        base_log_data = BaseLog.default(self)

        if base_customer:
            base_log_data['base_customer'] = base_customer

        if data:
            base_log_data['operation'] = data['request'].environ['REQUEST_METHOD']
            base_log_data['model_class'] = model_class
            base_log_data['model_id'] = data['id']
            base_log_data['function'] = function
            base_log_data['args'] = str(data['args'])
            base_log_data['params'] = str(data['params'])
            base_log_data['route'] = data['request'].url

        self.base_log_data = base_log_data

        self.data_return = {
            "successfully_fetched": {
                "status": 201,
                "status_message": "success",
                "message": "Successful Fetched"
                },
            "successfully_created": {
                "status": 201,
                "status_message": "success",
                "message": "Successful Created"
                },
            "server_error": {
                "status": 500,
                "status_message": "fail",
                "message": "Internal Server Error"
                },
            "user_dont_exist": {
                "status": 404,
                "status_message": "fail",
                "message": "User Don't Exist"
                },
            "base_customer_is_missing": {
                "status": 401,
                "status_message": "fail",
                "message": "BaseCustomer is Missing"
                },
            "token_is_missing": {
                "status": 401,
                "status_message": "fail",
                "message": "Token is Missing"
                },
            "token_is_invalid": {
                "status": 401,
                "status_message": "fail",
                "message": "Token is Invalid"
                },
            "permission_denied": {
                "status": 401,
                "status_message": "fail",
                "message": "Permission Denied"
                },
            "invalid_data": {
                "status": 422,
                "status_message": "fail",
                "message": "Unprocessable Entity"
                },
            "data_not_found": {
                "status": 404,
                "status_message": "fail",
                "message": "Not Found"
                },
            "method_not_allowed": {
                "status": 405,
                "status_message": "fail",
                "message": "Method Not Allowed"
                },
            "method": {
                "status": 200,
                "status_message": "ok",
                "message": "Method"
                },
        }

    def create_log(self):
        try:
            base_log = BaseLog(**self.base_log_data)
            db.session.add(base_log)
            db.session.commit()
        except Exception as error:
            db.session.rollback()

    def successfully_created(self, result=None, limit=None, quantity=None):
        status = 201
        status_message = "success"
        message = "Successful Created"
        try:
            self.base_log_data["message"] = message
            self.base_log_data["status"] = status
            self.base_log_data['result'] = str(result)
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify(
                {
                    "data": {
                        "status": status_message,
                        "message": message,
                        "limit": limit,
                        "total": quantity
                    },
                    "result": result
                }
            ), status

    def successfully_fetched(self, result=None, limit=None, quantity=None):
        status = 200
        status_message = "success"
        message = "Successful Request"
        try:
            self.base_log_data["message"] = message
            self.base_log_data["status"] = status
            self.base_log_data['result'] = str(result)
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify(
                {
                    "data": {
                        "status": status_message,
                        "message": message,
                        "limit": limit,
                        "total": quantity
                    },
                    "result": result
                }
            ), status
    
    def server_error(self, result=None, limit=None, quantity=None):
        status = 500
        status_message = "fail"
        message = "Internal Server Error"
        try:
            self.base_log_data["message"] = message
            self.base_log_data["status"] = status
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify(
                {
                    "data": {
                        "status": status_message,
                        "message": message,
                        "limit": limit,
                        "total": quantity
                    },
                    "result": None
                }), status

    def user_dont_exist(self, result=None, limit=None, quantity=None):
        status = 404
        status_message = "fail"
        message = "User Don't Exist"
        try:
            self.base_log_data["message"] = message
            self.base_log_data["status"] = status
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify(
                {
                    "data": {
                        "status": status_message,
                        "message": message,
                        "limit": limit,
                        "total": quantity
                    },
                    "result": None
                }), status


    def base_customer_is_missing(self, result=None, limit=None, quantity=None):
        status = 401
        status_message = "fail"
        message = 'BaseCustomer is Missing'
        try:
            self.base_log_data["message"] = message
            self.base_log_data["status"] = status
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify(
                {
                    "data": {
                        "status": status_message,
                        "message": message,
                        "limit": limit,
                        "total": quantity
                    },
                    "result": None
                }), status

    def token_is_missing(self, result=None, limit=None, quantity=None):
        status = 401
        status_message = "fail"
        message = 'Token is Missing'
        try:
            self.base_log_data["message"] = message
            self.base_log_data["status"] = status
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify(
                {
                    "data": {
                        "status": status_message,
                        "message": message,
                        "limit": limit,
                        "total": quantity
                    },
                    "result": None
                }), status

    def token_is_invalid(self, result=None, limit=None, quantity=None):
        status = 401
        status_message = "fail"
        message = 'Token is Invalid'
        try:
            self.base_log_data["message"] = message
            self.base_log_data["status"] = status
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify(
                {
                    "data": {
                        "status": status_message,
                        "message": message,
                        "limit": limit,
                        "total": quantity
                    },
                    "result": None
                }), status

    def permission_denied(self, result=None, limit=None, quantity=None):
        status = 401
        status_message = "fail"
        message = "Permission Denied"
        try:
            self.base_log_data["message"] = message
            self.base_log_data["status"] = status
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify(
                {
                    "data": {
                        "status": status_message,
                        "message": message,
                        "limit": limit,
                        "total": quantity
                    },
                    "result": None
                }), status

    def invalid_data(self, result=None, limit=None, quantity=None):
        status = 422
        status_message = "fail"
        message = "Unprocessable Entity"
        try:
            self.base_log_data["message"] = message
            self.base_log_data["status"] = status
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify(
                {
                    "data": {
                        "status": status_message,
                        "message": message,
                        "limit": limit,
                        "total": quantity
                    },
                    "result": None
                }), status

    def data_not_found(self, result=None, limit=None, quantity=None):
        status = 404
        status_message = "fail"
        message = "Not Found"
        try:
            self.base_log_data["message"] = message
            self.base_log_data["status"] = status
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify(
                {
                    "data": {
                        "status": status_message,
                        "message": message,
                        "limit": limit,
                        "total": quantity
                    },
                    "result": None
                }), status

    def method_not_allowed(self, result=None, limit=None, quantity=None):
        status = 405
        status_message = "fail"
        message = "Method Not Allowed"
        try:
            self.base_log_data["message"] = message
            self.base_log_data["status"] = status
            self.create_log()
        except Exception as error:
            print(error)
        finally:
            return jsonify(
                {
                    "data": {
                        "status": status_message,
                        "message": message,
                        "limit": limit,
                        "total": quantity
                    },
                    "result": None
                }), status

    def method(self, result=None, limit=None, quantity=None):
        """
        """
        return self.create_response(
            name="method",
            result=result,
            limit=limit,
            quantity=quantity
        )

    def create_response(self, name, result=None, limit=None, quantity=None):
        """
        """
        for item in self.data_return:
            if item == name:
                data_return = self.data_return[item]

        return jsonify(
            {
                "data": {
                    "status": data_return["status_message"],
                    "message": data_return["message"],
                    "limit": limit,
                    "total": quantity
                },
                "result": result
            }), data_return["status"]