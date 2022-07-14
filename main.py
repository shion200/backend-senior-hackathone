from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/items")
async def read_items(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip":skip, "limit":limit}

@app.get("/users")
async def read_users(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q" : q, "skip": skip, "limit":limit}
