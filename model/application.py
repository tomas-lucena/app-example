from sqlalchemy import Date,Column,Float,DateTime,String,Text,Numeric,Integer
from sqlalchemy.ext.declarative import declarative_base
from model import db
from datetime import datetime

class Application(db.Model):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=True)
    role = Column(String(50), nullable=False)
    experience = Column(Integer, nullable=False)
    location = Column(String(50), nullable=False)
    submission_date = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "role": self.role,
            "experience": self.experience,
            "location": self.location,
            "submission_date": self.submission_date.strftime('%Y-%m-%d %H:%M:%S')
        }

