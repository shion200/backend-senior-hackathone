from pydantic import BaseModel


class SignUpUser(BaseModel):
    username:str
    password:str
    email:str

class SignInUser(BaseModel):
    username:str
    password:str

class AuthInfo(BaseModel):
    jwt:str

class loginUser(BaseModel):
    token:str
    username:str
