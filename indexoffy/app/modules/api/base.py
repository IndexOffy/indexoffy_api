# coding=utf-8
"""
Base View to create helpers common to all Webservices.
"""

class BaseApi(object):
    """Main Class.
    """
    def __init__(self, request):
        """Constructor
        """
        self.request = request

        api_token = self.validate_token()

        # valid token
        self.token = api_token.token
        self.base_customer = api_token.base_customer

    def validate_token(self):
        """
        Validate Token in HTTP Header
        """
        # API token header

        from pdb import set_trace; set_trace()

        header = 'offy-token'
        token = self.request.headers.get(header)

        pass

    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass
