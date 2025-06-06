import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

mejor_valoradas_bp = Blueprint("mejor_valoradas", __name__)

@mejor_valoradas_bp.route("/mejor_valoradas")
def mejor_valoradas():
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=es-ES&page=1"
    response = requests.get(url)
    datos = response.json()["results"]
    return render_template("mejor_valoradas.html", datos=datos)
