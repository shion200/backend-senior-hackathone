from fastapi import FastAPI, Depends, HTTPException, status
from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "shion" : {
        "username" : "shion",
        "full_name" : "shion kyumma",
        "email" : "usushio2002@gmail.com",
        "password" : "ahiahi",
        "disabled" : False,
    },
    "alice" : {
        "username" : "alice",
        "full_name" : "Alice Wonderson",
        "email" : "alice@example.com",
        "password": "fakehashedsecret2",
        "disabled" : True,
    },
}
app = FastAPI()

@app.get("/items")
async def read_items(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip":skip, "limit":limit}

@app.get("/users")
async def read_users(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q" : q, "skip": skip, "limit":limit}
