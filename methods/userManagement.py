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
    db.execute('INSERT INTO userstable(username,password,token) VALUES (?,?,?)',(username,makeHash(password),secrets.token_hex()))
    if db.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password)):
        return "username exist"

    connectedDB.commit()
    return "create new user"

async def loginUser(db,username,password):
    db.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = db.fetchall()
    return data
