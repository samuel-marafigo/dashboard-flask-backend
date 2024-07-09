from flask import Blueprint, request, jsonify
from app.services.attendance_service import AttendanceService

attendance_bp = Blueprint('attendance', __name__)
attendance_service = AttendanceService()

@attendance_bp.route('/max_quantities_today', methods=['GET'])
def get_max_quantities_for_today():
    result = attendance_service.get_max_quantities_for_today()
    return jsonify(result), 200

@attendance_bp.route('/scrape', methods=['GET'])
def scrape_data():
    result = attendance_service.scrape_data_task()
    return jsonify(result), 200