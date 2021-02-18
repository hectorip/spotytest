from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Spotify Analytics"


@app.route("/welcome_user")
def welcome_auth_user():
    return "Auth redirect users"


@app.route("/about")
def about():
    return "Servicio para que puedas consultar tus estadísticas de la música que escuchas"
