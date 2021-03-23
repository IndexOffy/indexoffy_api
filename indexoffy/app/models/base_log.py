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

    base_customer = db.Column(db.Integer, nullable=False)
    user_name = db.Column(db.String(100), nullable=True)
    user_email = db.Column(db.String(100), nullable=True)
    operation = db.Column(db.String(10), nullable=True)
    model_class = db.Column(db.String(50), nullable=True)
    function = db.Column(db.String(50), nullable=True)
    model_id = db.Column(db.Integer, nullable=True)
    params = db.Column(db.String(256), nullable=True)
    args = db.Column(db.String(256), nullable=True)
    result = db.Column(db.String(256), nullable=True)
    message = db.Column(db.String(100), nullable=True)
    status = db.Column(db.Integer, nullable=True)
    api_token = db.Column(db.String(100), nullable=True)
    ip_address = db.Column(db.Integer, nullable=True)
    route = db.Column(db.String(100), nullable=True)

    # New instance instantiation procedure
    def __init__(self,
        base_customer,
        user_name,
        user_email,
        operation,
        model_class,
        function,
        model_id,
        params,
        args,
        result,
        message,
        status,
        api_token,
        ip_address,
        route
    ):

        self.base_customer = base_customer
        self.user_name     = user_name
        self.user_email    = user_email
        self.operation     = operation
        self.model_class   = model_class
        self.function      = function
        self.model_id      = model_id
        self.params        = params
        self.args          = args
        self.result        = result
        self.message       = message
        self.status        = status
        self.api_token     = api_token
        self.ip_address    = ip_address
        self.route         = route

    def __repr__(self):
        return '<id %r>' % (self.id)