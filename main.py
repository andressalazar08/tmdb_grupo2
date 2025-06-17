from flask import Flask
from routes.popular import popular_bp
#from routes.mejor_valoradas import mejor_valoradas_bp
#from routes.buscar_nombre import busqueda_bp
from routes.detalles import detalles_bp
#from routes.proximos import proximos_bp
from routes.generos import generos_bp

app=Flask(__name__)

app.register_blueprint(popular_bp)
#app.register_blueprint(mejor_valoradas_bp)
#app.register_blueprint(busqueda_bp)
app.register_blueprint(detalles_bp)
#app.register_blueprint(proximos_bp)
app.register_blueprint(generos_bp)

if __name__=="__main__":
    app.run(debug=True)