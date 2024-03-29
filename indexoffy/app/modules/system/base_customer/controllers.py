# coding=utf-8

from app import db
from app.api.base import BaseApi
from app.api.utils.responses import BaseResponse

from app.models.base_customer import BaseCustomer, base_schema, base_schemas

class ControlerBaseCustomer(BaseApi):
    """
    """
    def __init__(self, base_customer, data=None):
        super().__init__(base_customer, data)

        self.model_class = BaseCustomer
        self.base_schema = base_schema
        self.base_schemas = base_schemas

        self.response = BaseResponse(
            base_customer=base_customer,
            model_class=str(self.model_class.__name__),
            data=data
        )

    def get(self, model_id=None):
        try:
            query = self.model_class.query \
                .filter(
                    self.model_class.id == model_id) \
                .first()
            if query:
                result = self.base_schema.dump(query)
                return self.response.successfully_fetched(result=result, limit=1, quantity=1)
        except:
            return self.response.server_error()

        return self.response.data_not_found()