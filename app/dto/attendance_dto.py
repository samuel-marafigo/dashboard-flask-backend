from typing import List, Optional
from pydantic import BaseModel
from datetime import date

class AttendanceDTO(BaseModel):
    dataInicio: date
    dataFinal: date
    municipes: bool
    unidades: List['Unit']
    retorno: Optional[List['Retorno']]

    class Unit(BaseModel):
        id: int

    class Retorno(BaseModel):
        titulo: str
        quantidade: float
