from . import db
from .abstract_base_model import BaseModel


class Stock(db.Model,BaseModel):
    __tablename__ = "stock"
    quantity =  db.Column(db.Integer, nullable=False)
    bottle_id =  db.Column(db.Integer, db.ForeignKey("bottle.id"),primary_key=True, nullable=False)
    bottle = db.relationship("Bottle", lazy="joined")

    def __init__(
        self,
        quantity,
        bottle_id
    ):
        self.quantity=quantity
        self.bottle_id=bottle_id

    def to_json(self):
        return {
            "quantity" : self.quantity,
            "bottle" : self.bottle.to_json(),
        }
