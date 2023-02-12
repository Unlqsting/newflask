from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class sports(db.Model):
    __tablename__ = 'sports' 
    _uid = db.Column(db.String(255), primary_key=True)
    _name = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self, uid, name):
        self. uid = uid
        self._name = name

    @property
    def uid(self):
        return self. uid
    
    @uid.setter
    def uid(self, uid):
        self. uid = uid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def dictionary(self):
        dict = {
            "userid" : self.uid,
            "Name" : self.name,
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
            "uid": self.uid,
            "name": self.name,
        }


    def update(self, uid="", name=""):
        """only updates values with length"""
        if len(uid) > 0:
            self.uid = uid
        if len(name) > 0:
            self.name = name
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
        u1 = sports(uid=1 , name = "Jace")
        u2 = sports(uid=2 , name = "Julien")

        users = [u1, u2]

        """Builds sample user/note(s) data"""
        for user in users:
            try:
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate username, or error: {user.uid}")

