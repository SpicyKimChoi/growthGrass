from flask import Flask, request, jsonify, current_app
from sqlalchemy import create_engine, text

def create_app(test_config = None):		
    app = Flask(__name__)

    # app.json_encoder = CustomJSONEncoder

    if test_config is None:	
        app.config.from_pyfile("./db/config.py")
    else:
        app.config.update(test_config)

    database = create_engine(app.config['DB_URL'], encoding = 'utf-8', max_overflow = 0)
    app.database = database	
    
    @app.route('/test', methods=['GET'])
    def test():
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

    return app	