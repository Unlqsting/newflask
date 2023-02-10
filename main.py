import threading
from api.athlete import athlete_api 

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from model.jokes import initJokes
from model.users import initUsers
from model.athletes import initAthletes
from model.sport import initSports
from model.signups import initSignups
from model.etrack_users import initEtrackUsers

# setup APIs
from api.covid import covid_api # Blueprint import api definition
from api.joke import joke_api # Blueprint import api definition
from api.user import user_api # Blueprint import api definition
from api.athlete import athlete_api
from api.signup import signup_api
from api.etrack_user import etrack_user_api
# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition

# register URIs
app.register_blueprint(joke_api) # register api routes
app.register_blueprint(covid_api) # register api routes
app.register_blueprint(user_api) # register api routes
app.register_blueprint(app_projects) # register app pages
app.register_blueprint(athlete_api)
app.register_blueprint(signup_api)
app.register_blueprint(etrack_user_api)

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")   

@app.before_first_request
def activate_job():
    initJokes()
    initUsers()
    initAthletes()
    initSignups()
    initEtrackUsers()
    
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,PATCH')
  return response

# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volumes/sqlite.db'
    app.run(debug=True, host="0.0.0.0", port="8086")
