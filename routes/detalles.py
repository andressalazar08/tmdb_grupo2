import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")

detalles_bp=Blueprint("Detalles", __name__)

@detalles_bp.route("/detalles/<int:id_pelicula>")
def detalles(id_pelicula):
    url = f"https://api.themoviedb.org/3/movie/{id_pelicula}?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)


    if response.status_code == 200:
        datos_pelicula = response.json()
        return render_template("detalles.html", pelicula=datos_pelicula)
    else:
        return render_template("error.html", mensaje="No se pudo obtener los detalles de la película.")

