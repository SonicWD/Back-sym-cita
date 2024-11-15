from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.db_stup import get_db
from database.models.all_models import Factura
from database.schemas.facturas import FacturaCreate, FacturaResponse, FacturaUpdate


router = APIRouter(
    tags=["facturas"]
)



@router.post("/facturas", response_model=FacturaResponse)
def crear_factura(factura: FacturaCreate, db: Session = Depends(get_db)):
    nueva_factura = Factura(**factura.dict())
    db.add(nueva_factura)
    db.commit()
    db.refresh(nueva_factura)
    return nueva_factura

@router.get("/facturas", response_model=list[FacturaResponse])
def listar_facturas(db: Session = Depends(get_db)):
    return db.query(Factura).all()

@router.get("/facturas/{id}", response_model=FacturaResponse)
def obtener_factura(id: int, db: Session = Depends(get_db)):
    factura = db.query(Factura).get(id)
    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return factura

@router.put("/facturas/{id}", response_model=FacturaResponse)
def actualizar_factura(id: int, datos: FacturaUpdate, db: Session = Depends(get_db)):
    factura = db.query(Factura).get(id)
    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(factura, key, value)
    db.commit()
    db.refresh(factura)
    return factura

@router.delete("/facturas/{id}")
def eliminar_factura(id: int, db: Session = Depends(get_db)):
    factura = db.query(Factura).get(id)
    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    db.delete(factura)
    db.commit()
    return {"detail": "Factura eliminada"}
