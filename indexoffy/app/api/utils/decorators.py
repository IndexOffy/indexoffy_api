# coding=utf-8

import ast

from app import app, db
from flask import request
from functools import wraps
from app.api.utils.utils import BaseUtils

from app.models.base_token import BaseToken
from app.models.base_customer import BaseCustomer
from app.api.utils.responses import BaseResponse


class BaseDecorator(object):
    """ Base View to Decorators common to all Webservices.
    """

    def __init__(self):
        """Constructor
        """
        pass

    def validate_token(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            data = BaseUtils.get_data(request=request)
            response = BaseResponse(base_customer=data['base_customer'], data=data)

            try:
                query_token = db.session.query(BaseToken) \
                    .filter(
                        BaseToken.api_token == data["access_token"],
                        BaseToken.status == True
                    ).first()
            except:
                return response.permission_denied()

            if query_token:
                if query_token.base_customer != data['base_customer']:
                   return response.permission_denied() 

                return f(data['base_customer'], *args, **kwargs)

            return response.permission_denied()
        
        return decorated

    def validate_token_system(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            data = BaseUtils.get_data(request=request)
            response = BaseResponse(base_customer=data['base_customer'], data=data)

            try:
                query_user = db.session.query(BaseCustomer.id) \
                    .filter(
                        BaseCustomer.id == data['base_customer'],
                    ).first()
            except:
                return response.server_error()

                if not query_user:
                    return response.permission_denied()

            if data['access_token'] == app.config['SECRET_KEY']:
                return f(query_user.id, *args, **kwargs)

            return response.permission_denied() 

        return decorated

    def system(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            data = BaseUtils.get_data(request=request)
            response = BaseResponse(base_customer=data['base_customer'], data=data)

            if data["method"] in('PUT'):
                if not data["id"]:
                    return response.permission_denied()

            if not data["base_customer"]:
                return response.base_customer_is_missing()

            if not data["access_token"]:
                return response.token_is_missing()

            return f(data, *args, **kwargs)
        
        return decorated