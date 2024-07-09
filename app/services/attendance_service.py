import json
import requests
from datetime import datetime
from pytz import timezone
from app.repositories.attendance_repository import AttendanceRepository
from app.dto.recent_attendance_dto import RecentAttendanceDTO
import os
from app.dto.attendance_dto import AttendanceDTO
from app.models.attendance import Attendance
from app import celery

json_path = './data/healthUnits.json'


class AttendanceService:
    def __init__(self):
        self.attendance_repository = AttendanceRepository()
        self.health_units = self.load_health_units()

    def load_health_units(self):
        with open(json_path) as f:
            return json.load(f)

    def get_max_quantities_for_today(self):
        sao_paulo_tz = timezone('America/Sao_Paulo')
        now = datetime.now(sao_paulo_tz)
        start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_day = now

        results = self.attendance_repository.find_max_quantities_for_today(start_of_day, end_of_day)
        recent_attendances = [
            RecentAttendanceDTO(id=result[0], quantity=result[1]).dict()
        for result in results]
        return recent_attendances


    def scrape_data_task(self):
        api_url = "https://saudetransparente2.sjp.pr.gov.br/saudetransparenteapi/saude-transparente/atendimento-farmaceuticos/buscar-dados-farmaceuticos"
        health_units_json_path = "data/healthUnits.json"

        with open(health_units_json_path, 'r') as file:
            health_units = json.load(file)

        sao_paulo_tz = timezone('America/Sao_Paulo')
        now = datetime.now(sao_paulo_tz)

        attendance_repository = AttendanceRepository()

        for unit in health_units:
            unit_id = unit['id']
            unit_name = unit['name']
            payload = {
                "dataInicio": now.strftime('%Y-%m-%d'),
                "dataFinal": now.strftime('%Y-%m-%d'),
                "municipes": False,
                "unidades": [{"id": unit_id}],
                "retorno": None
            }
            response = requests.post(api_url, json=payload)
            response_data = response.json()

            if response_data and response_data['retorno']:
                quantidade = next(
                    (item['quantidade'] for item in response_data['retorno']
                     if item['titulo'] == "Usuários atendidos no período informado"), 0.0)

                attendance = Attendance(now, unit_name, quantidade)
                attendance_repository.save(attendance)