from flask import Blueprint, current_app, jsonify
from flask_restful import Api

common_blueprint = Blueprint("common", __name__)
common_blueprint_api = Api(common_blueprint)


@common_blueprint.route("/routes")
def list_routes():
    """ List all the routes available for an API """
    output = []
    for rule in current_app.url_map.iter_rules():
        methods = ",".join(rule.methods)
        line = "{:50s} {:20s}".format(str(rule), methods)
        output.append(line)
    return jsonify(routes=output)


@common_blueprint.route("/ping")
def is_running():
    """ Return OK if API is running """
    return "OK"
