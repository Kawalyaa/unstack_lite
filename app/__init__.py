"""Creating app"""
from flask import Flask
from instance.config import app_config
"""importing the configurations from the .config file which is in the instance folder"""
from app.api.v1.views.question_views import question as qstn
from app.api.v1.views.answer_views import answer as ans
"""We import blueprint """


def create_app(config_name):
    '''creating  the app using the configurations in the dictionary created in the .config file'''
    app = Flask(__name__, instance_relative_config=True)
    """register blueprint"""
    app.register_blueprint(qstn)
    app.register_blueprint(ans)
    """Load the default configuration"""
    app.config.from_object(app_config['development'])
    """Load the configuration from the instance folder"""
    app.config.from_pyfile('config.py')
    return app
