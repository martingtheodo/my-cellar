import factory
from models import Winery
from . import OriginFactory

class WineryFactory(factory.Factory):
    class Meta:
        model = Winery

    name = factory.Faker('company', locale='fr_FR')
    origin = factory.SubFactory(OriginFactory)
