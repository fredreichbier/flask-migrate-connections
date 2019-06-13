from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:test@192.168.33.101/test'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

print('Flask-SQLAlchemy db.session().bind = {!r}'.format(db.session().bind))
print('Flask-SQLAlchemy character_set_results = {}'.format(db.session().execute("SELECT @@character_set_results").fetchall()[0]))
