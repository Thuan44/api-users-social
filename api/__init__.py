from flask_restful import Api

from app import flaskAppInstance
from .User import User
from .UserById import UserById

# Create REST server
restServer = Api(flaskAppInstance)

# Create a resource and the accessible routes
restServer.add_resource(User, "/api/user")
restServer.add_resource(UserById, "/api/user/id/<int:userId>")
