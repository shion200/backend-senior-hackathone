from fastapi import FastAPI, Depends, HTTPException, status
from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "shion" : {
        "username" : "shion",
        "full_name" : "shion kyumma",
        "email" : "usushio2002@gmail.com",
        "hashed_password" : "fakehashedahiahi",
        "disabled" : False,
    },
    "alice" : {
        "username" : "alice",
        "full_name" : "Alice Wonderson",
        "email" : "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled" : True,
    },
}
app = FastAPI()

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")

class User(BaseModel):
    username : str
    email : Optional[str] = None
    full_name : Optional[str] = None
    disabled : Optional[bool] = None
    
class UserInDB(User):
    hashed_password: str

def get_user(sb, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user

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
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code = 400, detail = "Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code = 400, detail = "Incorrect username or password")
    return {"access_token" : user.username, "token_type" : "bearer"}

# @app.get("/items")
# async def read_items(q: Optional[str] = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip":skip, "limit":limit}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
