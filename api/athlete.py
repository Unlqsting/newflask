from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource, reqparse # used for REST API building
from __init__ import db
from model.athletes import Athlete

athlete_api = Blueprint('athlete_api', __name__,
                   url_prefix='/api/athlete')

api = Api(athlete_api)

class AthleteAPI(Resource):
    class _Create(Resource):
        def post(self):
            try:
                ''' Read data for json body '''
                body = request.get_json()
                
                Age = body.get('Age')
                if Age is None or len(Age)< 1:
                    return {'message': f'Age is missing, or is less than 1 character'}, 400
                
                Weight = body.get('Weight')
                if Weight is None or len(Weight)< 1:
                    return {'message': f'Weight is missing, or is less than 1 character'}, 400
                
                Bench = body.get('Bench')
                if Bench is None or len(Bench)< 1:
                    return {'message': f'Bench is missing, or is less than 1 character'}, 400
                
                Squat = body.get('Squat')
                if Squat is None or len(Age)< 1:
                    return {'message': f'Squat is missing, or is less than 1 character'}, 400
                
                Pullup= body.get('Pullup')
                if Pullup is None or len(Pullup)< 1:
                    return {'message': f'Pullup is missing, or is less than 1 character'}, 400
                
                Mile = body.get('Mile')
                if Mile is None or len(Mile)< 1:
                    return {'message': f'Mile is missing, or is less than 1 character'}, 400

                ''' #1: Key code block, setup USER OBJECT '''
                uo = Athlete(Age, Weight, Bench, Squat, Pullup, Mile)
                
                ''' #2: Key Code block to add user to database '''
                # create user in database
                user = uo.create()
                # success returns json of user
            
                return jsonify(user.read())
            except Exception as e:
                return {'message':str(e)}
    # resources
   # class _Create(Resource):
    #    def post(self):
     #       parser = reqparse.RequestParser()
      #      parser.add_argument("Weight", required=False, type=int)
       #     parser.add_argument("Bench", required=False, type=int)
        #    parser.add_argument("Squat", required=False, type=int)
         #   parser.add_argument("Press", required=False, type=int)
          #  parser.add_argument("Pushup", required=False, type=int)
           # args = parser.parse_args()

            #athlete = Athlete(args["Weight"], args["Bench"], args["Squat"], args["Press"], args["Pushup"])
            #try:
             #   db.session.add(athlete)
              #  db.session.commit()
               # return athlete.to_dict(), 201
            #except Exception as e:
             #   db.session.rollback()
              #  return {"message": f"server error: {e}"}, 500

    class _Read(Resource):
        def get(self):
            athletes = Athlete.query.all()    # read/extract all users from database
            json_ready = [ath.read() for ath in athletes]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    class _Security(Resource):

        def post(self):
            ''' Read data for json body '''
            body = request.get_json()

            ''' Get Data '''
            Age = body.get('Age')
            Weight = body.get('Weight')
            Bench = body.get('Bench')
            Squat = body.get('Squat')
            Pullup = body.get('Pullup')
            Mile = body.get('Mile')

            return jsonify(Athlete.read())


    api.add_resource(_Read, "/")
    api.add_resource(_Create, "/create")
    api.add_resource(_Security, '/authenticate')



