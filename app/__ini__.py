"""Creating app"""
from flask import Flask
from instance.config import app_config
"""importing the configurations from the .config file which is in the instance folder"""
from app.version1 import app_one as v1
"""We import blueprint from the init file located in the version1 folder"""


def create_app(config_name):
    '''creating  the app using the configurations in the dictionary created in the .config file'''
    app = Flask(__name__, instance_relative_config=True)
    """register blueprint"""
    app.register_blueprint(v1)
    """Load the default configuration"""
    app.config.from_object(app_config['development'])
    """Load the configuration from the instance folder"""
    app.config.from_pyfile('config.py')
    return app
