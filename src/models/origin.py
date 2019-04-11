from . import db
from .abstract_base_model import BaseModel


class Origin(db.Model,BaseModel):
    __tablename__ = "origin"
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    region =  db.Column(db.String(256), nullable=False)
    country =  db.Column(db.String(256), nullable=False)

    def __init__(
        self,
        region,
        country
    ):
        self.region=region
        self.country=country

    def to_json(self):
        return {
            "region" : self.region,
            "country" : self.country,
        }
