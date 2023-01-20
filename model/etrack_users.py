from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class User(db.Model):
    __tablename__ = 'users'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    _name = db.Column(db.String(255), unique=False, nullable=False)
    _pwHash = db.Column(db.String(255), unique=False, nullable=False)

class User:
    def __init__(self, uname, pwHash):
        self._uname = uname
        self._pwHash = pwHash

    @property
    def uname(self):
        return self._uname
    
    @uname.setter
    def uname(self, uname):
        self._uname = uname

    @property
    def pwHash(self):
        return self._pwHash

    @pwHash.setter
    def pwHash(self, pwHash):
        self._pwHash = pwHash

    @property
    def dictionary(self):
        dict = {
            "username" : self.uname,
            "password hash" : self.pwHash,
        }
        return dict

    def __str__(self):
        return json.dumps(self.dictionary)
    
    def __repr__(self):
        return f'User(username={self._uname}, password hash={self._pwHash})'


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
            "pwHash": self.pwHash,
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, uname="", pwHash=""):
        """only updates values with length"""
        if len(uname) > 0:
            self.uname = uname
        if len(pwHash) > 0:
            self.pwHash = pwHash
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

def initEtrackUsers():
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""
    u1 = User(uname="Albert" , pwHash = "sha512$b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86")
    u2 = User(uname="Bob" , pwHash = "sha512$b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86")

    users = [u1, u2]

    """Builds sample user/note(s) data"""
    for user in users:
        try:
            user.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate username, or error: {user.uname}")
