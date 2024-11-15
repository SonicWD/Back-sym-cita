from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.models.all_models import Receta
from database.db_stup import get_db
from database.schemas.receta import RecetaCreate, RecetaResponse, RecetaUpdate


router = APIRouter(
    tags=["recetas"]
)

@router.post("/recetas", response_model=RecetaResponse)
def crear_receta(receta: RecetaCreate, db: Session = Depends(get_db)):
    nueva_receta = Receta(**receta.dict())
    db.add(nueva_receta)
    db.commit()
    db.refresh(nueva_receta)
    return nueva_receta

@router.get("/recetas", response_model=list[RecetaResponse])
def listar_recetas(db: Session = Depends(get_db)):
    return db.query(Receta).all()

@router.get("/recetas/{id}", response_model=RecetaResponse)
def obtener_receta(id: int, db: Session = Depends(get_db)):
    receta = db.query(Receta).get(id)
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    return receta

@router.put("/recetas/{id}", response_model=RecetaResponse)
def actualizar_receta(id: int, datos: RecetaUpdate, db: Session = Depends(get_db)):
    receta = db.query(Receta).get(id)
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(receta, key, value)
    db.commit()
    db.refresh(receta)
    return receta

@router.delete("/recetas/{id}")
def eliminar_receta(id: int, db: Session = Depends(get_db)):
    receta = db.query(Receta).get(id)
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    db.delete(receta)
    db.commit()
    return {"detail": "Receta eliminada"}
