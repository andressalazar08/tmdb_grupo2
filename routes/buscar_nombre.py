#ruta de carolina
import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

busqueda_bp = Blueprint("busqueda", __name__)

@busqueda_bp.route("/busqueda")
def busqueda():
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query=batman&language=es-ES"
    response = requests.get(url)
    datos = response.json()["results"]
    return render_template("busqueda.html", datos=datos)
