from flask import Flask
from flask_cors import CORS



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ESP32'
    
    CORS(app)

    
    from .views import views 
   

    app.register_blueprint(views, url_prefix="/")

    return app




