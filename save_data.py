import sqlite3
import pandas as pd

import get_meal_calorie 
import main
import calorie_graph

name = 'shion'
foodname = '煮込み' 
unit1 = 757
unit2 = 0
calorie = 522
date = calorie_graph.date()

db_name = "meal_data.db"
conn = sqlite3.connect(db_name,
                       isolation_level=None
                    )
def data_table():
    c = conn.cursor()
    sql = """
        CREATE TABLE FOOD(
            username VARCHAR(20),
            foodname VARCHAR(20),
            unit1    INTEGER,
            unit2    INTEGER,
            calorie  INTEGER
            date     INTEGER
        );
    """ 
    c.eecute(sql)
    c.close()

# sql = f"""
#     INSERT INTO FOOD VALUES(
#         {name},
#         {foodname},
#         {unit1},
#         {unit2},
#         {calorie},
#         {date},
#     )
# """
def data_write():
    sql = (name, foodname, unit1, unit2, calorie, date)
    c = conn.cursor()
    c.execute("insert into FOOD VALUES(?, ?, ?, ?, ?, ?)",sql)
    c.commit()
    c.in_transaction = False
    c.close()

# c.execute(all)

def data_read():
    all = """SELECT DISTINCT * FROM FOOD"""
    c = conn.cursor()
    c.execute(all)
    for item_all in c:
        user = item_all[0]
        if user == name:
            print(item_all)
    c.close()

def mouth_calorie_sum():
    ans = 0
    all = """SELECT DISTINCT * FROM FOOD"""
    c = conn.cursor()
    for item_all in c:
        user = item_all[0]
        if user == name:
            ans += item_all[4]
    return ans

# def read_not_same_name():
    
# print(sql)
# conn.execute(sql)
# conn.close()
    