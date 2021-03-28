# coding=utf-8

from app import db
from app.api.base import BaseApi

from app.models.base_customer import BaseCustomer, base_schema, base_schemas

class ControlerBaseCustomer(BaseApi):
    """
    """
    def __init__(self, base_customer, data=None):
        super().__init__(base_customer)

        self.model_class = BaseCustomer
        self.base_schema = base_schema
        self.base_schemas = base_schemas

