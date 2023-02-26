from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class etrack_user(db.Model):
    __tablename__ = 'etrack_users'  # table name is plural, class name is singular
    # Define the User schema with "vars" from object
    _date = db.Column(db.String(255), primary_key=True)
    _savedWorkouts = db.Column(db.PickleType, unique=False, nullable=False)

    def __init__(self, date, savedWorkouts):
        self._date = date
        self._savedWorkouts = savedWorkouts

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        self._date = date

    @property
    def savedWorkouts(self):
        return self._savedWorkouts

    @savedWorkouts.setter
    def savedWorkouts(self, savedWorkouts):
        self._savedWorkouts = savedWorkouts

    @property
    def dictionary(self):
        dict = {
            "date" : self.date,
            "saved workouts" : self.savedWorkouts,
        }
        return dict

    def __str__(self):
        return json.dumps(self.dictionary)
    
    def __repr__(self):
        return f'etrack_user(date={self._date}, savedWorkouts={self._savedWorkouts})'


    # CRUD stuff
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "date": self.date,
            "savedWorkouts": self.savedWorkouts,
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, date, savedWorkouts):
        """only updates values with length"""
        if len(date) > 0:
            self.date = date
        # if len(savedWorkouts) > 0:
        self.savedWorkouts = savedWorkouts
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

def initEtrackUsers():
    with app.app_context():
        # db.init_app(app)
        db.create_all()
        r1 = etrack_user(date="25 February 2023" , savedWorkouts = ["This is a test of the new table"])

        rows = [r1]

        """Builds sample user/note(s) data"""
        for row in rows:
            try:
                row.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate username, or error: {row.date}")
