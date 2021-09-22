import os
from sqlalchemy import Column, String, Integer, ForeignKey
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
database_path = os.environ['DATABASE_URL']

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


def create_tables():
    db.create_all()

'''
Person
'''
class Person(db.Model):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    quote = db.relationship("Quote")

    def __init__(self, name):
        self.name = name

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
        }

'''
Quote
'''
class Quote(db.Model):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    person_id = Column(Integer, ForeignKey('persons.id'))

    def __init__(self, title, description, person_id):
        self.title = title
        self.description = description
        self.person_id = person_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'person_id': self.person_id
        } 
