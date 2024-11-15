from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.models.all_models import Horario, Rol, Usuario
from database.db_stup import get_db
from database.schemas.horario import HorarioCreate, HorarioResponse, HorarioUpdate


router = APIRouter(
    tags=["horarios"]
)


@router.post("/horarios", response_model=HorarioResponse)
def crear_horario(horario: HorarioCreate, db: Session = Depends(get_db)):
    nuevo_horario = Horario(**horario.dict())
    db.add(nuevo_horario)
    db.commit()
    db.refresh(nuevo_horario)
    return nuevo_horario

@router.get("/horarios", response_model=list[HorarioResponse])
def listar_horarios(db: Session = Depends(get_db)):
    return db.query(Horario).all()

@router.get("/horarios/{id}", response_model=HorarioResponse)
def obtener_horario(id: int, db: Session = Depends(get_db)):
    horario = db.query(Horario).get(id)
    if not horario:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return horario

@router.put("/horarios/{id}", response_model=HorarioResponse)
def actualizar_horario(id: int, datos: HorarioUpdate, db: Session = Depends(get_db)):
    horario = db.query(Horario).get(id)
    if not horario:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(horario, key, value)
    db.commit()
    db.refresh(horario)
    return horario

@router.delete("/horarios/{id}")
def eliminar_horario(id: int, db: Session = Depends(get_db)):
    horario = db.query(Horario).get(id)
    if not horario:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    db.delete(horario)
    db.commit()
    return {"detail": "Horario eliminado"}
