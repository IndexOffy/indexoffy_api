from app import db, ma


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

    def __init__(self, name, email, code, score, date, status):

        self.name       = name
        self.email      = email
        self.code       = code
        self.score      = score
        self.date       = date
        self.status     = status

    def __repr__(self):
        return '<id %r>' % (self.id)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'code', 'score', 'date')
        

user_schema = UserSchema()
users_schema = UserSchema(many=True)
fields_list = ['id', 'name', 'email', 'code', 'score', 'date']