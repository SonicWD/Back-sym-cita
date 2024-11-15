from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.models.all_models import Cita
from database.db_stup import get_db
from database.schemas.citas import CitaCreate, CitaResponse, CitaUpdate


router = APIRouter(
    tags=["citas"]
)


@router.post("/citas", response_model=CitaResponse)
def crear_cita(cita: CitaCreate, db: Session = Depends(get_db)):
    nueva_cita = Cita(**cita.dict())
    db.add(nueva_cita)
    db.commit()
    db.refresh(nueva_cita)
    return nueva_cita

@router.get("/citas", response_model=list[CitaResponse])
def listar_citas(db: Session = Depends(get_db)):
    return db.query(Cita).all()

@router.get("/citas/{id}", response_model=CitaResponse)
def obtener_cita(id: int, db: Session = Depends(get_db)):
    cita = db.query(Cita).get(id)
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita

@router.put("/citas/{id}", response_model=CitaResponse)
def actualizar_cita(id: int, datos: CitaUpdate, db: Session = Depends(get_db)):
    cita = db.query(Cita).get(id)
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(cita, key, value)
    db.commit()
    db.refresh(cita)
    return cita

@router.delete("/citas/{id}")
def eliminar_cita(id: int, db: Session = Depends(get_db)):
    cita = db.query(Cita).get(id)
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    db.delete(cita)
    db.commit()
    return {"detail": "Cita eliminada"}
