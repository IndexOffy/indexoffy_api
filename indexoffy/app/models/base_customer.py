from app import db, ma
from marshmallow import fields, EXCLUDE
class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class BaseCustomer(Base):

    __tablename__ = 'base_customer'

    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(128),  nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, name, email, password, status):

        self.name       = name
        self.email      = email
        self.password   = password
        self.status     = status

    def __repr__(self):
        return '<id %r>' % (self.id)

class BaseCustomerSchema(ma.Schema):
    name = fields.Str()
    email = fields.Email()
    password = fields.Str()
    status = fields.Integer()
    class Meta:
        unknown = EXCLUDE
        fields = ('id','name','email','password','status')

base_schema = BaseCustomerSchema()
base_schemas = BaseCustomerSchema(many=True)