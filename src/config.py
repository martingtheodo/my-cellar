import logging
import os

DEBUG = True if os.getenv("DEBUG_MODE") == "True" else False
APPLICATION_ROOT = os.getenv("MY_CELLAR_APPLICATION_ROOT", "/my-cellar")
HOST = os.getenv("MY_CELLAR_HOST", "0.0.0.0")
PORT = int(os.getenv("MY_CELLAR_PORT", "5044"))
WORKER_COUNT = os.getenv("MY_CELLAR_WORKER_COUNT", 1)

DB_CONTAINER = os.getenv("MY_CELLAR_DB_CONTAINER", "db")
DATABASE = {
    "type": "mysql",
    "user": os.getenv("MY_CELLAR_DB_USER"),
    "pw": os.getenv("MY_CELLAR_DB_PW", ""),
    "host": os.getenv("MY_CELLAR_DB_HOST", DB_CONTAINER),
    "port": os.getenv("MY_CELLAR_DB_PORT", 3306),
    "db": os.getenv("MY_CELLAR_DB_NAME", "my_cellar"),
}
DB_URI = "%(type)s://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s?charset=utf8" % DATABASE

logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# Disable Flask-SQLAlchemy event system
SQLALCHEMY_TRACK_MODIFICATIONS = False
