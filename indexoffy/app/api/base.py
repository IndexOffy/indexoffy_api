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
        self.model_class = None
        self.base_schema = None
        self.base_schemas = None
        self.base_customer = base_customer
        self.response = BaseResponse(base_customer=base_customer)


    def get_all(self):
        """ Method GET All
        """
        request_limit = 50 if int(self.data['limit']) > 50 else self.data['limit']

        try:
            users = self.model_class.query.limit(request_limit).all()
            if users:
                result = self.base_schemas.dump(users)
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

    def put(self, model_id):
        """ Method PUT
        """
        model_data = self.model_class.query.get(model_id)

        # Verifica se existe registro.
        if not model_data:
            return self.response.user_dont_exist()

        # Verificar conteúdo do registro.
        if "id" in self.data['body']:
            return self.response.invalid_data()

        try:
            for item in self.data['body']:
                setattr(model_data, item, self.data['body'][item])
            db.session.commit()
            result = self.base_schema.dump(model_data)
            return self.response.successfully_fetched(result=result)
        except Exception as error:
            db.session.rollback()
            return self.response.server_error()

    def post(self):
        """ Method POST
        """
        try:
            base_data = self.model_class(**self.data['body'])
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
