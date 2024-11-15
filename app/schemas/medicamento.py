from typing import Optional
from pydantic import BaseModel


class MedicamentoBase(BaseModel):
    nombre: str
    descripcion: Optional[str]
    id_proveedor: Optional[int]
    precio: float

class MedicamentoCreate(MedicamentoBase):
    pass

class MedicamentoUpdate(MedicamentoBase):
    pass

class MedicamentoResponse(MedicamentoBase):
    id_medicamento: int

    class Config:
        from_attributes = True
