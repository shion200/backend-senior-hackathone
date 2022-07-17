import hashlib
import secrets
import sqlite3


async def makeHash(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

async def checkHash(password,hashedPassword):
    if  makeHash(password) == hashedPassword:
        return hashedPassword
    return False

async def addUser(db,connectedDB,username,password):
    db.execute('INSERT INTO loginUser(username,password,token) VALUES (?,?,?)',(username,makeHash(password),secrets.token_hex()))
    if db.execute('SELECT * FROM loginUSer WHERE username =?',(username,)):
        return "username exist"

    connectedDB.commit()
    return "create new user"

async def signinUser(db,username,password):
    db.execute('SELECT token,userName FROM loginUser WHERE username =? AND password = ?',(username,password))
    data = db.fetchall()
    if data == []:
        return "Incorrect username or password"
    return data
