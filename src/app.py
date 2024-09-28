from flask import Flask

def create_app(test_config: dict = None) -> Flask:
    """
    :param test_config:
    """
    app = Flask(__name__, instance_relative_config=True)

    if test_config:
        app.config.from_mapping(test_config)

    app.config.from_pyfile("config.py")

    return app