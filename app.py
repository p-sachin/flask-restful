from flask import Flask
from flask_restful import Resource, Api
from routes.home.route import HomeRoute, HomeRouteWithId
from utils.db import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    if app.config is None:
        app.config.from_object(app.config.BaseConfig)
    else:
        app.config.from_object(app.config)

    db.init_app(app) # Initialize the database 
    db.create_all(app=app) # Create tables
    api = Api(app)
    api.add_resource(HomeRoute, '/todos/')
    api.add_resource(HomeRouteWithId, '/todos/<string:id>')
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)