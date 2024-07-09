from app.models.attendance import Attendance
from app.__init__ import db

class AttendanceRepository:
    def find_max_quantities_for_today(self, start_of_day, end_of_day):
        results = db.session.query(
            Attendance.id, db.func.max(Attendance.quantity)
        ).filter(
            Attendance.timestamp.between(start_of_day, end_of_day)
        ).group_by(Attendance.id).all()
        return results

    def save(self, attendance):
        db.session.add(attendance)
        db.session.commit()
