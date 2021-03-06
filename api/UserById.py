from flask_restful import Resource
from flask import request
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

    def put(self, userId):
        cur = conn.cursor()
        sql = "UPDATE users SET user_name = %s, user_password = %s, user_email = %s WHERE user_id = %s"
        userName = request.form["userName"]
        userPassword = request.form["userPassword"]
        userEmail = request.form["userEmail"]
        cur.execute(sql, (userName, userPassword, userEmail, userId))
        conn.commit()
        cur.close()
        return {"message": "User updated successfully"}, 200

    def delete(self, userId):
        cur = conn.cursor()
        sql = "DELETE FROM users WHERE user_id = %s"
        cur.execute(sql, format(userId))
        conn.commit()
        cur.close()
        return {"message": "User deleted successfully"}, 200
