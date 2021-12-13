from flask_restful import Resource
import logging as logger


class UserById(Resource):
    def get(self, userId):
        logger.debug("Inside get method of user by id")
        return {
            "message": "Inside get method of user by id. User ID = {}".format(userId)
        }, 200

    def post(self, userId):
        logger.debug("Inside post method of user by id")
        return {
            "message": "Inside post method of user by id. User ID = {}".format(userId)
        }, 200

    def put(self, userId):
        logger.debug("Inside put method of user by id")
        return {
            "message": "Inside put method of user by id. User ID = {}".format(userId)
        }, 200

    def delete(self, userId):
        logger.debug("Inside delete method of user by id")
        return {
            "message": "Inside delete method of user by id. User ID = {}".format(userId)
        }, 200
