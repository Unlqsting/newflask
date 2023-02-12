from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class etrack_user(db.Model):
    __tablename__ = 'etrack_users'  # table name is plural, class name is singular
    # Define the User schema with "vars" from object
    _uname = db.Column(db.String(255), primary_key=True)
    _savedWorkouts = db.Column(db.PickleType, unique=False, nullable=False)

    def __init__(self, uname, savedWorkouts):
        self._uname = uname
        self._savedWorkouts = savedWorkouts

    @property
    def uname(self):
        return self._uname
    
    @uname.setter
    def uname(self, uname):
        self._uname = uname

    @property
    def savedWorkouts(self):
        return self._savedWorkouts

    @savedWorkouts.setter
    def savedWorkouts(self, savedWorkouts):
        self._savedWorkouts = savedWorkouts

    @property
    def dictionary(self):
        dict = {
            "username" : self.uname,
            "saved workouts" : self.savedWorkouts,
        }
        return dict

    def __str__(self):
        return json.dumps(self.dictionary)
    
    def __repr__(self):
        return f'User(username={self._uname}, password hash={self._savedWorkouts})'


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
            "uname": self.uname,
            "savedWorkouts": self.savedWorkouts,
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, uname, savedWorkouts):
        """only updates values with length"""
        if len(uname) > 0:
            self.uname = uname
        if len(savedWorkouts) > 0:
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
        db.init_app(app)
        db.create_all()
        global u1
        u1 = etrack_user(uname="testUser" , savedWorkouts = {"1 February 2023 workout(s)": ["This is a test"]})

        users = [u1]

        """Builds sample user/note(s) data"""
        for user in users:
            try:
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate username, or error: {user.uname}")
