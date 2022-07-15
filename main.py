from fastapi import FastAPI, Depends, HTTPException, status
from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

import user_append

users_db = user_append.information_replay()

app = FastAPI()

def fake_hash_password(password: str):
    return password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")

class User(BaseModel):
    username : str
    email : Optional[str] = None
    full_name : Optional[str] = None
    disabled : Optional[bool] = None
    
class UserInDB(User):
    hashed_password: str
    
# class UserInEmail(User):
#     email : str

def get_user(sb, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    user = get_user(users_db, token)
    return user

# def get_email(email: str):
#     return email

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invaild authentication credential",
            headers = {"www-Authenticate" : "Bearer"},
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code = 400, detail = "Inactive user")
    return current_user
 
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code = 400, detail = "Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code = 400, detail = "Incorrect username or password")
    # mail = UserInEmail(**user_dict)
    # user_email = get_email(form_data.email)
    # if not user_email == mail.email:
    #     raise HTTPException(status_code = 400, detail = "Incorrect email")
    return {"access_token" : user.username, "token_type" : "bearer"}
    

# @app.get("/items")
# async def read_items(q: Optional[str] = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip":skip, "limit":limit}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
