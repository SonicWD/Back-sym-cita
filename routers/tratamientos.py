from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.models.all_models import Tratamiento
from database.db_stup import get_db
from database.schemas.tratamiento import TratamientoCreate, TratamientoResponse, TratamientoUpdate


router = APIRouter(
    tags=["tratamiento"]
)

@router.post("/tratamientos", response_model=TratamientoResponse)
def crear_tratamiento(tratamiento: TratamientoCreate, db: Session = Depends(get_db)):
    nuevo_tratamiento = Tratamiento(**tratamiento.dict())
    db.add(nuevo_tratamiento)
    db.commit()
    db.refresh(nuevo_tratamiento)
    return nuevo_tratamiento

@router.get("/tratamientos", response_model=list[TratamientoResponse])
def listar_tratamientos(db: Session = Depends(get_db)):
    return db.query(Tratamiento).all()

@router.get("/tratamientos/{id}", response_model=TratamientoResponse)
def obtener_tratamiento(id: int, db: Session = Depends(get_db)):
    tratamiento = db.query(Tratamiento).get(id)
    if not tratamiento:
        raise HTTPException(status_code=404, detail="Tratamiento no encontrado")
    return tratamiento

@router.put("/tratamientos/{id}", response_model=TratamientoResponse)
def actualizar_tratamiento(id: int, datos: TratamientoUpdate, db: Session = Depends(get_db)):
    tratamiento = db.query(Tratamiento).get(id)
    if not tratamiento:
        raise HTTPException(status_code=404, detail="Tratamiento no encontrado")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(tratamiento, key, value)
    db.commit()
    db.refresh(tratamiento)
    return tratamiento

@router.delete("/tratamientos/{id}")
def eliminar_tratamiento(id: int, db: Session = Depends(get_db)):
    tratamiento = db.query(Tratamiento).get(id)
    if not tratamiento:
        raise HTTPException(status_code=404, detail="Tratamiento no encontrado")
    db.delete(tratamiento)
    db.commit()
    return {"detail": "Tratamiento eliminado"}
