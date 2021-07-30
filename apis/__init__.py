from flask_cors import CORS
from flask_restx import Api
from flask import Blueprint
from app import app

VERSION = "v1"

blueprint = Blueprint(VERSION, __name__)

# Set up cross-scripting allowed
CORS(blueprint)

# Set up the API and init the blueprint
api = Api(default="Klarna Assignment Service", default_label="")
api.init_app(blueprint)

app.register_blueprint(blueprint, url_prefix = '/api/{}'.format(VERSION))