from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from .winery import Winery
from .origin import Origin
from .appellation import Appellation
from .grape_variety import GrapeVariety
from .cuvee import Cuvee
from .appellation import Appellation
from .bottle import Bottle
from .stock import Stock
