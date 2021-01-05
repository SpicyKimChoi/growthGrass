from flask import Flask, request, jsonify, current_app
from flask_restx import Api, Resource
from sqlalchemy import create_engine, text
from controllers.test import Test

def create_app(test_config = None):		
    app = Flask(__name__)
    api = Api(app)

    if test_config is None:	
        app.config.from_pyfile("./db/config.py")
    else:
        app.config.update(test_config)

    database = create_engine(app.config['DB_URL'], encoding = 'utf-8', max_overflow = 0)
    app.database = database	

    api.add_namespace(Test, '/test')

    return app	