from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.models.all_models import InventarioMedicamentos, Medicamento
from database.db_stup import get_db
from database.schemas.int_medicamento import InventarioCreate, InventarioResponse
from database.schemas.medicamento import MedicamentoCreate, MedicamentoResponse, MedicamentoUpdate


router = APIRouter(
    tags=["medicamentos_inventarios"]
)



@router.post("/medicamentos", response_model=MedicamentoResponse)
def crear_medicamento(medicamento: MedicamentoCreate, db: Session = Depends(get_db)):
    nuevo_medicamento = Medicamento(**medicamento.dict())
    db.add(nuevo_medicamento)
    db.commit()
    db.refresh(nuevo_medicamento)
    return nuevo_medicamento

@router.get("/medicamentos", response_model=list[MedicamentoResponse])
def listar_medicamentos(db: Session = Depends(get_db)):
    return db.query(Medicamento).all()

@router.get("/medicamentos/{id}", response_model=MedicamentoResponse)
def obtener_medicamento(id: int, db: Session = Depends(get_db)):
    medicamento = db.query(Medicamento).get(id)
    if not medicamento:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    return medicamento

@router.put("/medicamentos/{id}", response_model=MedicamentoResponse)
def actualizar_medicamento(id: int, datos: MedicamentoUpdate, db: Session = Depends(get_db)):
    medicamento = db.query(Medicamento).get(id)
    if not medicamento:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(medicamento, key, value)
    db.commit()
    db.refresh(medicamento)
    return medicamento

@router.delete("/medicamentos/{id}")
def eliminar_medicamento(id: int, db: Session = Depends(get_db)):
    medicamento = db.query(Medicamento).get(id)
    if not medicamento:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    db.delete(medicamento)
    db.commit()
    return {"detail": "Medicamento eliminado"}


@router.post("/inventario", response_model=InventarioResponse)
def crear_inventario(inventario: InventarioCreate, db: Session = Depends(get_db)):
    nuevo_inventario = InventarioMedicamentos(**inventario.dict())
    db.add(nuevo_inventario)
    db.commit()
    db.refresh(nuevo_inventario)
    return nuevo_inventario

@router.get("/inventario", response_model=list[InventarioResponse])
def listar_inventario(db: Session = Depends(get_db)):
    return db.query(InventarioMedicamentos).all()
