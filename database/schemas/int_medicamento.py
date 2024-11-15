from pydantic import BaseModel


class InventarioBase(BaseModel):
    nombre_medicamento: str
    cantidad: int
    fecha_caducidad: str
    id_proveedor: int

class InventarioCreate(InventarioBase):
    pass

class InventarioResponse(InventarioBase):
    id_inventario: int

    class Config:
        from_attributes = True
