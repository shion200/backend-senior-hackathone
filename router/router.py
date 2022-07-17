import sqlite3
from typing import List

import DBclass.user as cl
import methods.user as UM
from fastapi import Depends, FastAPI, HTTPException, status
from main import User
from pydantic import BaseModel  # リクエストbodyを定義するために必要

app = FastAPI()
conn= sqlite3.connect('database.db')
db = conn.cursor()

@app.post("/signup/")
def read_item(user:User):
    response =  UM.addUser(db,user.username,user.password)
    if response == "username exist":
        raise HTTPException(status_code = 400, detail = response)

    return response
