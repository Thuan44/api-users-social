from flask_restful import Resource
import logging as logger
from database.database import conn


class UserById(Resource):
    def get(self, userId):
        cur = conn.cursor()
        sql = "SELECT * FROM users WHERE user_id = %s"
        cur.execute(sql, format(userId))
        data = cur.fetchone()
        user = {
            "user_id": data[0],
            "user_name": data[1],
            "user_password": data[2],
            "user_email": data[3],
        }
        cur.close()
        return user, 200

    # def post(self, userId):
    #     logger.debug("Inside post method of user by id")
    #     return {
    #         "message": "Inside post method of user by id. User ID = {}".format(userId)
    #     }, 200

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
