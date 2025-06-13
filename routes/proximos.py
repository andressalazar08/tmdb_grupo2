import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

proximos_bp = Blueprint("proximos", __name__)

@proximos_bp.route("/proximos")
def proximos():
    url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={API_KEY}&language=es-ES&page=1"
    response = requests.get(url)
    datos = response.json()["results"]
    return render_template("proximos.html", datos=datos)

