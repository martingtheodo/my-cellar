from . import db
from .abstract_base_model import BaseModel


class Appellation(db.Model,BaseModel):
    __tablename__ = "appellation"
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    name =  db.Column(db.String(256), nullable=False)
    origin_id = db.Column(db.Integer, db.ForeignKey("origin.id"), nullable=False)
    origin = db.relationship("Origin")

    def __init__(
        self,
        name,
        origin,
    ):
        self.name=name
        self.origin=origin

    def to_json(self):
        return {
            "name" : self.name,
        }
