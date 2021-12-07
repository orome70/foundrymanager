"""
Module d'initialisation, avec la méthode d'initialisation des bases.
"""
from flask import Flask
from .views import app
from . import models

models.db.init_app(app)
app.config.from_object('config')
tmpUri = app.config['SQLALCHEMY_DATABASE_URI']
print(tmpUri + '\n')


@app.cli.command('initDb')
def initDb():
    """Initialisation de la base de donnée. 
     Attention : efface tout le contenu antérieur."""
    models.initDb()
