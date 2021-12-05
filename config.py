"""
Paramètres de configuration.
Pour flask, mais pas uniquement.
"""
# Lancement de l'application flask : FLASK_APP=runRoApp.py flask run

# Construction du fichier de dépendances :
# pip freeze > requirements.txt

#import hashlib  ## Utile pour créer des hash (voir plus bas dans les mots de passes)
import os ## Utile pour manipuler les fichiers et les dossiers

## Un clé secrète est nécessaire pour générer le cookies de Django,
## utilisé par Flask
## On peut générer une clé ici : https://miniwebtool.com/django-secret-key-generator/
SECRET_KEY = "5)+1cn&p!9o@kj4qao0c+w@&k4ar&yvn(k!+0a8+2b-&^h^+fq"

### Config DB
#SQLALCHEMY_DATABASE_URI = 'postgresql://'+DB_USER+':'+DB_PASS+'@localhost:5432/'+DB_NAME
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'roApp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Config de l'application elle-même

MY_URL = "https://poc-ringover.jamespot.com"