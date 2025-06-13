import os
import requests
from flask import Blueprint, render_template, request
from dotenv import load_dotenv  

load_dotenv()
API_KEY = os.getenv("API_KEY")

proximos_bp = Blueprint("proximos", __name__)

@proximos_bp.route("/proximos")
def proximos():
    seleccion=request.args.get("Ordenar")
    print(seleccion)
    url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={API_KEY}&language=es-ES&page=1"
    response = requests.get(url)
    datos = response.json()["results"]
    if seleccion=="popularity":
        datos.sort(key=lambda x: x.get("popularity"))
    elif seleccion=="genre_ids":
         datos.sort(key=lambda x: x.get("genre_ids"))
    elif seleccion =="title":
         datos.sort(key=lambda x: x.get("title"))
    elif seleccion =="vote_average":
         datos.sort(key=lambda x: x.get("vote_average"))
    return render_template("proximos.html", datos=datos)

