from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

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
            # validate name
            #! topicOwner = body.get('topicOwner')
            #! if topicOwner is None or len(topicOwner) < 2:
            #!     return {'message': f'Name is missing, or is less than 2 characters'}, 210
            # validate uid
            postTitle = body.get('topic')
            
            post = body.get('postText')
            # look for password and dob

            ''' #1: Key code block, setup USER OBJECT '''
            uo = Post(
                      postTitle=postTitle, 
                      post=post
                      )
            
            ''' Additional garbage error checking '''
            # set password if provided
           
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            createPost = uo.create()
            # success returns json of post
            if createPost:
                return jsonify(createPost.read())
            # failure returns error

    class _Read(Resource):
        def get(self):
            posts = Post.query.all()    # read/extract all posts from database
            json_ready = [createPost.read() for createPost in posts]
            # prepare output in json
            return jsonify(json_ready)
            
        # jsonify creates Flask response object, more specific to APIs than json.dumps

    # class _

    # class _

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    
