from pydantic import BaseModel


class CitaBase(BaseModel):
    id_paciente: int
    id_personal: int
    fecha: str
    hora: str
    id_tipo_cita: int
    id_estado: int

class CitaCreate(CitaBase):
    pass

class CitaUpdate(CitaBase):
    pass

class CitaResponse(CitaBase):
    id_cita: int

    class Config:
        from_attributes = True
