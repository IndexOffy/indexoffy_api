# coding=utf-8

from app import app, db
from flask import request
from functools import wraps

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
            access_token = request.headers.get('access_token')

            response = BaseResponse(
                model_class=str(__name__),
                function="validate_token",
            )

            if not access_token:
                return response.token_is_missing()
            try:
                query_user = db.session.query(
                        BaseToken.id.label('token_id'),
                        BaseToken.api_type.label('api_type'),
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
                    "request": request,
                    "user": query_user,
                }
                return f(data, *args, **kwargs)

            return response.permission_denied()
        
        return decorated

    def validate_token_admin(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            access_token = request.headers.get('access_token')

            response = BaseResponse(
                model_class=str(__name__),
                function="validate_token_admin",
            )

            if not access_token:
                return response.token_is_missing()
            try:
                query_user = db.session.query(
                        BaseToken.id.label('token_id'),
                        BaseToken.api_type.label('api_type'),
                        BaseCustomer.id.label('base_customer'),
                        BaseCustomer.name.label('name'),
                        BaseCustomer.email.label('email')
                    ) \
                    .join(BaseCustomer, BaseToken.base_customer==BaseCustomer.id) \
                    .filter(
                        BaseToken.api_token == access_token,
                        BaseToken.status == True,
                        BaseToken.api_type == 0
                    ).first()
            except:
                return response.token_is_invalid()

            if query_user:
                data =  {
                    "request": request,
                    "user": query_user,
                }
                return f(data, *args, **kwargs)

            return response.permission_denied() 
        
        return decorated

    def validate_token_system(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            data = request.view_args.get('id')
            access_token = request.headers.get('access_token')
            
            response = BaseResponse(
                model_class=str(__name__),
                function="validate_token_system",
            )

            if access_token == app.config['SECRET_KEY']:
                return f(data, *args, **kwargs)

            return response.permission_denied()
        
        return decorated