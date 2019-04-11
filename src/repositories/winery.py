from models import Winery


class WineryRepository:
    @staticmethod
    def get_list():
        return Winery.query.all()
