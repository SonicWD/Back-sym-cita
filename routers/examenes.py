from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.models.all_models import Examen
from database.db_stup import get_db
from database.schemas.examen import ExamenCreate, ExamenResponse, ExamenUpdate


router = APIRouter(
    tags=["examenes"]
)

@router.post("/examenes", response_model=ExamenResponse)
def crear_examen(examen: ExamenCreate, db: Session = Depends(get_db)):
    nuevo_examen = Examen(**examen.dict())
    db.add(nuevo_examen)
    db.commit()
    db.refresh(nuevo_examen)
    return nuevo_examen

@router.get("/examenes", response_model=list[ExamenResponse])
def listar_examenes(db: Session = Depends(get_db)):
    return db.query(Examen).all()

@router.get("/examenes/{id}", response_model=ExamenResponse)
def obtener_examen(id: int, db: Session = Depends(get_db)):
    examen = db.query(Examen).get(id)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")
    return examen

@router.put("/examenes/{id}", response_model=ExamenResponse)
def actualizar_examen(id: int, datos: ExamenUpdate, db: Session = Depends(get_db)):
    examen = db.query(Examen).get(id)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(examen, key, value)
    db.commit()
    db.refresh(examen)
    return examen

@router.delete("/examenes/{id}")
def eliminar_examen(id: int, db: Session = Depends(get_db)):
    examen = db.query(Examen).get(id)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")
    db.delete(examen)
    db.commit()
    return {"detail": "Examen eliminado"}
