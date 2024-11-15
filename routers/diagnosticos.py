from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.models.all_models import Diagnostico
from database.db_stup import get_db
from database.schemas.diagnostico import DiagnosticoCreate, DiagnosticoResponse, DiagnosticoUpdate


router = APIRouter(
    tags="diagnostico"
)


@router.post("/diagnosticos", response_model=DiagnosticoResponse)
def crear_diagnostico(diagnostico: DiagnosticoCreate, db: Session = Depends(get_db)):
    nuevo_diagnostico = Diagnostico(**diagnostico.dict())
    db.add(nuevo_diagnostico)
    db.commit()
    db.refresh(nuevo_diagnostico)
    return nuevo_diagnostico

@router.get("/diagnosticos", response_model=list[DiagnosticoResponse])
def listar_diagnosticos(db: Session = Depends(get_db)):
    return db.query(Diagnostico).all()

@router.get("/diagnosticos/{id}", response_model=DiagnosticoResponse)
def obtener_diagnostico(id: int, db: Session = Depends(get_db)):
    diagnostico = db.query(Diagnostico).get(id)
    if not diagnostico:
        raise HTTPException(status_code=404, detail="Diagnóstico no encontrado")
    return diagnostico

@router.put("/diagnosticos/{id}", response_model=DiagnosticoResponse)
def actualizar_diagnostico(id: int, datos: DiagnosticoUpdate, db: Session = Depends(get_db)):
    diagnostico = db.query(Diagnostico).get(id)
    if not diagnostico:
        raise HTTPException(status_code=404, detail="Diagnóstico no encontrado")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(diagnostico, key, value)
    db.commit()
    db.refresh(diagnostico)
    return diagnostico

@router.delete("/diagnosticos/{id}")
def eliminar_diagnostico(id: int, db: Session = Depends(get_db)):
    diagnostico = db.query(Diagnostico).get(id)
    if not diagnostico:
        raise HTTPException(status_code=404, detail="Diagnóstico no encontrado")
    db.delete(diagnostico)
    db.commit()
    return {"detail": "Diagnóstico eliminado"}
