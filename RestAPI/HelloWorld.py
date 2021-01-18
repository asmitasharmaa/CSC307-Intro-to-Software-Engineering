from flask import Flask
from flask import request
from flask import jsonify
from random_username.generate import generate_username
import random
from flask_cors import CORS
app = Flask(__name__)
CORS(app) # <--- add this line

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

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users

   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = idGenerator()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      resp.status_code = 201 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      print(userToAdd)
      return jsonify(userToAdd), 201

   elif request.method == 'DELETE':
      userToDel = request.get_json()
      userID = userToDel['id']
      for i in range(len(users['users_list'])):
         if users['users_list'][i]['id'] == userID:
            users['users_list'].pop(i)
            break
      return users  


@app.route('/users/<id>', methods = ['DELETE'])
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id: # and request.method == 'DELETE':
           users['users_list'].remove(user)
           resp = jsonify(success=True)
           return resp
      return ({})
   return users

@app.route('/users/<name>/<job>')
def get_user_nameJob(name, job):
   subdict = {'users_list' : []}
   if name and job:
      for user in users['users_list']:
        if user['name'] == name and user['job'] == job:
            subdict['users_list'].append(user)
      return subdict
      #return ({})
   return users


def idGenerator():
   print(generate_username(1)[0], str(random.randint(1, 1001)))
   return generate_username(1)[0]  + str(random.randint(1, 1001))



if __name__ == "__main__":
    app.run(debug=True)

