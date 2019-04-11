from . import db
from .abstract_base_model import BaseModel


class GrapeVariety(db.Model,BaseModel):
    __tablename__ = "grape_variety"
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    name =  db.Column(db.String(256), nullable=False)

    def __init__(
        self,
        name,
    ):
        self.name=name

    def to_json(self):
        return {
            "name" : self.name,
        }
