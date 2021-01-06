from flask import Flask, request, jsonify, current_app
from sqlalchemy import create_engine, text
from flask_restx import Resource, Api, Namespace

User = Namespace('User')

@User.route('/login')
class Login(Resource):
    def post(self):
        androidId = request.json.get('androidId')
        print(androidId)
        
        row = current_app.database.execute(text(f"""
            select * from users where android_id = {androidId};
        """)).fetchone()

        return jsonify({
            'id': row['id']
        })