from flask_script import Command
from factories import BottleFactory
from models import db


class FixturesCommand(Command):
    def run(self):
        bottles = BottleFactory.build_batch(1000)
        for bottle in bottles:
            db.session.add(bottle)
        db.session.commit()
