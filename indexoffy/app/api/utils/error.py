# coding=utf-8

from app import db

class BaseError(object):
    """ Base View to Error common to all Webservices.
    """
    def __init__(self, *args, **kwargs):
        """Constructor
        """

    def error(self):
        """ 
        """
        return None