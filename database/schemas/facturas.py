from typing import Optional
from pydantic import BaseModel


class FacturaBase(BaseModel):
    id_cita: int
    monto_total: float
    fecha: str
    id_metodo_pago: int
    id_estado_factura: int

class FacturaCreate(FacturaBase):
    pass

class FacturaUpdate(BaseModel):
    id_metodo_pago: Optional[int]
    id_estado_factura: Optional[int]

class FacturaResponse(FacturaBase):
    id_factura: int

    class Config:
        from_attributes = True
