# coding=utf-8

from app import db
from flask import jsonify, request
from functools import wraps

from app.api.utils.responses import BaseResponse


class BaseApi(object):
    """ Base View to create helpers common to all Webservices.
    """
    def __init__(self, data):
        """Constructor
        """
        pass

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
