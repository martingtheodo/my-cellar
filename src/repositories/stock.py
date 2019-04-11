from models import Stock


class StockRepository:
    @staticmethod
    def get_list():
        return Stock.query.all()
