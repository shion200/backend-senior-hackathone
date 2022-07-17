import os
import secrets
import sqlite3

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import classname
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

classname.User(BaseModel)
classname.UserInDB(User)
# class User(BaseModel):
#     username : str
#     email : Optional[str] = None
#     token:str
#     full_name : Optional[str] = None
#     disabled : Optional[bool] = None

# class UserInDB(User):
#     hashed_password: str

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