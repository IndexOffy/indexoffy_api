from app import db, ma

class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

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

    def default(self):
        """
        """
        base_log_data = { 
            'base_customer': 0,
            'user_name': "No name",
            'user_email': "No email",
            'operation': "operation",
            'model_class': "model_class",
            'function': "function",
            'model_id': 0,
            'params': None,
            'args': None,
            'result': "No result",
            'message': "No message",
            'status': 0,
            'api_token': None,
            'ip_address': None,
            'route': None
        }

        return base_log_data

class BaseErrorSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'base_customer',
            'user_name',
            'user_email',
            'operation',
            'model_class',
            'function',
            'model_id',
            'params',
            'args',
            'result',
            'message',
            'status',
            'api_token',
            'ip_address',
            'route'
        )

base_log_schema = BaseErrorSchema()
base_logs_schema = BaseErrorSchema(many=True)
