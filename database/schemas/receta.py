from typing import Optional
from pydantic import BaseModel


class RecetaBase(BaseModel):
    id_cita: int
    fecha: str
    instrucciones: Optional[str]

class RecetaCreate(RecetaBase):
    pass

class RecetaUpdate(RecetaBase):
    pass

class RecetaResponse(RecetaBase):
    id_receta: int

    class Config:
        from_attributes = True
