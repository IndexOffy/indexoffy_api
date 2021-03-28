from app import db, ma

class Base(db.Model):
    
    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
class BaseError(Base):

    __tablename__ = 'base_error'

    base_customer = db.Column(db.Integer, nullable=False)
    model_class = db.Column(db.String(50), nullable=False)
    traceback = db.Column(db.String(256), nullable=True)

    def __init__(self, base_customer, model_class, traceback):

        self.base_customer = base_customer
        self.model_class   = model_class
        self.traceback     = traceback

    def __repr__(self):
        return '<id %r>' % (self.id)
class BaseErrorSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'base_customer',
            'model_class',
            'traceback'
        )

base_schema = BaseErrorSchema()
base_schemas = BaseErrorSchema(many=True)
