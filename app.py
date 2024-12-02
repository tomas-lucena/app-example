from flask import Flask,render_template
import controller
import model
from flask_cors import CORS
from flask_migrate import Migrate
import os

migrate = Migrate()

def create_app():
    CONFIG_ENVIRONMENT = os.environ.get("CONFIG_ENVIRONMENT")

    app = Flask(__name__)
    CORS(app)  

    app.config.from_object(CONFIG_ENVIRONMENT)

    model.init_model(app)
    migrate.init_app(app)  
    controller.init_bp(app)
    
    return app



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True,port=9112)