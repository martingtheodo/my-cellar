from models import Bottle


class BottleRepository:
    @staticmethod
    def get_list():
        return Bottle.query.all()
