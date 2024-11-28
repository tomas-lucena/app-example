
from model.application import Application
from flask import request,jsonify,render_template
from datetime import datetime
from model import db
from flask import Blueprint


application_bp = Blueprint('application',__name__)

# Routes
@application_bp.route("/", methods=["GET", "POST"])
def submit_application():
    try:
        applications = Application.query.all()
    
    except Exception as e:
        print(f"Error: {e}")
        applications = []

    if request.method == "GET":
        return render_template("index.html",applications=applications) 

    try:
        data = request.form
        application = Application(
            name=data.get('name',''),
            email=data.get('email'),
            phone=data.get('phone', ''),
            role=data.get('role'),
            experience=data.get('experience'),
            location=data.get('location'),
        )
        db.session.add(application)
        db.session.commit()
        applications+=[application]
        return render_template("index.html",applications=applications) 
        # return jsonify({"message": "Application submitted successfully!"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return render_template("index.html",applications=applications) 
        # return jsonify({"error": "An error occurred while submitting the application."}), 500
