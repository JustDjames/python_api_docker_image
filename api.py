from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Mack",
        "age": "34",
        "job": "Plumber"
    },
    {
        "name": "Danielle",
        "age": "26",
        "job": "Programmer"
    },
    {
        "name": "Nick",
        "age": "48",
        "job": "Dancer"
    }
]
class AllUsers(Resource):
    # return all users. Use GET method
    def get(self):
        return users, 200

class User(Resource):

    # return specified user. Use GET method
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not Found", 404
    
    
class DeleteUser(Resource):    
    def delete(self,name):
        global users
        users = [user for user in users if user["name"] !=name]
        return "{}  is deleted.".format(name), 200

class NewUser(Resource):
    # create new user. Use POST method
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("job")
        args = parser.parse_args()

        for user in users:
            if(args["name"] == user["name"]):
                return "User with name {} already exists".format(args["name"]), 400
        
        user = {
            "name": args["name"],
            "age": args["age"],
            "job": args["job"]
        }
        users.append(user)
        return user, 201

class UpdateUser(Resource):
    def put(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("job")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["name"]= args["name"]
                user["age"] = args["age"]
                user["job"] = args["job"]
                return user, 200
        return "user doesn't exist, to create a new user use /newuser route", 404
class Help(Resource):
    def get(self):
        helpMessage = "This is a Basic Api written in Python. It uses different routes to perform CRUD (Create, Read, Edit, and Delete) on a users list." \
        "Below are the Routes, their functions and the HTTP methods needed:" \
        "/help - Used to display this message - GET" \
        "/users - returns the full list of users - GET" \
        "/user/<name> - returns information for the specified user - GET" \
        "/newuser - add a new user to the users list - POST (new user must be in JSON format)" \
        "/user/<name>/update - updates the specified user with new infomation - PUT (new information must be in JSON format. Must include name even if name hasn't changed" \
        "/user/<name>/delete - Deletes the specified user - DELETE)" 
        return helpMessage, 200
api.add_resource(Help, "/help")
api.add_resource(User, "/user/<string:name>")
api.add_resource(AllUsers,"/users" )
api.add_resource(NewUser,"/newuser")
api.add_resource(UpdateUser,"/user/<string:name>/update")
api.add_resource(DeleteUser,"/user/<string:name>/delete")

app.run(debug=True)