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
            user = "Admin"
            access_token = request.headers.get('access_token')
            base_customer = request.headers.get('base_customer')
            
            response = BaseResponse(
                model_class=str(__name__),
                function="validate_token_system",
            )

            if access_token == app.config['SECRET_KEY']:
                return f(user, *args, **kwargs)

        return decorated

    def system(f):
        @wraps(f)
        def decorated(*args, **kwargs):

            response = BaseResponse(
                model_class=str(__name__),
                function="system",
            )

            try:
                request_id = int(request.view_args.get('id', 0))
            except:
                return response.invalid_data()

            data= {
                "id": request_id,
                "limit": request.args.get('limit', 1),
                "page": request.args.get('page', 1),
                "request": request,
            }
            
            data = request.view_args.get('id', None)
            return f(data, *args, **kwargs)
        
        return decorated