# coding=utf-8

from app import db
from app.api.base import BaseApi

from app.models.base_error import BaseError, base_schema, base_schemas

class ControlerBaseError(BaseApi):
    """
    """
    def __init__(self, base_customer, data=None):
        super().__init__(base_customer, data)

        self.model_class = BaseError
        self.base_schema = base_schema
        self.base_schemas = base_schemas
