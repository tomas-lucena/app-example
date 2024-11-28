from flask import Blueprint

bp = Blueprint("restapi", __name__,)# url_prefix="/api/v1")

def init_bp(app):  
    from .health_bp import health_bp
    from .application_bp import application_bp

    bp.register_blueprint(health_bp)
    bp.register_blueprint(application_bp)

    app.register_blueprint(bp)

