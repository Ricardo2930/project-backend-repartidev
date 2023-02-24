from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from os import getenv
from datetime import timedelta



app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["JWT_SECRET_KEY"] = getenv('SECRET_KEY') # sin el .env "super-secret"  #esta firma tiene que ser unica. Se ubica en una variable de entorno
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=7) #tiempo de expiracion de token, datetime libreria de python. 7días para su expiración
jwt = JWTManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    return "Iniciamos el Project Backend REPARTIDEV"

import routers.usuarios_router
import routers.servicios_router