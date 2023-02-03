from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.etrack_users import etrack_user

etrack_user_api = Blueprint('user_api', __name__,
                   url_prefix='/api/etrack_users')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(etrack_user_api)

class etrack_UserAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            uname = body.get('uname')
            if uname is None or len(uname) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210
            # validate uid
            
            pwHash = body.get('pwHash')
        
            uo = etrack_user(uname=uname, 
                      pwHash=pwHash)
            


            
            # create user in database
            user = uo.create()
            # success returns json of user
            if user:
                return jsonify(user.read())
            # failure returns error
            return {'message': f'Processed {uname}, either a format error or User ID {pwHash} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            users = etrack_user.query.all()    # read/extract all users from database
            json_ready = [user.read() for user in users]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')