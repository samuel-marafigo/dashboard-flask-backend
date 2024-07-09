from app import db

class Attendance(db.Model):
    __tablename__ = 'attendance'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    unit = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Float, nullable=False)

    def __init__(self, timestamp, unit, quantity):
        self.timestamp = timestamp
        self.unit = unit
        self.quantity = quantity