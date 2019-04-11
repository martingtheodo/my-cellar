from flask_restful import Resource
from repositories import WineryRepository
from flasgger.utils import swag_from


class WineryResource(Resource):
    @staticmethod
    @swag_from("../swagger/winery/GET.yml")
    def get():
        wineries = WineryRepository.get_list()
        return [winery.to_json() for winery in wineries]
