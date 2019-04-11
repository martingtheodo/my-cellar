import factory
from models import Appellation
from . import OriginFactory

class AppellationFactory(factory.Factory):
    class Meta:
        model = Appellation

    name = factory.Faker('word', locale='fr_FR')
    origin = factory.SubFactory(OriginFactory)
