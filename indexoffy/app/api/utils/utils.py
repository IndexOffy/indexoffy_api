# coding=utf-8

from app import db

from app.api.utils.responses import BaseResponse

class BaseUtils(object):
    """ Base View to Utils common to all Webservices.
    """
    def __init__(self, *args, **kwargs):
        """Constructor
        """

    def check_number(self, value):
        """
        """
        pass

    def check_character(self, value):
        """
        """
        return None

    def check_request(self, request):
        """
        """
        return None