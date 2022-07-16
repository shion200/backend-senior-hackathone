users_information = {
    "shion" : {
        "username" : "shion",
        "email" : "usushio2002@gmail.com",
        "hashed_password" : "ahiahi",
        # "disabled" : False,
    },
    "alice" : {
        "username" : "alice",
        "email" : "alice@example.com",
        "hashed_password": "secret2",
        # "disabled" : True,
    },
}

example = {
        "ahiahi" : {
        "username" : "ahiahi",
        "email" : "ahiahi@example.com",
        "hashed_password" : "hello",
        # "disabled" : False,
    },
}

data_input= {
    "name" : {
        "username" : "default",
        "email" : "ahiahi@example.com",
        "hashed_password" : "default",
    }
}
def change_dict_key(d, old_key, new_key, default_value=None):
    d[new_key] = d.pop(old_key, default_value)

def input_user_data(name, new_name, new_password):
    change_dict_key(data_input, "name", name)
    data_input.update({ name : {"username" : new_name, "hashed_password" : new_password}})
    # data_input.update("username" : new_name,"hashed_password" : new_password})

def input_data():
    input_user_data("ahiahiahi","ahiahiahi", "enter")
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