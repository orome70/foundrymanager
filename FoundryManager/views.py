from flask import Flask, render_template, request

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, type app.config['MY_VARIABLE']

# Here we may add some initialization

# This is a basic class to put all the data needed to transfer anything to a page template.

class PageData:
    def __init__(self, title, description,params={}):
        self.title = title
        self.description = description
        self.params = params


@app.route('/index/')
@app.route('/index.html/')
@app.route('/index.php/')
@app.route('/')
def index():
    """
    Page d'accueil du site : profil de christophe
    """
    pageData = PageData("Page d'index", "Pour le moment il n'y a rien d'intéressant", {})
    return render_template('index.html', pageData=pageData)
    
@app.route('/profile/<email>/')
def profile(email=None):
    """
    Page de profile
    """
    params = {}
    params['user'] = email
    # Here we chould get user data from email
    pageData = PageData("Profil " + email, "C'est la page de profil de l'utilisateur" + email, params)
    return render_template('profile.html', pageData=pageData)

if __name__ == "__main__":
    app.run(debug=True)
    #app.run()
