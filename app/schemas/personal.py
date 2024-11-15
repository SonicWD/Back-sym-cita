from typing import Optional
from pydantic import BaseModel, EmailStr


class PersonalBase(BaseModel):
    id_cargo: Optional[int]
    id_tipo_documento: Optional[int]
    numero_documento: str
    nombre: Optional[str]
    apellido: Optional[str]
    telefono: Optional[str]
    email: Optional[EmailStr]

class PersonalCreate(PersonalBase):
    pass

class PersonalUpdate(PersonalBase):
    pass

class PersonalResponse(PersonalBase):
    id_personal: int

    class Config:
        from_attributes = True
