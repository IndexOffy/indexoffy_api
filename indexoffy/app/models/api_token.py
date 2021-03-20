# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

# Define a ApiToken model
class ApiToken(Base):

    __tablename__ = 'api_token'

    base_customer = db.Column(db.String(128), nullable=False)
    api_token = db.Column(db.String(256), nullable=False,unique=True)
    status = db.Column(db.SmallInteger, nullable=False)
    api_type = db.Column(db.String(128), nullable=False)

    # New instance instantiation procedure
    def __init__(self, base_customer, api_token, status):

        self.base_customer  = base_customer
        self.api_token      = api_token
        self.status         = status

    def __repr__(self):
        return '<id %r>' % (self.id)