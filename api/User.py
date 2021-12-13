from flask_restful import Resource
import logging as logger
from database.database import conn
import json

# Open a cursor to perform database operations
cur = conn.cursor()


class User(Resource):
    def get(self):
        logger.debug("Inside get method")
        return {"message": "Inside post method"}, 200

    def post(self):
        logger.debug("Inside post method")
        return {"message": "Inside post method"}, 200

    def put(self):
        logger.debug("Inside put method")
        return {"message": "Inside put method"}, 200

    def delete(self):
        logger.debug("Inside delete method")
        return {"message": "Inside delete method"}, 200
