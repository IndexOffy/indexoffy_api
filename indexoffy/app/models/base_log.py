# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

# Define a BaseLog model
class BaseLog(Base):

    __tablename__ = 'base_log'

    base_customer = db.Column(db.String(256), nullable=False)
    user_name = db.Column(db.String(100),  nullable=False)
    user_email = db.Column(db.String(100),  nullable=False)
    operation = db.Column(db.String(10),  nullable=False)
    model_class = db.Column(db.String(50),  nullable=False)
    model_id = db.Column(db.String(50),  nullable=False)

    # New instance instantiation procedure
    def __init__(self, base_customer, user_name, user_email, operation, model_class, model_id):

        self.base_customer = base_customer
        self.user_name     = user_name
        self.user_email    = user_email
        self.operation     = operation
        self.model_class   = model_class
        self.model_id      = model_id

    def __repr__(self):
        return '<id %r>' % (self.id)