from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class sports(db.Model):
    __tablegoal__ = 'sports' 
    id = db.Column(db.Integer, primary_key=True)
    _goal = db.Column(db.String(255),nullable=False)
    _diff = db.Column(db.Integer,nullable=False)
    _time = db.Column(db.String(255),nullable=False)
    

    def __init__(self, goal, diff, time):
        
        self._goal = goal
        self._diff = diff
        self._time = time
        
    def __repr__(self):
        return "<sports(goal='%s', diff='%s', time='%s'>" % (
            self._goal,
            self._diff,
            self._time,
        )

    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self, goal):
        self._goal = goal
        
    @property
    def diff(self):
        return self._diff
        
    @diff.setter
    def diff(self, diff):
        self._diff = diff
        
    @property
    def time(self):
        return self._time
        
    @time.setter
    def time(self, time):
        self._time = time


    @property
    def dictionary(self):
        dict = {
            
            "goal" : self.goal,
            "diff" : self.diff,
            "time" : self.time
           
        }
        return dict

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
            "goal" : self.goal,
            "diff" : self.diff,
            "time" : self.time
        }


    def uptime(self, goal="", diff="", time=""):
        """only uptimes values with length"""

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

def initSports():
    """Create database and tables"""
    with app.app_context():
        # db.init_app(app)
        db.create_all()
        
        # ! no need for tester data. Already created.
        """Tester data for table"""
        # u1 = sports(goal = "bench 135", diff= "6")
        # u2 = sports(goal = "squat 225", diff= "7")

        # users = [u1, u2]

        """Builds sample user/note(s) data"""
        # for user in users:
        #     try:
        #         user.create()
        #     except IntegrityError:
        #         '''fails with bad or duplicate data'''
        #         db.session.remove()
        #         print(f"Records exist, duplicate usergoal, or error: {user.uid}")

