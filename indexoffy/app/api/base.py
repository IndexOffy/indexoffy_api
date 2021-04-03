# coding=utf-8

from app import db
from flask import jsonify, request
from functools import wraps

from app.api.utils.responses import BaseResponse


class BaseApi(object):
    """ Base View to create helpers common to all Webservices.
    """
    def __init__(self, base_customer, data=None):
        """Constructor
        """
        self.data = data
        self.model_class = None
        self.base_schema = None
        self.base_schemas = None
        self.base_customer = base_customer
        self.response = BaseResponse(
            base_customer=base_customer
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
