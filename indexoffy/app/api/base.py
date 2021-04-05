# coding=utf-8

from app import db
from flask import jsonify, request
from functools import wraps
from traceback import format_exc

from app.api.utils.responses import BaseResponse


class BaseApi(object):
    """ Base View to create helpers common to all Webservices.
    """
    def __init__(self, base_customer, data=None):
        """Constructor
        """
        self.data = data
        self.params = {}
        self.model_class = None
        self.base_schema = None
        self.base_schemas = None
        self.base_customer = base_customer
        self.response = BaseResponse(base_customer=base_customer)


    def get_all(self):
        """ Method GET All
        """
        # Limiting the query to 50 records.
        request_limit = 50 if int(self.data['limit']) > 50 else self.data['limit']

        # Adequacy of received parameters
        for item in self.base_schema.fields:
            option = self.data['params'].get(item)
            if option:
                self.params[item] = option

        try:
            query_model = self.model_class.query
            for item in self.params:
                query_model = query_model.filter(getattr(self.model_class, item) == self.params[item])
            query_model = query_model.all()

            if query_model:
                result = self.base_schemas.dump(query_model)
                return self.response.successfully_fetched(result=result, limit=request_limit, quantity=len(result))
        except:
            return self.response.server_error()
        
        return self.response.successfully_fetched()

    def get(self, model_id):
        """ Method GET
        """
        try:
            query = self.model_class.query \
                .filter(
                    self.model_class.id == model_id,
                    self.model_class.base_customer == self.base_customer) \
                .first()
            if query:
                result = self.base_schema.dump(query)
                return self.response.successfully_fetched(result=result, limit=1, quantity=1)
        except:
            return self.response.server_error()

        return self.response.data_not_found()

    def put(self, model_id, data=None):
        """ Method PUT
        """
        # body => Request API / data => System
        base_data = data if data else self.data['body']
        model_data = self.model_class.query.get(model_id)

        # Checks if there is a record.
        if not model_data:
            return self.response.user_dont_exist()

        # Check the contents of the registry.
        if "id" in base_data:
            return self.response.invalid_data()

        try:
            for item in base_data:
                setattr(model_data, item, base_data[item])
            db.session.commit()
            result = self.base_schema.dump(model_data)
            return self.response.successfully_fetched(result=result)
        except Exception as error:
            db.session.rollback()
            return self.response.server_error()

    def post(self, data=None):
        """ Method POST
        """
        # body => Request API / data => System
        base_data = data if data else self.data['body']

        try:
            base_data = self.model_class(**base_data)
            db.session.add(base_data)
            db.session.commit()
            result = self.base_schema.dump(base_data)

            return self.response.successfully_fetched(result=result)
        except Exception as error:
            db.session.rollback()
            return self.response.server_error()

    def delete(self):
        """ Method DELETE
        """
        return self.response.successfully_fetched()
