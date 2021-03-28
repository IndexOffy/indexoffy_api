# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db, ma

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

# Define a BaseCustomer model
class BaseCustomer(Base):

    __tablename__ = 'base_customer'

    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(128),  nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password, status):

        self.name       = name
        self.email      = email
        self.password   = password
        self.status     = status

    def __repr__(self):
        return '<id %r>' % (self.id)

class BaseCustomerSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'name',
            'email',
            'password',
            'status'
        )

base_customer_schema = BaseCustomerSchema()
base_customers_schema = BaseCustomerSchema(many=True)