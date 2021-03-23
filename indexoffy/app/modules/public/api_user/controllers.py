# Import flask dependencies

from app import db
from flask import request, jsonify

from app.models.user import User, user_schema, users_schema, fields_list

from app.api.base import BaseApi
from app.api.utils.responses import BaseResponse
class ControlerUser(BaseApi):
    """
    """
    def __init__(self, data):
        super().__init__(data)

        self.response = BaseResponse(
            data=data,
            model_class=str(__name__)
        )

        self.params = {}
        try:
            for item_value in fields_list:
                option = request.args.get(item_value)
                if option:
                    self.params[item_value] = option
        except print(0):
            pass

    def get(self):
        """
        """
        try:
            user = User.query.filter(User.code == self.params['code']).first()
            if user:
                result = user_schema.dump(user)
                return self.response.successfully_fetched(result=result,params=self.params)
        except:
            return BaseResponse().server_error()

        return BaseResponse().user_dont_exist()

    def post(self):
        pass

    def put(self):
        pass
