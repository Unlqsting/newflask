from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from flask import Flask, request, redirect
from __init__ import app, db
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

"""
These object can be used throughout project.
1.) Objects from this file can be included in many blueprints
2.) Isolating these object definitions avoids duplication and circular dependencies
"""

# Setup of key Flask object (app)
app = Flask(__name__)
CORS(app)
CORS(app, origins=['http://localhost:4002'])

from model.forums import Post

forum_api = Blueprint('forum_api', __name__,
                   url_prefix='/api/forum')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(forum_api)


class ForumAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.form
            
            ''' Avoid garbage in, error checking '''

            # validate uid
            postTitle = body.get('topic')
            if postTitle is None or len(postTitle) < 2:
                return {'message': f'post tile is missing, or is less than 2 characters'}, 211
            
            post = body.get('postText')
            if post is None or len(post) < 12:
                return {'message': f'please describe your post adequately'}, 212
            # look for password and dob

            ''' #1: Key code block, setup USER OBJECT '''
            uo = Post(
                      postTitle=postTitle, 
                      post=post,
                      )
            
            ''' Additional garbage error checking '''
            # set password if provided
           
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            createPost = uo.create()
            # success returns json of post
            if createPost:
                redirect_url = 'http://localhost:4002/forum'
                return redirect(redirect_url)
            # failure returns error

    class _Read(Resource):
        def get(self):
            posts = Post.query.all()    # read/extract all posts from database
            json_ready = [createPost.read() for createPost in posts]
            # prepare output in json
            return jsonify(json_ready)
            
        # jsonify creates Flask response object, more specific to APIs than json.dumps

    class _Update(Resource):
        def patch(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            lookId = body.get('id')
            postupd = Post.query.filter_by(id=lookId).first()
            
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            postTitle = body.get('postTitle')
            if postTitle is None or len(postTitle) < 2:
                return {'message': f'post title is missing or is less than 2 characters'}, 211
            
            post = body.get('post')
            if post is None or len(post) < 12:
                return {'message': f'post is missing or is less than 12 characters'}, 212

            postupd.update(postTitle, post)
            
    class _Delete(Resource):
        def delete(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            lookId = body.get('id')
            postdel = Post.query.filter_by(id=lookId).first()
            
            postdel.delete()
        
            
        
            
    # class _

    # class _

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Update, '/update')
    api.add_resource(_Delete, '/delete')
    api.add_resource(_Read, '/')
    
