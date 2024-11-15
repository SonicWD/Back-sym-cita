from typing import Optional
from pydantic import BaseModel


class UsuarioBase(BaseModel):
    nombre_usuario: str
    contrasena: str
    id_rol: int

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(BaseModel):
    contrasena: Optional[str]

class UsuarioResponse(BaseModel):
    id_usuario: int
    nombre_usuario: str
    id_rol: int

    class Config:
        from_attributes = True
