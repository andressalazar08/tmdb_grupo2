import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

detalles_pel=Blueprint("detallespel", __name__)

@detalles_pel.route("/detallespel/<int:resumen>")
def detallespel(resumen):
    url = f"https://api.themoviedb.org/3/movie/{resumen}?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    data=response.json()
    return render_template("detalle_pelicula.html",data=data)