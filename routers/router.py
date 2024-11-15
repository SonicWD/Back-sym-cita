from fastapi import APIRouter
from routers.citas import router as c_router
from routers.diagnosticos import router as d_router
from routers.examenes import router as e_router
from routers.horarios import router as h_router
from routers.medinventarios import router as inv_router
from routers.pacientes import router as pc_router
from routers.personal import router as per_router
from routers.recetas import router as re_router
from routers.tratamientos import router as tr_router
from routers.recetas import router as us_router


router = APIRouter(
    prefix="/api_citas"
)


router.include_router(c_router)
router.include_router(d_router)
router.include_router(e_router)
router.include_router(h_router)
router.include_router(inv_router)
router.include_router(pc_router)
router.include_router(per_router)
router.include_router(re_router)
router.include_router(tr_router)
router.include_router(us_router)