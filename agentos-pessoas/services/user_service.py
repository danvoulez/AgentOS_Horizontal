
from agentos_pessoas.models.user_model import User
from uuid import uuid4
USERS: dict[str, User] = {}

def create_user(u: User)->User:
    u.id = uuid4().hex
    USERS[u.email] = u
    return u

def get_user(email:str)->User|None:
    return USERS.get(email)
