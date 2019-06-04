from flask import Flask, jsonify, make_response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = [
    {
        "name": "mack",
        "age": "34",
        "job": "plumber"
    },
    {
        "name": "danielle",
        "age": "26",
        "job": "programmer"
    },
    {
        "name": "nick",
        "age": "48",
        "job": "dancer"
    }
]

@app.route('/')
def index():
    helpMessage = "This is a Basic Api written in Python. It uses different routes to perform CRUD (Create, Read, Edit, and Delete) on a users list.\n" \
    "Below are the Routes, their functions and the HTTP methods needed:\n" \
    "/ - Used to display this message - GET\n" \
    "/users - returns the full list of users - GET\n" \
    "/user/<name> - returns information for the specified user - GET\n" \
    "/newuser - add a new user to the users list - POST (new user must be in JSON format)\n" \
    "/user/<name>/update - updates the specified user with new infomation - PUT (new information must be in JSON format. Must include name even if name hasn't changed\n" \
    "/user/<name>/delete - Deletes the specified user - DELETE)\n" 
    return helpMessage, 200

@app.route('/users')
def get_users():
    return jsonify(users)

@app.route('/user/<string:name>', methods=['GET'])
def get_user(name):
    name = name.lower()
    user = [user for user in users if user['name'] == name]
    if len(user) == True:
        return jsonify(user[0])
    return jsonify('User not Found'), 404

@app.route('/new',methods=['POST'])
def create_user():
    if not request.json:
        return jsonify('request must be made in JSON'), 400
    elif not 'name'in request.json or len(request.json['name']) == 0:
        return jsonify('Missing parameter. ensure request has name'), 400
    elif not 'age' in request.json or len(request.json['age']) == 0:
        return jsonify('Missing parameter. ensure request has age'), 400
    elif not 'job'in request.json or len(request.json['job']) == 0:
        return jsonify('Missing parameter. ensure request has job'), 400
    
    for user in users:
        if(request.json['name'] == user['name']):
            return jsonify("user with that name already exists"), 400
    
    user = {
        'name': request.json['name'].lower(),
        'age': request.json['age'].lower(),
        'job': request.json['job'].lower()
    }
    users.append(user)
    return jsonify(user), 201

@app.route('/update/<string:name>',methods=['PUT'])
def update_user(name):
    name = name.lower()
    user = [user for user in users if user['name'] == name]
    if len(user) == 0:
        return jsonify('User not found'),404
    if not request.json:
        return jsonify('request must be made in JSON'), 400
    elif not 'name'in request.json or len(request.json['name']) == 0:
        return jsonify('Missing parameter. ensure request has name'), 400
    elif not 'age' in request.json or len(request.json['age']) == 0:
        return jsonify('Missing parameter. ensure request has age'), 400
    elif not 'job'in request.json or len(request.json['job']) == 0:
        return jsonify('Missing parameter. ensure request has job'), 400
    
    user[0]['name'] = request.json.get('name', user[0]['name']).lower()
    user[0]['age'] = request.json.get('age', user[0]['age']).lower()
    user[0]['job'] = request.json.get('job', user[0]['job']).lower()
    return jsonify(user[0]), 201
@app.route('/delete/<string:name>', methods=['DELETE'])
def delete_user(name):
    name = name.lower()
    user = [user for user in users if user['name'] == name]
    if len(user) == 0:
        return jsonify('User not found'), 404
    users.remove(user[0])
    return jsonify('User deleted'),201

app.run(host='0.0.0.0',port=5000,debug=True)