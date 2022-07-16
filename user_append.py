users_information = {
    "shion" : {
        "username" : "shion",
        # "full_name" : "shion kyumma",
        # "email" : "usushio2002@gmail.com",
        "hashed_password" : "ahiahi",
        # "disabled" : False,
    },
    "alice" : {
        "username" : "alice",
        # "full_name" : "Alice Wonderson",
        # "email" : "alice@example.com",
        "hashed_password": "secret2",
        # "disabled" : True,
    },
}

example = {
        "ahiahi" : {
        "username" : "ahiahi",
        # "email" : "ahiahi@example.com",
        "hashed_password" : "hello",
        # "disabled" : False,
    },
}

def no_duplication(information :dict, beginner: dict):
    flag = True
    example_keys = list(beginner.keys())
    example_value = list(beginner.values())
    
    for key, value in users_information.items():
        if key == example_keys or value == example_value:
            flag == False
        
    if flag == True:
        users_information.update(example)
    return users_information

def information_replay():
    no_duplication(users_information, example)
    replay = users_information
    return replay
