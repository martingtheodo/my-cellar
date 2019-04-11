import factory
from models import Origin

class OriginFactory(factory.Factory):
    class Meta:
        model = Origin

    region = factory.Faker('city', locale='fr_FR')
    country = factory.Faker('country', locale='fr_FR')
