# from flask import Blueprint, request, jsonify
# from flask_restful import Api, Resource
# from __init__ import db
# from model.users import User

# user_api = Blueprint('user_api', __name__,
#                    url_prefix='/api/users')

# api = Api(user_api)

# class UserAPI(Resource):
#     def post(self):
#         try:
#             ''' Read data for json body '''
#             body = request.get_json()
#             Workout = body.get('Workout')
#             Reps = body.get('Reps')
#             Sets = body.get('Sets')

#             ''' #1: Key code block, setup USER OBJECT '''
#             uo = User(Workout, Reps, Sets)

#             ''' #2: Key Code block to add user to database '''
#             # create user in database
#             db.session.add(uo)
#             db.session.commit()

#             # success returns json of user
#             return jsonify(uo.read())
#         except Exception as e:
#             db.session.rollback()
#             return {'message': str(e)}

#     def get(self):
#         users = User.query.all()    # read/extract all users from database
#         json_ready = [uo.read() for uo in users]  # prepare output in json
#         return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

# api.add_resource(UserAPI, "/")


from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource, reqparse # used for REST API building
from __init__ import db
from model.users import User

user_api = Blueprint('user_api', __name__,
                   url_prefix='/api/user')

api = Api(user_api)

class UserAPI(Resource):
    class _Create(Resource):
        def post(self):
            try: 
                "read data"
                body = request.form
                
                Workout = body.get('Workout')
                Reps = body.get('Reps')
                Sets = body.get('Sets')
                
                uo = User(Workout, Reps, Sets)
                
                create = uo.create()
                
                return jsonify(create.read())
            except Exception as e:
                return {'message':str(e)}
            
    class _Read(Resource):
        def get(self):
            users = User.query.all()    # read/extract all users from database
            json_ready = [uo.read() for uo in users]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    class _Delete(Resource):
        def delete(self):
            try:
                db.session.query(User).delete()
                db.session.commit()
                return {'message': 'All data has been cleared.'}
            except Exception as e:
                return {'message': str(e)}, 500

    api.add_resource(_Read, "/")
    api.add_resource(_Create, "/create")
    api.add_resource(_Delete, "/delete")
