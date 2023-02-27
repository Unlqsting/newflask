from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource, reqparse # used for REST API building
from __init__ import db
from model.sport import sports

sport_api = Blueprint('sport_api', __name__,
                   url_prefix='/api/sport')

api = Api(sport_api)

class SportAPI(Resource):
    class _Create(Resource):
        def post(self):
            try: 
                "read data"
                body = request.get_json()
                
                goal = body.get('goal') 
                diff = body.get('diff')
                time = body.get('time')
                
                uo = sports(goal, diff, time)
                
                create = uo.create()
                
                return jsonify(create.read())
            except Exception as e:
                return {'message':str(e)}
            
    class _Read(Resource):
        def get(self):
            goals = sports.query.all()    # read/extract all users from database
            json_ready = [ath.read() for ath in goals]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
        
    class _Secure(Resource):

        def post(self):
            ''' Read data for json body '''
            body = request.get_json()

            ''' Get Data '''
            Goal = body.get('goal')
            Diff = body.get('diff')
            Time = body.get('time')

            return jsonify(sports.read())




    api.add_resource(_Read, "/")
    api.add_resource(_Create, "/create")
    api.add_resource(_Secure, "/authenticate")
                