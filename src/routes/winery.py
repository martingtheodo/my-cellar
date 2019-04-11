from flask import Blueprint
from flask_restful import Api
from resources import WineryResource

WINERY_BLUEPRINT = Blueprint("winery", __name__)
Api(WINERY_BLUEPRINT).add_resource(WineryResource, "/winery", endpoint="winery")
