# coding=utf-8

import ast

from app import db
from app.api.utils.responses import BaseResponse

class BaseUtils(object):
    """ Base View to Utils common to all Webservices.
    """
    def __init__(self, *args, **kwargs):
        """Constructor
        """

    def get_data(request):
        """
        """
        request_body = request.data.decode("UTF-8")
        request_id = request.view_args.get('id', None)
        base_customer = request.headers.get('base_customer', None)
        access_token = request.headers.get('access_token', None)

        if request_id:
            if request_id.isnumeric() == False:
                request_id = None
            else:
                request_id = int(request_id)

        if base_customer:
            if base_customer.isnumeric() == False:
                base_customer = None
            else:
                base_customer = int(base_customer)

        if request_body:
            request_body = ast.literal_eval(request_body)
        else:
            request_body = {}

        return {
            "id": request_id,
            "body": request_body,
            "params": request.args,
            "args": request.view_args,
            "access_token": access_token,
            "base_customer": base_customer,
            "limit": request.args.get('limit', 50),
            "page": request.args.get('page', 1),
            "method": request.method,
            "request": request
        }