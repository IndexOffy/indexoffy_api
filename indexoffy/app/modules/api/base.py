# coding=utf-8

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

    def validate_token(self):
        @wraps(self)
        def decorated(*args, **kwargs):
            token = request.args.get('token')
            if not token:
                return jsonify({'message': 'token is missing', 'data': {}}), 401
            try:
                data = BaseToken.query.filter(
                    BaseToken.api_token == token,
                    BaseToken.status == True,
                    BaseToken.api_type == 1
                ).first()
            except:
                return jsonify({'message': 'token is invalid', 'data': {}}), 401
            return self(data, *args, **kwargs)
        
        return decorated

    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass
