# coding=utf-8

from app import db
from app.api.base import BaseApi


class ControlerBaseError(BaseApi):
    """
    """
    def __init__(self, data):
        super().__init__(data)

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass
