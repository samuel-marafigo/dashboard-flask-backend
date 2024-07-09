from pydantic import BaseModel

class RecentAttendanceDTO(BaseModel):
    id: int
    quantity: float
