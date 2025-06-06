import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")

detalles_bp=Blueprint("Detalles", __name__)

@detalles_bp.route("/detalles")
def detalles():
    url = f"https://api.themoviedb.org/3/movie/550?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    genero = id
