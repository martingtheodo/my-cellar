import factory
from models import Cuvee
from . import WineryFactory
from .appellation import AppellationFactory
from .grape_variety import GrapeVarietyFactory

class CuveeFactory(factory.Factory):
    class Meta:
        model = Cuvee

    name = factory.Faker('words', locale='fr_FR', nb=3)
    colour = name = factory.Faker('word', locale='fr_FR')
    winery = factory.SubFactory(WineryFactory)
    appellation = factory.SubFactory(AppellationFactory)
    grape_varieties = GrapeVarietyFactory.build_batch(2)
