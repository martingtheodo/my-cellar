from . import db
from .abstract_base_model import BaseModel

cuvee_grape_variety_table = db.Table('cuvee_grape_variety', db.Model.metadata,
    db.Column('cuvee_id', db.Integer, db.ForeignKey('cuvee.id')),
    db.Column('grape_variety_id', db.Integer, db.ForeignKey('grape_variety.id'))
)

class Cuvee(db.Model,BaseModel):
    __tablename__ = "cuvee"
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    name =  db.Column(db.String(256), nullable=False)
    colour =  db.Column(db.String(128), nullable=False)
    winery_id = db.Column(db.Integer, db.ForeignKey("winery.id"), nullable=False)
    winery = db.relationship("Winery", lazy="joined")
    appellation_id = db.Column(db.Integer, db.ForeignKey("appellation.id"), nullable=False)
    appellation = db.relationship("Appellation", lazy="joined")
    grape_varieties = db.relationship("GrapeVariety",
                    secondary=cuvee_grape_variety_table, lazy="joined")

    def __init__(
        self,
        name,
        colour,
        winery,
        appellation,
        grape_varieties
    ):
        self.name=name
        self.colour=colour
        self.winery=winery
        self.appellation=appellation
        self.grape_varieties=grape_varieties

    def to_json(self):
        return {
            "name" : self.name,
            "colour" : self.colour,
            "appellation" : self.appellation.to_json(),
            "winery": self.winery.to_json(),
            "grape_varieties": [grape_variety.to_json() for grape_variety in self.grape_varieties]
        }
