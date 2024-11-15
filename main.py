from fastapi import FastAPI
import uvicorn
from routers.router import router as main_router
from database.db_stup import engine, Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(main_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)