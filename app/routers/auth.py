from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from app.database.connection import get_db
from app.schemas import UserCreate, User as UserSchema, Token
from app.security import (
    authenticate_user,
    create_access_token,
    get_current_active_user,
    create_user,
    update_user,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=UserSchema)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user

@router.get("/me", response_model=UserSchema)
async def read_users_me(current_user: UserSchema = Depends(get_current_active_user)):
    return current_user

@router.put("/me", response_model=UserSchema)
async def update_user_me(
    user_update: UserCreate,
    current_user: UserSchema = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    updated_user = update_user(db, current_user.user_id, user_update)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.post("/logout")
async def logout(current_user: UserSchema = Depends(get_current_active_user)):
    # En un sistema de autenticación basado en JWT, el logout se maneja típicamente en el cliente
    # El servidor no necesita realizar ninguna acción específica
    return {"message": "Logout successful"}