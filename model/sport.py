from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class sports(db.Model):
    __tablegoal__ = 'sports' 
    _uid = db.Column(db.String(255), primary_key=True)
    _goal = db.Column(db.String(255), unique=False, nullable=False)
    _diff = db.Column(db.String(255), unique=False, nullable=False)
    _date = db.Column(db.String(255), unique=False, nullable=False)
    _status = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self, uid, goal, diff, date, status):
        self. uid = uid
        self._goal = goal
        self._diff = diff
        self._date = date
        self._status = status

    @property
    def uid(self):
        return self. uid
    
    @uid.setter
    def uid(self, uid):
        self. uid = uid

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
    def date(self):
        return self._date
        
    @date.setter
    def date(self, date):
        self._date = date
        
    @property
    def status(self):
        return self._status
        
    @status.setter
    def status(self, status):
        self._status = status
        


    

    @property
    def dictionary(self):
        dict = {
            "userid" : self.uid,
            "goal" : self.goal,
            "diff" : self.diff,
            "date" : self.date,
            "status" : self.status
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
            "userid" : self.uid,
            "goal" : self.goal,
            "diff" : self.diff,
            "date" : self.date,
            "status" : self.status
        }


    def update(self, uid="", goal="", diff="", status=""):
        """only updates values with length"""
        if len(uid) > 0:
            self.uid = uid
        if len(goal) > 0:
            self.goal = goal
        if len(diff) > 0:
            self.diff = diff
        if len(status) > 0:
            self.status = status

        
        db.session.commit()
        return self


    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

def initSports():
    """Create database and tables"""
    with app.app_context():
        db.init_app(app)
        db.create_all()
        """Tester data for table"""
        u1 = sports(uid=1 , goal = "Jace")
        u2 = sports(uid=2 , goal = "Julien")

        users = [u1, u2]

        """Builds sample user/note(s) data"""
        for user in users:
            try:
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate usergoal, or error: {user.uid}")

