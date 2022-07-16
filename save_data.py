import sqlite3
import pandas as pd
import datetime

import get_meal_calorie 
import main

def date():
    dt = datetime.datetime.now()
    return dt.day

name = 'shion'
foodname = 'カレーうどん' 
unit1 = 757
unit2 = 0
calorie = 456
today = date()

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
            calorie  INTEGER,
            today    INTEGER
        );
    """ 
    c.execute(sql)
    c.close()

# data_table()

# sql = f"""
#     INSERT INTO FOOD VALUES(
#         {name},
#         {foodname},
#         {unit1},
#         {unit2},
#         {calorie},
#         {today},
#     )
# """
def data_write():
    sql = (name, foodname, unit1, unit2, calorie, today)
    c = conn.cursor()
    c.execute("insert into FOOD VALUES(?, ?, ?, ?, ?, ?)",sql)
    # c.commit()
    # c.in_transaction = False
    c.close()

# c.execute(all)
# data_write()
def data_read():
    all = """SELECT DISTINCT * FROM FOOD"""
    c = conn.cursor()
    c.execute(all)
    for item_all in c:
        print(item_all)
        user = item_all[0]
        if user == name:
            print(item_all)
    c.close()

data_read()

def mouth_calorie_sum():
    ans = 0
    all = """SELECT DISTINCT * FROM FOOD"""
    c = conn.cursor()
    c.execute(all)
    for item_all in c:
        user = item_all[0]
        if user == name:
            ans += item_all[4]
    return ans

def day_calorie_sum():
    ans = 0
    all = """SELECT DISTINCT * FROM FOOD"""
    c = conn.cursor()
    c.execute(all)
    for item_all in c:
        user = item_all[0]
        if user == name and date() == item_all[5]:
            ans += item_all[4]
    return ans
    
# print(mouth_calorie_sum())
# def read_not_same_name():
    
# print(sql)
# conn.execute(sql)
# conn.close()
    