# coding=utf-8

from app import db
from app.api.base import BaseApi

from app.models.base_error import BaseError, base_errors_schema

class ControlerBaseError(BaseApi):
    """
    """
    def __init__(self, base_customer):
        super().__init__(base_customer)

        self.base_customer = base_customer

    def get(self, model_id=None):
        try:
            query = BaseError.query \
                .filter(
                    BaseError.id == model_id,
                    BaseError.bustomer == self.base_customer) \
                .first()

            if query:
                result = base_errors_schema.dump(query)
                return self.response.successfully_fetched()
        except:
            return self.response.server_error()

        return self.response.user_dont_exist()

    def post(self, data):
        pass

    def put(self, id, data):
        pass
