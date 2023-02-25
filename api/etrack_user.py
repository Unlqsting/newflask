from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.etrack_users import etrack_user
import model.etrack_users
from __init__ import app, db


etrack_user_api = Blueprint('etrack_user_api', __name__,
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
            date = body.get('date')
            if date is None or len(date) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210
            # validate uid
            
            savedWorkouts = body.get('savedWorkouts')
        
            uo = etrack_user(date=date, 
                      savedWorkouts=savedWorkouts)
            


            
            # create user in database
            user = uo.create()
            # success returns json of user
            if user:
                return jsonify(user.read())
            # failure returns error
            return {'message': f'Processed {date}, either a format error or User ID {savedWorkouts} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            users = etrack_user.query.all()    # read/extract all users from database
            json_ready = [user.read() for user in users]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    class _Update(Resource):
        def patch(self):
            body = request.get_json()
            targetDate = body.get('date')
            targetRow = etrack_user.query.filter_by(_date=targetDate).first()
            print(targetRow)
            ''' Read data for json body '''

            print(body)
            ''' Avoid garbage in, error checking '''
            # validate name
            savedWorkouts = body.get('savedWorkouts')
            print(savedWorkouts)
            # targetRow = etrack_user.read(model.etrack_users.u1)
            if savedWorkouts == targetRow._savedWorkouts:
                return {'message': f'Already exists', 'Workouts':savedWorkouts}
            else:
                print("updating")
                # targetRow._savedWorkouts = savedWorkouts
                # db.session.commit
                targetRow.update(targetDate, savedWorkouts)
                print(targetRow._savedWorkouts)
                print(targetRow.read())
                return jsonify(targetRow.read())

    class _Delete(Resource):
        def delete(self):
            body = request.get_json()
            targetDates = body.get('targetDates')
            print(targetDates)
            json_ready = []
            for date in targetDates:
                print("date is " + date)
                targetRow = etrack_user.query.filter_by(_date=date).first()
                targetRow.delete()
                json_ready.append(targetRow.read())
            return jsonify(json_ready)
                





    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Update, '/update')
    api.add_resource(_Read, '/')
    api.add_resource(_Delete, '/delete')