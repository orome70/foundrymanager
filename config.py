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

## A présent, on met les éléments de configuration pour utiliser les api :
## Ringover d'une part et Jamespot d'autre part

# Éléments de sécu Jamespot (midgard)
J_APP = "EXT-krisapp"
J_KEY = "theMeg4keYForM3"
J_HEADERS = {
    'X-Com-Jamespot-Module-Name': J_APP,
    'X-Com-Jamespot-Module-Key' : J_KEY
}
J_HOST = "https://midgard.orome.org/api/server/2.0/"

# Éléments de sécu ringover
# A terme ce sera configuré dans l'application.
RO_KEY = "c25ccde7acbccc69833907345b810b184b169f70"
RO_HEADER = {
    'Authorization': RO_KEY
}
RO_HOST = "https://public-api.ringover.com/v2/"


# Basedir est juste utiliser pour définir l'url de la base sqlight.
# Comme je vais utiliser directement postgresql, on s'en fiche.
#basedir = os.path.abspath(os.path.dirname(__file__))
DB_NAME = 'ro_data'
DB_USER = 'ro_user'
DB_CLEAR_PASS = '377pgP4za'
DB_PASS = DB_CLEAR_PASS
#'md5' + hashlib.md5((DB_USER + DB_CLEAR_PASS).encode()).hexdigest()

### Config DB
#SQLALCHEMY_DATABASE_URI = 'postgresql://'+DB_USER+':'+DB_PASS+'@localhost:5432/'+DB_NAME
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'roApp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Config de l'application elle-même

MY_URL = "https://poc-ringover.jamespot.com"