from flask import Flask

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from stackoverflow.main.routes import main
    from stackoverflow.users.routes import users
    app.register_blueprint(main)
    app.register_blueprint(users)

    return app
