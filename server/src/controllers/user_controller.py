from flask import Flask, request, jsonify, current_app, abort
from sqlalchemy import create_engine, text
from flask_restx import Resource, Api, Namespace, fields

User = Namespace(
    name = 'User',
    description="유저 정보에 관한 API"
)

user_login_fields = User.model('User', {  # Model 객체 생성
    'androidId': fields.String(description='안드로이드 아이디', required=True, example="123123")
})

user_signup_fields = User.model('User', {  # Model 객체 생성
    'androidId': fields.String(description='안드로이드 아이디', required=True, example="123123"),
    'username': fields.String(description='유저 닉네임', required=True, example="원준대로")
})

def abort_account_doesnt_exist(account_id):
    abort(404, "Account {} doesn't exist".format(account_id))

def abort_account_already_exist(account_id):
    abort(409, "Account {} already exist".format(account_id))

@User.route('/login')
class Login(Resource):
    @User.response(200, 'Success')
    @User.response(404, '등록되지 않은 유저입니다.')
    @User.expect(user_login_fields)
    def post(self):
        """ androidId를 바탕으로 로그인을 진행합니다. """ 
        androidId = request.json.get('androidId')
        print(androidId)
        
        row = current_app.database.execute(text(f"""
            select * from users where android_id = {androidId};
        """)).fetchone()
        
        if row == None :
            # abort(404, '등록되지 않은 유저입니다.') 
            abort_account_doesnt_exist(androidId)
        return {
            'id': row['id']
        }, 200

@User.route('/signup')
class Signup(Resource):
    @User.response(201, 'Success')
    @User.response(409, '이미 존재하는 유저입니다.')
    @User.expect(user_signup_fields)
    def post(self):
        """ androidId를 바탕으로 회원가입을 진행합니다. """ 
        androidId = request.json.get('androidId')
        username = request.json.get('username')
        
        #이미 등록된 안드로이드 기기가 있는경우, (제약조건 추가?)
        isExist = current_app.database.execute(text(f"""
            select * from users where android_id = {androidId};
        """)).fetchone()

        if isExist is not None:
            abort_account_already_exist(androidId)

        current_app.database.execute(text(f"""
            insert into users (android_id, user_name) value ("{androidId}", "{username}");
        """))

        row = current_app.database.execute(text(f"""
            select * from users where android_id = {androidId};
        """)).fetchone()
        print(row)
        return {
            'id': row['id']
        }, 201