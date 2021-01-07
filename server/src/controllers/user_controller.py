from flask import Flask, request, jsonify, current_app, abort
from sqlalchemy import create_engine, text
from flask_restx import Resource, Api, Namespace

User = Namespace('User')

def abort_account_doesnt_exist(account_id):
    abort(404, "Account {} doesn't exist".format(account_id))

@User.route('/login')
@User.response(404, '등록되지 않은 유저입니다.')
class Login(Resource):
    def post(self):
        androidId = request.json.get('androidId')
        print(androidId)
        
        row = current_app.database.execute(text(f"""
            select * from users where android_id = {androidId};
        """)).fetchone()
        
        if row == None :
            # abort(404, '등록되지 않은 유저입니다.') 
            abort_account_doesnt_exist(androidId)
        return jsonify({
            'id': row['id']
        })