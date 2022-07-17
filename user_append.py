import sqlite3
import pandas as pd

db_user = 'userdata.db'

conn = sqlite3.connect(db_user,
                       isolation_level=None
                    )
c=conn.cursor()

def user_data_table():
    # c = conn.cursor()
    sql = """
        CREATE TABLE USER(
            username VARCHAR(20),
            email    VARCHAR(20),
            password VARCHAR(20),
            token    VARCHAR(20)
        );
    """ 
    c.execute(sql)
    c.close()
    
# user_data_table()

# sql = (name, foodname, unit1, unit2, calorie, today)
#     c = conn.cursor()
#     c.execute("insert into FOOD VALUES(?, ?, ?, ?, ?, ?)",sql)
name = 'aiai'
email = 'ahiahi@example.com'
password = 'hello'
token = 'name'

users_information = {
    "shion" : {
        "username" : "shion",
        "email" : "usushio2002@gmail.com",
        "hashed_password" : "ahiahi",
        "token" : "shiota",
        # "disabled" : False,
    },
    "alice" : {
        "username" : "alice",
        "email" : "alice@example.com",
        "hashed_password": "secret2",
        "token" : "token",
        # "disabled" : True,
    },
}
example = {
        "ahiahi" : {
        "username" : "ahiahi",
        "email" : "ahiahi@example.com",
        "hashed_password" : "hello",
        "token" : "hehehe",
        # "disabled" : False,
    },
}

data_input= {
    "name" : {
        "username" : "default",
        "email" : "ahiahi@example.com",
        "hashed_password" : "default",
        "token" : "default",
    }
}

def user_write():
# c.execute("CREATE TABLE sample (username VARCHAR(20), email VARCHAR(20), hashed_password VARCHAR(20),")
    all = """SELECT DISTINCT * FROM USER"""
    c.execute(all)
    for item in c :
        if item[3] == token:
            c.close()
            return False
    sql = (name, email, password, token)
    c.execute("insert into USER values(? ,?, ?, ?)", sql)
    c.close()
# c.execute("INSERT INTO sample VALUES ()")
print(user_write())

def user_replay():
    c=conn.cursor()
    all = """SELECT DISTINCT * FROM USER"""
    c.execute(all)
    for item in c :
        change_dict_key(data_input, "name", item[0])
        data_input.update({item[0] : {"username" : item[0], "email" : item[1], "hashed_password" : item[2], "token" : item[3]}})
        no_duplication(users_information, data_input)
        replay = users_information
    c.close()
    return replay
        # print(information_replay())

def change_dict_key(d, old_key, new_key, default_value=None):
    d[new_key] = d.pop(old_key, default_value)

def input_user_data(name, new_name,new_email,new_password, new_token):
    change_dict_key(data_input, "name", name)
    data_input.update({ name : {"username" : new_name, "email" : new_email, "hashed_password" : new_password, "new_token" : new_token}})
    # data_input.update("username" : new_name,"hashed_password" : new_password})

def input_data():
    input_user_data("ahiahiahi","ahiahiahi", "ahiahiahi@example.com", "enter", "ahiahiahi")
    return data_input
    
def no_duplication(information :dict, beginner: dict):
    flag = True
    example_keys = list(beginner.keys())
    example_value = list(beginner.values())
    
    for key, value in users_information.items():
        if key == example_keys or value == example_value:
            flag == False
        
    if flag == True:
        users_information.update(beginner)
    return users_information

def information_replay():
    no_duplication(users_information, input_data())
    replay = users_information
    return replay

user_replay()