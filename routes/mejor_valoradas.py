import os
import requests
from flask import Blueprint, render_template, request
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

mejor_valoradas_bp = Blueprint("mejor_valoradas", __name__)

@mejor_valoradas_bp.route("/mejor_valoradas")
def mejor_valoradas():
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=es-ES&page=1"
    response = requests.get(url)
    datos = response.json()["results"]

     # Leer filtros desde la URL
    buscar = request.args.get("buscar", "").lower()
    ordenar = request.args.get("ordenar", "titulo")

    # Filtro
    if buscar:
        datos = [p for p in datos if buscar in p["title"].lower()]

    # Ordenamiento
    if ordenar == "titulo":
        datos.sort(key=lambda x: x["title"])
    elif ordenar == "año":
        datos.sort(key=lambda x: x.get("release_date", "")[:4])
    elif ordenar == "rating":
        datos.sort(key=lambda x: x.get("vote_average", 0), reverse=True)

    return render_template("mejor_valoradas.html", datos=datos)
