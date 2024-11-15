from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.models.all_models import Personal
from database.db_stup import get_db
from database.schemas.personal import PersonalCreate, PersonalResponse, PersonalUpdate


router = APIRouter(
    tags=["personal"]
)

@router.post("/personal", response_model=PersonalResponse)
def crear_personal(personal: PersonalCreate, db: Session = Depends(get_db)):
    nuevo_personal = Personal(**personal.dict())
    db.add(nuevo_personal)
    db.commit()
    db.refresh(nuevo_personal)
    return nuevo_personal

@router.get("/personal", response_model=list[PersonalResponse])
def listar_personal(db: Session = Depends(get_db)):
    return db.query(Personal).all()

@router.get("/personal/{id}", response_model=PersonalResponse)
def obtener_personal(id: int, db: Session = Depends(get_db)):
    personal = db.query(Personal).get(id)
    if not personal:
        raise HTTPException(status_code=404, detail="Personal no encontrado")
    return personal

@router.put("/personal/{id}", response_model=PersonalResponse)
def actualizar_personal(id: int, datos: PersonalUpdate, db: Session = Depends(get_db)):
    personal = db.query(Personal).get(id)
    if not personal:
        raise HTTPException(status_code=404, detail="Personal no encontrado")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(personal, key, value)
    db.commit()
    db.refresh(personal)
    return personal

@router.delete("/personal/{id}")
def eliminar_personal(id: int, db: Session = Depends(get_db)):
    personal = db.query(Personal).get(id)
    if not personal:
        raise HTTPException(status_code=404, detail="Personal no encontrado")
    db.delete(personal)
    db.commit()
    return {"detail": "Personal eliminado"}
