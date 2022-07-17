import sqlite3
import pandas as pd

import save_data
# type rankingUser = {
#     "userName" : string,
#     "calorie" : number,
# }
# type ranking = {
#     "users" : rankingUser[],
# }

db_rank = 'ranking.db'

conn = sqlite3.connect(db_rank,
                       isolation_level=None
                    )

# c=conn.cursor()

token = "name"
name = "dori-"
calo = 100

def rank():
    c = conn.cursor()
    rank_sql = """
        CREATE TABLE RANK(
            token      VARCHAR(20),
            username   VARCHAR(20),
            calorie    INTEGER
        );
    """ 
    c.execute(rank_sql)
    c.close()
    
# rank()
    
def rank_write():
    c = conn.cursor()
    # c.execute("CREATE TABLE sample (username VARCHAR(20), email VARCHAR(20), hashed_password VARCHAR(20),")
    all = """SELECT DISTINCT * FROM RANK"""
    c.execute(all)
    for item in c :
        if item[0] == token:
            c.execute("UPDATE RANK SET calorie = ? WHERE token = ?", [calo, token])
            c.close()
            return True
    sql = (token, name, calo)
    c.execute("insert into RANK values(? ,?, ?)", sql)
    c.close()    
    
def rank_num():
    c = conn.cursor()
    c.execute("""SELECT * FROM RANK ORDER BY calorie ASC;""")
    for item in c :
        print(item)
    
rank_num()
    
# rank_write()
    
name = "shion"
num = save_data.mouth_calorie_sum()
def ranking():
    ranking_number = {
        "users" : {
            "username" : name,
            "calorie" : num,
        }
    }
    return ranking_number

# print(ranking())