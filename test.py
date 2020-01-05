#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
import psycopg2

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
#db = SQLAlchemy(app)


conn = psycopg2.connect('dbname = postgres user = postgres password = postgres')

cur = conn.cursor()

cur.execute('select * from test')

rows = cur.fetchall()

print(rows)