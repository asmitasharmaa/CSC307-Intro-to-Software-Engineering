from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

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
         'name': 'Asmi',
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
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp

   elif request.method == 'DELETE':
      userToDel = request.get_json()
      userID = userToDel['id']
      for i in range(len(users['users_list'])):
         if users['users_list'][i]['id'] == userID:
            users['users_list'].pop(i)
            break

      return users  


@app.route('/users/<id>')
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           return user
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



if __name__ == "__main__":
    app.run(debug=True)

