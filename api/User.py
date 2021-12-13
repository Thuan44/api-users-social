from flask_restful import Resource, reqparse
from flask import request
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
        cur = conn.cursor()
        sql = "INSERT INTO users (user_name, user_password, user_email) VALUES (%s, %s, %s)"
        userName = request.form["userName"]
        userPassword = request.form["userPassword"]
        userEmail = request.form["userEmail"]
        cur.execute(sql, (userName, userPassword, userEmail))
        conn.commit()
        cur.close()
        return {"message": "User added successfully"}, 201
