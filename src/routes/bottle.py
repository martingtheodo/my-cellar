from flask import Blueprint
from flask_restful import Api
from resources import BottleResource

BOTTLE_BLUEPRINT = Blueprint("bottle", __name__)
Api(BOTTLE_BLUEPRINT).add_resource(BottleResource, "/bottle", endpoint="bottle")
