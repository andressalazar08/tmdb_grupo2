import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

generos_bp = Blueprint("generos", __name__)

@generos_bp.route("/generos")
def generos():
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    datos = response.json()["results"]
    return render_template("generos.html", datos=datos)
