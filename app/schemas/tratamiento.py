from typing import Optional
from pydantic import BaseModel


class TratamientoBase(BaseModel):
    id_diagnostico: int
    lista_medicamentos: Optional[str]
    dosis: Optional[str]
    frecuencia: Optional[str]
    duracion: Optional[str]
    precio: float

class TratamientoCreate(TratamientoBase):
    pass

class TratamientoUpdate(TratamientoBase):
    pass

class TratamientoResponse(TratamientoBase):
    id_tratamiento: int

    class Config:
        from_attributes = True
