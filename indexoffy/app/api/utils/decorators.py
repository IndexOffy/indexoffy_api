# coding=utf-8

import ast

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
            model_id = request.headers.get('base_customer', "0")
            access_token = request.headers.get('access_token')

            if model_id.isnumeric() == False:
                return BaseResponse().invalid_data()
            else:
                response = BaseResponse(base_customer=model_id)

                try:
                    query_user = db.session.query(BaseCustomer.id) \
                        .filter(
                            BaseCustomer.id == model_id,
                        ).first()
                except:
                    return BaseResponse().server_error()

                if not query_user:
                    return response.permission_denied()

            if access_token == app.config['SECRET_KEY']:
                return f(query_user.id, *args, **kwargs)

            return response.permission_denied() 

        return decorated

    def system(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            request_id = request.view_args.get('id', "0")
            request_body = request.data.decode("UTF-8")

            if request_id != "0":
                if request_id.isnumeric() == False:
                    return BaseResponse().invalid_data()

            if request_body:
                request_body = ast.literal_eval(request_body)
            else:
                request_body = {}

            data= {
                "id": request_id,
                "body": request_body,
                "params": request.args,
                "args": request.view_args,
                "limit": request.args.get('limit', 50),
                "page": request.args.get('page', 1),
                "request": request,
            }
            
            return f(data, *args, **kwargs)
        
        return decorated