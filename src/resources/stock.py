from flask_restful import Resource
from repositories import StockRepository
from flasgger.utils import swag_from


class StockResource(Resource):
    @staticmethod
    @swag_from("../swagger/stock/GET.yml")
    def get():
        stocks = StockRepository.get_list()
        return [stock.to_json() for stock in stocks]
