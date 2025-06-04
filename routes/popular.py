import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

popular_bp = Blueprint("popular", __name__)

@popular_bp.route("/popular")
def popular():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    datos = response.json()["results"]
    return render_template("popular.html", datos=datos)
