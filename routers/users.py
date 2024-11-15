from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.models.all_models import Rol, Usuario
from database.db_stup import get_db


router = APIRouter(
    tags=["users"]
)


@router.post("/usuarios")
def crear_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

@router.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

@router.get("/usuarios/{id}")
def obtener_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).get(id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/usuarios/{id}")
def actualizar_usuario(id: int, datos: Usuario, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).get(id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(usuario, key, value)
    db.commit()
    db.refresh(usuario)
    return usuario

@router.delete("/usuarios/{id}")
def eliminar_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).get(id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario)
    db.commit()
    return {"detail": "Usuario eliminado"}

@router.get("/roles")
def listar_roles(db: Session = Depends(get_db)):
    return db.query(Rol).all()
