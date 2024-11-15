from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date

class PacienteBase(BaseModel):
    id_tipo_documento: Optional[int]
    numero_documento: str
    nombre: str
    apellido: str
    fecha_nacimiento: date
    id_genero: Optional[int]
    direccion_de_residencia: Optional[str]
    ocupacion: Optional[str]
    edad: Optional[int]
    telefono: Optional[str]
    email: Optional[EmailStr]
    eps: Optional[str]

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(PacienteBase):
    pass

class PacienteResponse(PacienteBase):
    id_paciente: int

    class Config:
        from_attributes = True
