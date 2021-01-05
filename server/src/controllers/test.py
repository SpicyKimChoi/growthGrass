from flask import Flask, request, jsonify, current_app
from sqlalchemy import create_engine, text
from flask_restx import Resource, Api, Namespace

Test = Namespace('Test')

@Test.route('')
class Testg(Resource):
    def get(self):
        row = current_app.database.execute(text("""
            select * from log where habbit_id in (select id from habbit where userid = 1);
        """)).fetchone()

        return jsonify({
            'id': row['id'], 
            'habbit_id': row['habbit_id'],
            'date': row['date'],
            'description': row['description'],
            'status': row['status'],
        })