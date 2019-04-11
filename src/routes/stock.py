from flask import Blueprint
from flask_restful import Api
from resources import StockResource

STOCK_BLUEPRINT = Blueprint("stock", __name__)
Api(STOCK_BLUEPRINT).add_resource(StockResource, "/stock", endpoint="stock")
