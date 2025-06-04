from flask import Flask
from routes.popular import popular_bp

app=Flask(__name__)

app.register_blueprint(popular_bp)

if __name__=="__main__":
    app.run(debug=True)