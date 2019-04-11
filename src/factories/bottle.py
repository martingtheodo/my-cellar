import factory
from models import Bottle
from . import CuveeFactory

class BottleFactory(factory.Factory):
    class Meta:
        model = Bottle

    type = factory.Faker('word', locale='fr_FR')
    vintage = factory.Faker('year', locale='fr_FR')
    cuvee = factory.SubFactory(CuveeFactory)
