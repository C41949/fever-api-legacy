import os

from flask import Flask

from database import db, db_name
from logs.views import logs
from temperature.views import temperatures

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(application)

application.register_blueprint(temperatures)
application.register_blueprint(logs)


@application.route("/")
def index():
    return 'Hi!'


if not os.path.isfile(f'../{db_name}'):
    with application.app_context():
        db.create_all()
