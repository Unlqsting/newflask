from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class etrack_user(db.Model):
    __tablename__ = 'signup'  # table name is plural, class name is singular
    # Define the User schema with "vars" from object
    _uname = db.Column(db.String(255), primary_key=True)
    _email = db.Column(db.String(255), unique=False, nullable=False)
    _pwHash = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self, uname, email, pwHash):
        self._uname = uname
        self._email = email
        self._pwHash = pwHash

    @property
    def uname(self):
        return self._uname
    
    @uname.setter
    def uname(self, uname):
        self._uname = uname
        
    @property
    def email(self):
        return self._email
    
    @uname.setter
    def email(self, email):
        self._email = email

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
            "email" : self.email,
            "password hash" : self.pwHash,
        }
        return dict

    def __str__(self):
        return json.dumps(self.dictionary)
    
    def __repr__(self):
        return f'Sign up data(username={self._uname}, email={self._email}, password hash={self._pwHash})'


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
            "email" : self.email,
            "pwHash": self.pwHash,
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, uname="", pwHash=""):
        """only updates values with length"""
        if len(uname) > 0:
            self.uname = uname
        
        # if len(email) > 0:
        #     self.email = email
        
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
    user1 = etrack_user(uname="Unlqsting", email="abc@gmail.com", pwHash = "sha512$b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86")
    user2 = etrack_user(uname="noor", email="xyz@gmail.com", pwHash = "sha512$b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86")

    signedUp = [user1, user2]

    """Builds sample user/note(s) data"""
    for user in signedUp:
        try:
            user.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate username, or error: {user.uname}")
