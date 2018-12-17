from flask import Flask
from app.api.v1.views.user_views import version1 as v1

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(v1)

    return app
