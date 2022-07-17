import hashlib
import secrets
import sqlite3

from methods.get_meal_calorie import main


async def makeHash(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

async def checkHash(password,hashedPassword):
    if  makeHash(password) == hashedPassword:
        return hashedPassword
    return False

async def setCalorieOfDay(db,connectedDB,inputCalorie,date,token):
    try:
        calorie =  db.execute('SELECT todayCalorie FROM calorie WHERE token =?',(token,))+inputCalorie
    except:
        calorie = inputCalorie
    db.execute('UPDATE calorie SET VALUES (?,?,?)',(token,calorie,date))

    connectedDB.commit()
    return "update calorie"

async def getUserCalorie(db,token):
    db.execute('SELECT thisMonthCalorie FROM calorie WHERE token =?',(token,))
    data = db.fetchall()
    if data == []:
        return "data is null"
    return data

async def setCalorieOfGoal(db,connectedDB,goalCalorie,token):
    db.execute('UPDATE calorie SET goal WHERE token',(goalCalorie,token))

    connectedDB.commit()
    return "update calorie"

async def getUserCalorieGoal(db,token):
    db.execute('SELECT goal FROM calorie WHERE token =?',(token))
    data = db.fetchall()
    if data == []:
        return "data is null"
    return data

async def scrapingFoodCalorie(foodname):
    calorie_data = main(foodname)
    return calorie_data[0]

async def getFoodCalorie(db,connectedDB,food):
    db.execute('SELECT * FROM userstable WHERE food =?',(food))
    data = db.fetchall()
    if data == []:
        calorie_data = scrapingFoodCalorie(food)
        db.execute('INSERT INTO userstable(food,calorie) VALUES (?,?)',(food["name"],food["calorie"]))
        connectedDB.commit()
        db.execute('SELECT * FROM userstable WHERE food =?',(food))
        data = db.fetchall()
    return data
