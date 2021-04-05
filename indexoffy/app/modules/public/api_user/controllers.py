# Import flask dependencies

from app import db
from flask import request, jsonify

from app.models.user import User, base_schema, base_schemas

from app.api.base import BaseApi
from app.api.utils.responses import BaseResponse
class ControlerUser(BaseApi):
    """
    """
    def __init__(self, base_customer, data=None):
        super().__init__(base_customer, data)

        self.model_class = User
        self.base_schema = base_schema
        self.base_schemas = base_schemas

        self.response = BaseResponse(
            base_customer=base_customer,
            model_class=str(self.model_class.__name__),
            data=data
        )

    def get_all(self):
        """ Method GET All
        """
        # Adequacy of received parameters
        for item in self.base_schema.fields:
            option = self.data['params'].get(item)
            if option:
                if item == 'code':
                    self.params[item] = option

        if not self.params:
            return self.response.successfully_fetched()

        try:
            query_model = self.model_class.query
            for item in self.params:
                query_model = query_model.filter(getattr(self.model_class, item) == self.params[item])
            query_model = query_model.first()

            if query_model:
                result = self.base_schema.dump(query_model)
                return self.response.successfully_fetched(result=result, limit=1, quantity=1)
        except:
            return self.response.server_error()
        
        return self.response.successfully_fetched()