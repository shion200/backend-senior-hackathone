async def getCalorieRanking(db):
    db.execute('SELECT * FROM userstable')
    data = db.fetchall()
    if data == []:
        return "data is null"
    return data
