"""
Basic models of Flask ORM.
"""
import logging as lg
from flask_sqlalchemy import SQLAlchemy


from .views import app

# Create database connection object
db = SQLAlchemy(app)
# Access to config
app.config.from_object('config')
# To get one variable, type app.config['MY_VARIABLE']

class FoundryMaster(db.Model):
    """Structure"""
    email = db.Column(db.String(200), primary_key=True)
    port = db.Column(db.Integer, nullable=False)
    pseudo =  db.Column(db.String(200), nullable=False)
    def __init__(self,email, port = 30000,pseudo="No Pseudo"):
        self.email = email
        self.pseudo = pseudo
        self.port = port


def initDb():
    """Database initialization;
    careful: it wipes previous data first.
    """
    db.drop_all()
    db.create_all()
    db.session.add(FoundryMaster("christophe@morvans.net", 30000, "orome"))
    db.session.add(FoundryMaster("lenaianel@gmail.com", 30003, "lenaianel"))
    db.session.commit()
    lg.warning('Database initialized!')

