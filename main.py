import os
import secrets
import sqlite3
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

import user_append
from dbclass.calorie import caloKUSA, inputCalorie, userCalorie
from dbclass.ranking import ranking
from dbclass.user import SignInUser, SignUpUser, loginUser
from methods.calorie import getUserCalorie, setCalorieOfDay, setCalorieOfGoal
from methods.ranking import getCalorieRanking
from methods.user import addUser, signinUser

users_db = user_append.user_replay()
name = 'shion'
app = FastAPI()
conn= sqlite3.connect('userdata.db')
db = conn.cursor()
def fake_hash_password(password: str):
    return password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")

class User(BaseModel):
    username : str
    email : Optional[str] = None
    token:str
    full_name : Optional[str] = None
    disabled : Optional[bool] = None

class UserInDB(User):
    hashed_password: str

# class UserInEmail(User):
#     email : str


# def get_user(sb, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)

# def fake_decode_token(token):
#     user = get_user(users_db, token)
#     return user

# # def get_email(email: str):
# #     return email

# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     user = fake_decode_token(token)
#     if not user:
#         raise HTTPException(
#             status_code = status.HTTP_401_UNAUTHORIZED,
#             detail = "Invaild authentication credential",
#             headers = {"www-Authenticate" : "Bearer"},
#         )
#     return user

# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#     if current_user.disabled:
#         raise HTTPException(status_code = 400, detail = "Inactive user")
#     return current_user

# @app.post("/token")
# async def login(payload: OAuth2PasswordRequestForm = Depends()):
#     print(payload.username)
#     user_dict = users_db.get(payload.username)
#     name = user_dict
#     if not user_dict:
#         raise HTTPException(status_code = 400, detail = "Incorrect username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hash_password(payload.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code = 400, detail = "Incorrect username or password")
#     # mail = UserInEmail(**user_dict)
#     # user_email = get_email(payload.email)
#     # if not user_email == mail.email:
#     #     raise HTTPException(status_code = 400, detail = "Incorrect email")
#     return {"access_token" : user.token, "token_type" : "bearer"}

# @app.post("/signup")
# async def siginup():

# @app.get("/items")
# async def read_items(q: Optional[str] = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip":skip, "limit":limit}

# @app.get("/users/me")
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user

# if __name__ == "__main__":
#     port = int(os.getenv("PORT", 5000))
#     app.run(host="0.0.0.0", port=port)
@app.post("/signup")
async def signup(payload:SignInUser):
    response =  addUser(db,conn,payload.username,payload.password)
    if response == "username exist":
        raise HTTPException(status_code = 400, detail = response)
    return response

@app.post("/signin",response_model= loginUser)
async def signin(payload:SignUpUser):
    response =  signinUser(db,payload.username,payload.password)
    if response == "Incorrect username or password":
        raise HTTPException(status_code = 400, detail = response)

    return response

@app.get("/caloKUSA",response_model=caloKUSA)
async def calokusa(payload:loginUser):
    response =  getUserCalorie(db,payload.token)
    if response == "data is null":
        raise HTTPException(status_code = 400, detail = response)

    return response

@app.post("/setCalorieOfDay",response_model=caloKUSA)
async def SetCalorieOfDay(payload:inputCalorie):
    response =  setCalorieOfDay(db,conn,payload.calorie,payload.date,payload.token)
    if response == "update calorie":
        raise HTTPException(status_code = 200, detail = response)

    return False
@app.post("/setCalorieOfGoal",response_model=userCalorie)
async def SetCalorieOfGoal(payload:loginUser):
    response = setCalorieOfGoal(db,conn,payload.calorie,payload.date,payload.token)
    if response == "update calorie":
        raise HTTPException(status_code = 200, detail = response)

    return False

@app.get("/getCalorieRanking",response_model=ranking)
async def GetCalorieRanking():
    response = getCalorieRanking(db)

    return response

