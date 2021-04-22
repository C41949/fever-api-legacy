import os

from flask import Flask
from flask_cors import CORS

from database import db, dev_db, prod_db
from logs.views import logs
from temperature.views import temperatures

application = Flask(__name__)
application.register_blueprint(temperatures)
application.register_blueprint(logs)
CORS(application)

is_dev = os.getenv('mode', 'dev') == 'dev'
application.config['SQLALCHEMY_DATABASE_URI'] = dev_db if is_dev else prod_db
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(application)

with application.app_context():
    db.create_all()


@application.route("/")
def index():
    return 'Up and running 🚀'


if is_dev:
    application.run(debug=True)
