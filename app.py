import os

from flask import Flask

from database import db, db_name
from temperature.views import temperatures


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(temperatures)
    return app


def setup_db():
    if not os.path.isfile(f'../{db_name}'):
        with app.app_context():
            db.create_all()


if __name__ == '__main__':
    app = create_app()
    setup_db()
    app.run(port=8001, debug=True)
