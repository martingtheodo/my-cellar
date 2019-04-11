from flask_restful import Resource
from repositories import BottleRepository
from flasgger.utils import swag_from


class BottleResource(Resource):
    @staticmethod
    @swag_from("../swagger/bottle/GET.yml")
    def get():
        bottles = BottleRepository.get_list()
        return [bottle.to_json() for bottle in bottles]
