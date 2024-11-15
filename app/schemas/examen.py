from typing import Optional
from pydantic import BaseModel


class ExamenBase(BaseModel):
    id_cita: int
    tipo: Optional[str]
    resultados: Optional[str]
    fecha: str
    observaciones: Optional[str]
    precio: float

class ExamenCreate(ExamenBase):
    pass

class ExamenUpdate(ExamenBase):
    pass

class ExamenResponse(ExamenBase):
    id_examen: int

    class Config:
        from_attributes = True
