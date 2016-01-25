from app import db
from flask.ext.login import UserMixin

class TimeSheet(db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    date = db.Column(db.String(16),index=True,nullable=False)
    start = db.Column(db.String(16)) 
    end = db.Column(db.String(16))
    total = db.Column(db.Float(60))
