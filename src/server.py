from flasgger import Swagger
from flask import Flask
from flask.blueprints import Blueprint
from flask_cors import CORS

import routes
from config import APPLICATION_ROOT, DB_URI, DEBUG, HOST, PORT, SQLALCHEMY_TRACK_MODIFICATIONS
from flask_debug_api import DebugAPIExtension
from flask_debugtoolbar import DebugToolbarExtension
from models import db

# config your API specs
# you can define multiple specs in the case your api has multiple versions
# ommit configs to get the default (all views exposed in /spec url)
# rule_filter is a callable that receives "Rule" object and
#   returns a boolean to filter in only desired views

server = Flask(__name__)

server.config["SWAGGER"] = {
    "swagger_version": "2.0",
    "title": "My Cellar",
    "specs": [
        {
            "version": "0.0.1",
            "title": "My cellar",
            "endpoint": "spec",
            "route": "/my-cellar/spec",
            "rule_filter": lambda rule: True,  # all in
        }
    ],
    "static_url_path": "/my-cellar/apidocs",
    "headers": [],
}

Swagger(server)

server.debug = DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
CORS(server, resources={r"/*": {"origins": "*"}}, headers=["Content-Type", "X-Requested-With", "Authorization"])
db.init_app(server)
db.app = server

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(blueprint, url_prefix=APPLICATION_ROOT)

server.secret_key = "development key"
DebugToolbarExtension(server)
DebugAPIExtension(server)

# Append Browse API Panel to Flask-DebugToolbar defaults
# (or add explicitly)
config = server.config
config["DEBUG_API_PREFIX"] = "/my-cellar"
panels = list(config["DEBUG_TB_PANELS"])
panels.append("flask_debug_api.BrowseAPIPanel")
config["DEBUG_TB_PANELS"] = panels


@server.route("/")
def index():
    return "<html><body></body></html>"


if __name__ == "__main__":
    server.run(host=HOST, port=PORT)
