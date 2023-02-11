""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

# Define the Post class to manage actions in 'posts' table,  with a relationship to 'users' table
class User(db.Model):
    __tablename__ = 'posts'

    # Define the Notes schema
    id = db.Column(db.Integer, primary_key=True)
    _Workout = db.Column(db.Integer, nullable=False)
    _Sets = db.Column(db.Integer, nullable=False)
    _Reps = db.Column(db.Integer, nullable=False)

    # Constructor of a Notes object, initializes of instance variables within object
    def __init__(self, Workout, Sets, Reps):
        self._Workout = Workout
        self._Sets = Sets
        self._Reps = Reps

    # Returns a string representation of the Notes object, similar to java toString()
    # returns string
        def __repr__(self):
            return "<Users(Workout='%s', Sets='%s', Reps='%s')>"% (
                self._Workout,
                self._Sets,
                self._Reps,
            )
    # CRUD create, adds a new record to the Notes table
    # returns the object added or None in case of an error
    def create(self):
        try:
            # creates a Notes object from Notes(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Notes table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None
    # Define the User class to manage actions in the 'users' table
    # -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
    # -- a.) db.Model is like an inner layer of the onion in ORM
    # -- b.) User represents data we want to store, something that is built on db.Model
    # -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
     # table name is plural, class name is singular

    # Define the User schema with "vars" from object
                # id = db.Column(db.Integer, primary_key=True)
                # _name = db.Column(db.String(255), unique=False, nullable=False)
                # _uid = db.Column(db.String(255), unique=True, nullable=False)
                # _password = db.Column(db.String(255), unique=False, nullable=False)
                # _dob = db.Column(db.Date)

                # # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
                # posts = db.relationship("Post", cascade='all, delete', backref='users', lazy=True)

                # # constructor of a User object, initializes the instance variables within object (self)
                # def __init__(self, name, uid, password="123qwerty", dob=date.today()):
                #     self._name = name    # variables with self prefix become part of the object, 
                #     self._uid = uid
                #     self.set_password(password)
                #     self._dob = dob

    # a name getter method, extracts name from object
    # Getters:
    @property
    def Workout(self):
        return self._Workout
    
    @property
    def Reps(self):
        return self._Reps
    
    @property
    def Sets(self):
        return self._Sets
   
    # Setters    
    @Workout.setter
    def Age(self, workout):
        self._Workout = workout

    @Reps.setter
    def Weight(self,reps):
        self._Weight = reps

    @Sets.setter
    def Weight(self,sets):
        self._Weight = sets
        
    # a getter method, extracts email from object
    @property
    def dictionary(self):
            dict = {
                "Workout" : self.Workout,
                "Sets" : self.Sets,
                "Reps" : self.Reps,
            }
            return dict

    def __str__(self):
            return json.dumps(self.dictionary)
        
    def __repr__(self):
            return f'Users(Workout={self._Workout}, Sets={self._Sets}, Reps={self._Reps})'

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

    def read(self):
        return {
            "Sets": self.Sets,
            "Reps": self.Reps,
            "Workout": self.Workout,
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, Workout="", Sets="", Reps=""):
        """only updates values with length"""
        if len(Workout) > 0:
            self.name = Workout
        if len(Sets) > 0:
            self.Sets = Sets
        if len(Reps) > 0:
            self.Sets = Sets
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing """


# Builds working data for testing
def initUsers():
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""
    Nathan = User(Workout='Chest Fly', Sets='5', Reps='8')
    Not_Nathan = User(Workout='Skull Crushers', Sets='4', Reps='10')

    users = [Nathan, Not_Nathan]

    """Builds sample user/note(s) data"""
    for user in users:
        try:
            '''add a few 1 to 4 notes per user'''
            # for num in range(randrange(1, 4)):
            #     note = "#### " + user.name + " note " + str(num) + ". \n Generated by test data."
            #     # user.posts.append(Post(id=user.id, note=note, image='ncs_logo.png'))
            # '''add user/post data to table'''
            user.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {user.uid}")
            