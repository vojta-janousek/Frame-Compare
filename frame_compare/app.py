from flask import Flask
from decouple import config

from routes import route_blueprint


def create_app():
    app = Flask(__name__)
    app.debug = config('DEBUG')

    app.register_blueprint(route_blueprint)

    return app


if (__name__ == '__main__'):
    app = create_app()
    app.run()
