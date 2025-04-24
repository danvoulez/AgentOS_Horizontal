
from fastapi import APIRouter, HTTPException, Depends, status, Header
from agentos_pessoas.models.user_model import User
from agentos_pessoas.services.user_service import create_user, get_user
import uuid

router = APIRouter(prefix="/users", tags=["users"])

FAKE_TOKENS = {}

def get_current_user(authorization: str = Header(...)):
    token = authorization.removeprefix("Bearer ")
    email = FAKE_TOKENS.get(token)
    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return get_user(email)

@router.post("/")
def register(u: User):
    user = create_user(u)
    return {"id": user.id}

@router.post("/login")
def login(credentials: dict):
    email = credentials.get("email")
    user = get_user(email)
    if not user or user.password!=credentials.get("password"):
        raise HTTPException(status_code=401, detail="invalid creds")
    token = uuid.uuid4().hex
    FAKE_TOKENS[token] = email
    return {"access_token": token, "token_type":"bearer"}

@router.get("/me")
def me(user: User = Depends(get_current_user)):
    return user
