from app import db, ma
from marshmallow import fields, EXCLUDE

class Base(db.Model):
    
    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class User(Base):

    __tablename__ = 'user'

    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    code = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    visibility = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, email, code, score, date, status):

        self.name       = name
        self.email      = email
        self.code       = code
        self.score      = score
        self.date       = date
        self.status     = status
        self.visibility = visibility

    def __repr__(self):
        return '<id %r>' % (self.id)

class UserSchema(ma.Schema):
    class Meta:
        unknown = EXCLUDE
        fields = ('id', 'name', 'email', 'code', 'score', 'date', 'status', 'visibility')
        
base_schema = UserSchema()
base_schemas = UserSchema(many=True)