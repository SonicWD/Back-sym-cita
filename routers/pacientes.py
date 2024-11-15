from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.models.all_models import Paciente
from database.db_stup import get_db
from database.schemas.paciente import PacienteCreate, PacienteResponse, PacienteUpdate


router = APIRouter(
    tags=["pacientes"]
)

@router.post("/pacientes", response_model=PacienteResponse)
def crear_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):
    nuevo_paciente = Paciente(**paciente.dict())
    db.add(nuevo_paciente)
    db.commit()
    db.refresh(nuevo_paciente)
    return nuevo_paciente

@router.get("/pacientes", response_model=list[PacienteResponse])
def listar_pacientes(db: Session = Depends(get_db)):
    return db.query(Paciente).all()

@router.get("/pacientes/{id}", response_model=PacienteResponse)
def obtener_paciente(id: int, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).get(id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

@router.put("/pacientes/{id}", response_model=PacienteResponse)
def actualizar_paciente(id: int, datos: PacienteUpdate, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).get(id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(paciente, key, value)
    db.commit()
    db.refresh(paciente)
    return paciente

@router.delete("/pacientes/{id}")
def eliminar_paciente(id: int, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).get(id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    db.delete(paciente)
    db.commit()
    return {"detail": "Paciente eliminado"}
