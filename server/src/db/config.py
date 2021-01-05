import os

db = {
	'user': os.environ['DATABASE_USER'],
	'password': os.environ['DATABASE_PWD'],
	'host': 'localhost',
	'port': 3306,
	'database': os.environ['DATABASE_NAME']
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"

print(db)