from flask import Flask
from flask import request
from flask import jsonify
from random_username.generate import generate_username
import random
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 

@app.route('/')
def hello_world():
	return 'Hello, world!'


users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Professor',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Asmi',
         'job': 'Computer Scientist',
      },
      {
         'id' : 'pat2020', 
         'name': 'Peepa',
         'job': 'Computer Scientist',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      username = request.args.get('name')
      job = request.args.get('job')

      if username and job:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == username and user['job'] == job:
               subdict['users_list'].append(user)
         return subdict

      elif username:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == username:
               subdict['users_list'].append(user)
         return subdict

      elif job:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['job'] == job:
               subdict['users_list'].append(user)
         return subdict
      return users

   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = idGenerator()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      resp.status_code = 201 # optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return jsonify(userToAdd), 201
  
@app.route('/users/<id>', methods = ['GET', 'DELETE'])
def get_user(id):
   if id and request.method == 'DELETE' :
      for user in users['users_list']:
        if user['id'] == id:
           users['users_list'].remove(user)
           resp = jsonify(success=True)
           resp.status_code = 204
           return resp
      return ({})

   if id and request.method == 'GET' :
      for user in users['users_list']:
        if user['id'] == id:
           return user

   return users

@app.route('/users/<name>/<job>')
def get_user_nameJob(name, job):
   subdict = {'users_list' : []}
   if name and job:
      for user in users['users_list']:
        if user['name'] == name and user['job'] == job:
            subdict['users_list'].append(user)
      return subdict
      
   return users


def idGenerator():
   return generate_username(1)[0]  + str(random.randint(1, 1001))



if __name__ == "__main__":
    app.run(debug=True)

