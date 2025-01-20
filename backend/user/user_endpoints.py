#user_endpoints.py


from fastapi import APIRouter, HTTPException, status
from auth.hashing import *
from core.config import settings
from schemas.user_schema import *
from fastapi.responses import JSONResponse
from data.db_methods import *


router = APIRouter()


@router.post("/create_user")
async def create_user(user: UserRegistration):
    user_exist = settings.USERS_DB.get(user.username)

    if user_exist:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Username already registered.")
    
    hashed_password = Hasher.hash_passw(user.password)
    user_in_db = UserInDB(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password
    )
    settings.USERS_DB.update({user.username: user_in_db.dict()})
    save_users_db()

    return JSONResponse(content={"message": "User created and stored in database",
                           "status": "ok"}, status_code=200)


@router.delete("/delete_user")
async def delete_user(user: str):
    user_exist = settings.USERS_DB.get(user)

    if not user_exist:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Username not in database.")
    
    del settings.USERS_DB[user]

    return JSONResponse(content={"message": "User deleted from database.",
                           "status": "ok"}, status_code=200)
