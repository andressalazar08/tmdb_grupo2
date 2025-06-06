import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv() #Librería de python para trabajar con variables de entorno
API_KEY = os.getenv("API_KEY") #Declaro la variable de entorno que viene del .env

popular_bp = Blueprint("popular", __name__) #Modularizar las rutas

@popular_bp.route("/popular")
def popular():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    datos = response.json()["results"]
    return render_template("popular.html", datos=datos)
