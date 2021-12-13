from flask_restful import Resource
import logging as logger
from database.database import conn


class User(Resource):
    def get(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
        users = []
        for user in data:
            users.append(
                {
                    "user_id": user[0],
                    "user_name": user[1],
                    "user_password": user[2],
                    "user_email": user[3],
                }
            )
        cur.close()
        return users, 200

    def post(self):
        logger.debug("Inside post method")
        return {"message": "Inside post method"}, 200

    # def put(self):
    #     logger.debug("Inside put method")
    #     return {"message": "Inside put method"}, 200

    # def delete(self):
    #     logger.debug("Inside delete method")
    #     return {"message": "Inside delete method"}, 200
