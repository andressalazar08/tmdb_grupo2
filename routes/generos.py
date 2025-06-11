import os
import requests
from flask import Blueprint, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

generos_bp = Blueprint("generos", __name__)

@generos_bp.route("/generos")
def generos():
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    datos = response.json()["genres"]
    return render_template("generos.html", datos=datos)


@generos_bp.route("/peliculas_por_genero/<int:genero_id>")
def peliculas_por_genero(genero_id):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=es-ES&with_genres={genero_id}"
    response = requests.get(url)
    peliculas = response.json().get("results", [])
    return jsonify(peliculas)