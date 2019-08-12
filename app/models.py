from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///author.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Author(db.Model):
    __tablename__ = 'author'


    id = db.Column(db.Integer , primary_key=True)
    first_name = db.Column(db.String(55) , nullable=False)
    last_name = db.Column(db.String(100)  , nullable=False)
    book = db.relationship('Book' , backref='author' , lazy='dynamic')


    def __init__(self,first_name , last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'<Author {self.get_full_name}>'




class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer , primary_key=True)
    title= db.Column(db.String(155) , nullable=False)
    price = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    
    def __repr__(self):
        return f'<Book {self.title}'


