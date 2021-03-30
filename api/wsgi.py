from flask import Flask

from database import db
from logs.views import logs
from temperature.views import temperatures

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@fever-database:5432/temperature'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

application.register_blueprint(temperatures)
application.register_blueprint(logs)

db.init_app(application)

with application.app_context():
    db.create_all()


@application.route("/")
def index():
    return 'Hi!'
