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

def abort_account_doesnt_exist(account_id):
    abort(404, "Account {} doesn't exist".format(account_id))

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

