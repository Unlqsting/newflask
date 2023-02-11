# from flask import Blueprint, request, jsonify
# from flask_restful import Api, Resource, reqparse # used for REST API building
# from __init__ import db
# from model.users import User

# user_api = Blueprint('user_api', __name__,
#                    url_prefix='/api/users')

# api = Api(user_api)

# class UserAPI(Resource):
#     class _Create(Resource):
#         def post(self):
#             try:
#                 ''' Read data for json body '''
#                 body = request.get_json()
                
#                 Workout = body.get('Workout')
#                 Reps = body.get('Reps')
#                 Sets = body.get('Sets')

#                 ''' #1: Key code block, setup USER OBJECT '''
#                 uo = User(Workout, Reps, Sets)
                
#                 ''' #2: Key Code block to add user to database '''
#                 # create user in database
#                 user = user.create()
#                 # success returns json of user
            
#                 return jsonify(uo.read())
#             except Exception as e:
#                 return {'message':str(e)}
#     # resources
#     # class _Create(Resource):
#     #    def post(self):
#     #     parser = reqparse.RequestParser()
#     #     parser.add_argument("Weight", required=False, type=int)
#     #     parser.add_argument("Bench", required=False, type=int)
#     #     parser.add_argument("Squat", required=False, type=int)
#     #     parser.add_argument("Press", required=False, type=int)
#     #     parser.add_argument("Pushup", required=False, type=int)
#     #     args = parser.parse_args()

#     #     athlete = Athlete(args["Weight"], args["Bench"], args["Squat"], args["Press"], args["Pushup"])
#     #     try:
#     #         db.session.add(athlete)
#     #         db.session.commit()
#     #         return athlete.to_dict(), 201
#     #     except Exception as e:
#     #         db.session.rollback()
#     #         return {"message": f"server error: {e}"}, 500

#     class _Read(Resource):
#         def get(self):
#             users = User.query.all()    # read/extract all users from database
#             json_ready = [User.read() for User in users]  # prepare output in json
#             return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

#     api.add_resource(_Read, "/")
#     api.add_resource(_Create, "/create")
    

from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from __init__ import db
from model.users import User

user_api = Blueprint('user_api', __name__,
                   url_prefix='/api/users')

api = Api(user_api)

class UserAPI(Resource):
    def post(self):
        try:
            ''' Read data for json body '''
            body = request.get_json()
            Workout = body.get('Workout')
            Reps = body.get('Reps')
            Sets = body.get('Sets')

            ''' #1: Key code block, setup USER OBJECT '''
            uo = User(Workout, Reps, Sets)

            ''' #2: Key Code block to add user to database '''
            # create user in database
            db.session.add(uo)
            db.session.commit()

            # success returns json of user
            return jsonify(uo.read())
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}

    def get(self):
        users = User.query.all()    # read/extract all users from database
        json_ready = [uo.read() for uo in users]  # prepare output in json
        return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

api.add_resource(UserAPI, "/")

