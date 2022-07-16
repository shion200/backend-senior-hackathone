import sqlite3
import pandas as pd

import get_meal_calorie 
import main

name = 'shion'
foodname = '煮込み' 
unit1 = 757
unit2 = 0
calorie = 522

db_name = "meal_data.db"
conn = sqlite3.connect(db_name,
                       isolation_level=None
                    )

# sql = """
#     CREATE TABLE FOOD(
#         username VARCHAR(20),
#         foodname VARCHAR(20),
#         unit1    INTEGER,
#         unit2    INTEGER,
#         calorie  INTEGER
#     );
# """ 

# sql = f"""
#     INSERT INTO FOOD VALUES(
#         {name},
#         {foodname},
#         {unit1},
#         {unit2},
#         {calorie}
#     )
# """

sql = (name, foodname, unit1, unit2, calorie)
c = conn.cursor()
a = conn.cursor()

namevalue = """SELECT DISTINCT username FROM FOOD"""
# c.execute(all)
c.execute("insert into FOOD VALUES(?, ?, ?, ?, ?)",sql)
all = """SELECT DISTINCT * FROM FOOD"""

a.execute(namevalue)
c.execute(all)
# data = c.fetchall()

for item_all in c:
    user = item_all[0]
    if user == name:
        print(item_all)
c.close()

# def read_not_same_name():
    
# print(sql)
# conn.commit()
# conn.in_transaction = False
# conn.execute(sql)
# conn.close()
    