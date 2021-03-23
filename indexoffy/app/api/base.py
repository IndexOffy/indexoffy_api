# coding=utf-8

from app import db
from flask import jsonify, request
from functools import wraps

from app.models.base_token import BaseToken
from app.models.base_customer import BaseCustomer
from app.api.utils.responses import BaseResponse


class BaseApi(object):
    """ Base View to create helpers common to all Webservices.
    """
    def __init__(self, request):
        """Constructor
        """
        self.api_token = request.headers.get('access_token')

    def validate_token(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            access_token = request.headers.get('access_token')

            response = BaseResponse(
                token=access_token,
                model_class=str(__name__),
                function="validate_token",
                operation=str(['GET'])
            )

            if not access_token:
                return response.token_is_missing()
            try:
                query_user = db.session.query(
                        BaseToken.id.label('token_id'),
                        BaseCustomer.id.label('base_customer'),
                        BaseCustomer.name.label('name'),
                        BaseCustomer.email.label('email')
                    ) \
                    .join(BaseCustomer, BaseToken.base_customer==BaseCustomer.id) \
                    .filter(
                        BaseToken.api_token == access_token,
                        BaseToken.status == True
                    ).first()
            except:
                return response.token_is_invalid()

            if query_user:
                data =  {
                    "args": request.__dict__['view_args'],
                    "user": query_user,
                    "params": request.args
                }
                return f(data, *args, **kwargs)
        
        return decorated

    def validate_token_admin(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            access_token = request.headers.get('access_token')

            response = BaseResponse(
                token=access_token,
                model_class=str(__name__),
                function="validate_token_admin",
                operation=str(['GET'])
            )

            if not access_token:
                return response.token_is_missing()
            try:
                query_user = db.session.query(
                        BaseToken.id.label('token_id'),
                        BaseCustomer.id.label('base_customer'),
                        BaseCustomer.name.label('name'),
                        BaseCustomer.email.label('email')
                    ) \
                    .join(BaseCustomer, BaseToken.base_customer==BaseCustomer.id) \
                    .filter(
                        BaseToken.api_token == access_token,
                        BaseToken.status == True
                    ).first()
            except:
                return response.token_is_invalid()

            if query_user:
                data =  {
                    "args": request.__dict__['view_args'],
                    "user": query_user,
                    "params": request.args
                }
                return f(data, *args, **kwargs)

            return response.permission_denied() 
        
        return decorated

    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass
