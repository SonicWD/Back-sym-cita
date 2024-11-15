from pydantic import BaseModel


class HorarioBase(BaseModel):
    id_personal: int
    id_dia_semana: int
    hora_inicio: str
    hora_fin: str
    disponibilidad: bool

class HorarioCreate(HorarioBase):
    pass

class HorarioUpdate(HorarioBase):
    pass

class HorarioResponse(HorarioBase):
    id_horario: int

    class Config:
        from_attributes = True
