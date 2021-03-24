# Import flask dependencies

from app import db
from flask import request, jsonify

from app.models.user import User, user_schema, users_schema, fields_list, fields_list_admin

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

        # api_type 0 = Admin / api_type 1 = User
        fields = fields_list if data['user'].api_type == 1 else fields_list_admin
        try:
            for item in fields:
                option = request.args.get(item)
                if option:
                    self.params[item] = option
        except print(0):
            pass

    def get_all(self):
        """
        """
        try:
            users = User.query
            for item in self.params:
                users = users.filter(getattr(User, item) == self.params[item])
            users = users.all()
            
            if users:
                result = users_schema.dump(users)
                return self.response.successfully_fetched(result=result, params=self.params)
        except:
            return self.response.server_error(params=self.params)
        
        return self.response.user_dont_exist(params=self.params)

    def get(self):
        """
        """
        try:
            user = User.query
            for item in self.params:
                user = user.filter(getattr(User, item) == self.params[item])
            user = user.first()

            if user:
                result = user_schema.dump(user)
                return self.response.successfully_fetched(result=result, params=self.params)
        except:
            return self.response.server_error(params=self.params)

        return self.response.user_dont_exist(params=self.params)

    def post(self):
        pass

    def put(self):
        pass
