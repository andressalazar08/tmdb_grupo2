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
    #buscar=request.form.get("buscar")
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query=stich&language=es-ES"
    response = requests.get(url)
    datos = response.json()["results"]
    return render_template("buscar_nombre.html", datos=datos)
