# coding=utf-8

from app import db
from flask import jsonify, request
from functools import wraps

from app.api.utils.responses import BaseResponse


class BaseApi(object):
    """ Base View to create helpers common to all Webservices.
    """
    def __init__(self, data, user):
        """Constructor
        """
        self.data = data
        self.user = user
        self.model_class = None
        self.base_schema = None
        self.base_schemas = None
        self.base_customer = user.base_customer
        self.response = BaseResponse(
            data=data,
            user=user,
            model_class=str(self.model_class)
        )

    def get(self, model_id):
        try:
            query = self.model_class.query \
                .filter(
                    self.model_class.id == model_id,
                    self.model_class.base_customer == self.base_customer) \
                .first()
            if query:
                result = self.base_schema.dump(query)
                return self.response.successfully_fetched(result=result)
        except:
            return self.response.server_error()

        return self.response.data_not_found()

    def put(self, model_id):
        return self.response.successfully_fetched()

    def post(self):
        return self.response.successfully_fetched()

    def delete(self):
        return self.response.successfully_fetched()
