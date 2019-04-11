from . import db
from .abstract_base_model import BaseModel


class Winery(db.Model,BaseModel):
    __tablename__ = "winery"
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    name =  db.Column(db.String(256), nullable=False)
    origin_id = db.Column(db.Integer, db.ForeignKey("origin.id"), nullable=False)
    origin = db.relationship("Origin", lazy="joined")

    def __init__(
        self,
        name,
        origin
    ):
        self.name=name
        self.origin=origin

    def to_json(self):
        return {
            "name" : self.name,
            "origin" : self.origin.to_json()
        }
