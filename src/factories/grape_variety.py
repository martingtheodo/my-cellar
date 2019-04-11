import factory
from models import GrapeVariety

class GrapeVarietyFactory(factory.Factory):
    class Meta:
        model = GrapeVariety

    name = factory.Faker('word', locale='fr_FR')
