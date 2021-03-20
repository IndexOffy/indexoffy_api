# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

# Define a ApiUser model
class ApiUser(Base):

    __tablename__ = 'api_user'

    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256),  nullable=False)
    code = db.Column(db.String(256),  nullable=False)
    level = db.Column(db.String(256),  nullable=False)
    date = db.Column(db.String(256),  nullable=False)
    status = db.Column(db.Date, nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, code, status):

        self.name       = name
        self.email      = email
        self.code       = code
        self.status     = status

    def __repr__(self):
        return '<id %r>' % (self.id)