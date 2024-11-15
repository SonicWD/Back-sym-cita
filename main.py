from fastapi import FastAPI
import uvicorn
from app.routers import auth
from app.database.connection import engine, Base    
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

app.include_router(auth.router, prefix="/auth", tags=["authentication"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)