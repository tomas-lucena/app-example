from flask import Flask,render_template
import controller
import model
from flask_cors import CORS
import os


def create_app():
    CONFIG_ENVIROMENT = os.environ.get("CONFIG_ENVIROMENT")

    app = Flask(__name__)
    CORS(app)  

    print("CONFIG_ENVIROMENT ",CONFIG_ENVIROMENT)
    app.config.from_object(CONFIG_ENVIROMENT)

    model.init_model(app)
    controller.init_bp(app)


    
    
    return app



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True,port=9112)