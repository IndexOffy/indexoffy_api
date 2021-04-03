# coding=utf-8

from app import db
from app.api.base import BaseApi
from app.api.utils.responses import BaseResponse

from app.models.base_log import BaseLog, base_schema, base_schemas

class ControlerBaseLog(BaseApi):
    """
    """
    def __init__(self, base_customer, data=None):
        super().__init__(base_customer, data)

        self.model_class = BaseLog
        self.base_schema = base_schema
        self.base_schemas = base_schemas

        self.response = BaseResponse(
            base_customer=base_customer,
            model_class=str(self.model_class.__name__),
            data=data
        )
