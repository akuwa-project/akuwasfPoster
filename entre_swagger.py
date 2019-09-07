#!/usr/bin/env python3.6
import settings
from flask import Flask, Blueprint
from e_user import ns as e_user_namespace
from poster import ns as poster_namespace
from restful import api

app = Flask(__name__)

def configure_app(flask_app):
    #flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/swagger-ui.html')
    api.init_app(blueprint)
    api.add_namespace(e_user_namespace)
    api.add_namespace(poster_namespace)
    flask_app.register_blueprint(blueprint)


def main():
    initialize_app(app)
    # log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(host='0.0.0.0', port='9090', debug=True)




if __name__ == "__main__":
    main()
