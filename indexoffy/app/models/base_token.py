from app import db, ma
from marshmallow import fields, EXCLUDE

class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class BaseToken(Base):

    __tablename__ = 'base_token'

    base_customer = db.Column(db.Integer, nullable=False)
    api_token = db.Column(db.String(256), nullable=False, unique=True)
    status = db.Column(db.Boolean, nullable=False)
    api_type = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, base_customer, api_token, status, api_type):

        self.base_customer  = base_customer
        self.api_token      = api_token
        self.status         = status
        self.api_type       = api_type

    def __repr__(self):
        return '<id %r>' % (self.id)
class BaseTokenSchema(ma.Schema):
    class Meta:
        unknown = EXCLUDE
        fields = ('id', 'base_customer', 'api_token', 'status', 'api_type')

base_schema = BaseTokenSchema()
base_schemas = BaseTokenSchema(many=True)
