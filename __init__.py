from flask import Flask
from extensions.extensions import db, migrate, bcrypt, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.config.Config")
    
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    return app