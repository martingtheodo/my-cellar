from . import db
from .abstract_base_model import BaseModel


class Bottle(db.Model,BaseModel):
    __tablename__ = "bottle"
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    vintage =  db.Column(db.String(4), nullable=False)
    cuvee_id = db.Column(db.Integer, db.ForeignKey("cuvee.id"), nullable=False)
    cuvee = db.relationship("Cuvee", lazy="joined")
    type = db.Column(db.String(32), nullable=False)

    def __init__(
        self,
        vintage,
        cuvee,
        type = 'classic',
    ):
        self.vintage=vintage
        self.type = type
        self.cuvee = cuvee

    def to_json(self):
        return {
            "vintage" : self.vintage,
            "type" : self.type,
            "cuvee" : self.cuvee.to_json()
        }
