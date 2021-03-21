# coding=utf-8

import json

from app.models.base_token import BaseToken
from flask import jsonify, request
from functools import wraps
class BaseApi(object):
    """ Base View to create helpers common to all Webservices.
    """
    def __init__(self, request):
        """Constructor
        """
        self.request = request
        self.api_token = request.args.get('token')

    def validate_token(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            access_token = request.headers.get('access_token')
            if not access_token:
                return jsonify({'message': 'token is missing', 'data': {}}), 401
            try:
                query_token = BaseToken.query.filter(
                    BaseToken.api_token == access_token,
                    BaseToken.status == True
                ).first()
            except:
                return jsonify({'message': 'token is invalid', 'data': {}}), 401

            data =  {
                "base_customer": query_token.base_customer,
                "args": request.args.__dict__,
                "params": request.__dict__['view_args']
            }
            return f(data, *args, **kwargs)
        
        return decorated

    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass
