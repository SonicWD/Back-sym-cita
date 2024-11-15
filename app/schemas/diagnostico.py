from typing import Optional
from pydantic import BaseModel


class DiagnosticoBase(BaseModel):
    id_cita: int
    descripcion: Optional[str]
    observaciones: Optional[str]
    recomendaciones: Optional[str]

class DiagnosticoCreate(DiagnosticoBase):
    pass

class DiagnosticoUpdate(DiagnosticoBase):
    pass

class DiagnosticoResponse(DiagnosticoBase):
    id_diagnostico: int

    class Config:
        from_attributes = True
