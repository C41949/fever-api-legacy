from flask_sqlalchemy import SQLAlchemy

dev_db = 'sqlite:///db.db'
prod_db = 'postgresql://postgres:postgres@fever-database:5432/temperature'

db = SQLAlchemy()
