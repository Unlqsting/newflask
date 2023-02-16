""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''

# Define the Post class to manage actions in 'posts' table,  with a relationship to 'users' table
class Post(db.Model):
    __tablename__ = 'forumPosts'

    # Define the Notes schema
    id = db.Column(db.Integer, primary_key=True)
    postTitle = db.Column(db.String(255), unique=False, nullable=False)
    post = db.Column(db.String(255), unique=False, nullable=False)
    # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)

    # Constructor of a Notes object, initializes of instance variables within object
    def __init__(self, postTitle, post):
        self.postTitle = postTitle
        self.post = post


    # Returns a string representation of the Notes object, similar to java toString()
    # returns string
    def __repr__(self):
        return "Posts(" + str(self.id) + "," + self.postTitle + "," + self.post + "," + ")"

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

    # CRUD read, returns dictionary representation of Notes object
    # returns dictionary
    def read(self):   
        return {
            "id": self.id,
            "postTitle": self.postTitle,
            "post": self.post
        }


# Define the User class to manage actions in the 'users' table
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) User represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL



# Builds working data for testing
def initPost():
    with app.app_context():
        """Create database and tables"""
        db.init_app(app)
        db.create_all()
        #! """Tester data for table"""
        # p1 = Post(postTitle='First post', post='This is my first post')
        # p2 = Post(postTitle='Second post', post='This is my second post')
        # p3 = Post(postTitle='Third post', post='This is my third post')
        
        # posts = [p1, p2, p3]

        # #! """Builds sample user/note(s) data"""
        # for post in posts:
        #     try:
        #         '''add a few 1 to 4 notes per user'''
        #         post.create()
        #     except IntegrityError:
        #         '''fails with bad or duplicate data'''
        #         db.session.remove(posts)
        #         return None