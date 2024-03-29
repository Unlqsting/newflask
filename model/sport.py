
""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

# Define the Post class to manage actions in 'posts' table,  with a relationship to 'users' table
class sports(db.Model):
    __tablename__ = 'sports'

    # Define the Notes schema
    id = db.Column(db.Integer, primary_key=True)
    _goal = db.Column(db.String(255), nullable=False)
    _diff = db.Column(db.Integer, nullable=False)
    _time = db.Column(db.String(255), nullable=False)

    def __init__(self, goal, diff, time):
        self._goal = goal
        self._diff = diff
        self._time = time

    @property
    def goal(self):
        return self._goal
    
    @property
    def time(self):
        return self._time
    
    @property
    def diff(self):
        return self._diff
   
    # Setters    
    @goal.setter
    def goal(self, goal):
        self._goal = goal

    @time.setter
    def time(self,time):
        self._time = time

    @diff.setter
    def diff(self,diff):
        self._diff = diff

    def create(self):
        try:
            db.session.add(self)  
            db.session.commit()  
            return self
        except IntegrityError:
            db.session.remove()
            return None

    def read(self):
        return {
            "diff": self.diff,
            "time": self.time,
            "goal": self.goal,
        }
    
    def update(self, goal="", diff="", time=""):
        """only updates values with length"""

        if len(goal) > 0:
            self.goal = goal
        if len(diff) > 0:
            self.diff = diff
        if len(time) > 0:
            self.time = time
        
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

    def __str__(self):
            return json.dumps(self.dictionary)
        
    def __repr__(self):
            return f'Users(goal={self._goal}, diff={self._diff}, time={self._time})'

    def create(self):
            try:
                # creates a person object from User(db.Model) class, passes initializers
                db.session.add(self)  # add prepares to persist person object to Users table
                db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
                print("commit")
                return self
            except IntegrityError:
                print("issue")
                db.session.remove()
                return None

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, goal="", diff="", time=""):
        """only updates values with length"""
        if len(goal) > 0:
            self.name = goal
        if len(diff) > 0:
            self.diff = diff
        if len(time) > 0:
            self.diff = diff
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


def initSports():
    """Create database and tables"""
    with app.app_context():
        # db.init_app(app)
        db.create_all()
    #     "Testing data"
    #     u1 = sports(goal="Finish Homework",diff="10",date="4/20/2023")
    #     u2 = sports(goal="Run a Mile",diff="5",date="4/21/2023")
    # sports = [u1, u2]