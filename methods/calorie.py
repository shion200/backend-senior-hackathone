import hashlib
import secrets
import sqlite3


async def makeHash(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

async def checkHash(password,hashedPassword):
    if  makeHash(password) == hashedPassword:
        return hashedPassword
    return False

async def setCalorieOfDay(db,connectedDB,inputCalorie,date,token):
    try:
        calorie =  db.execute('SELECT * FROM userstable WHERE token =? AND date = ?',(token,date))+inputCalorie
    except:
        calorie = inputCalorie
    db.execute('INSERT INTO userstable(token,calorie,date) VALUES (?,?,?)',(token,calorie,date))

    connectedDB.commit()
    return "update calorie"

async def getUserCalorie(db,token):
    db.execute('SELECT * FROM userstable WHERE token =?',(token))
    data = db.fetchall()
    if data == []:
        return "data is null"
    return data
async def setCalorieOfDay(db,connectedDB,inputCalorie,date,token):
    db.execute('INSERT INTO userstable(token,calorie,date) VALUES (?,?,?)',(token,calorie,date))

    connectedDB.commit()
    return "update calorie"
async def setCalorieOfGoal(db,connectedDB,goalCalorie,date,token):
    db.execute('INSERT INTO userstable(token,calorie,date) VALUES (?,?,?)',(token,calorie,date))

    connectedDB.commit()
    return "update calorie"

async def getUserCalorieGoal(db,token):
    db.execute('SELECT * FROM userstable WHERE token =?',(token))
    data = db.fetchall()
    if data == []:
        return "data is null"
    return data
