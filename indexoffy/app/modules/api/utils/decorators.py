# coding=utf-8

from app import db
from functools import wraps

class BaseApi(object):
    """ Base View to Decorators common to all Webservices.
    """

    def __init__(self):
        """Constructor
        """
        pass