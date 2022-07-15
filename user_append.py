users_information = {
    "shion" : {
        "username" : "shion",
        # "full_name" : "shion kyumma",
        "email" : "usushio2002@gmail.com",
        "hashed_password" : "ahiahi",
        "disabled" : False,
    },
    "alice" : {
        "username" : "alice",
        # "full_name" : "Alice Wonderson",
        "email" : "alice@example.com",
        "hashed_password": "secret2",
        "disabled" : True,
    },
}

def user_return():
    return users_information

def information_append(information):
    users_information.append(information)
    
# example = {
#         "ahiahi" : {
#         "username" : "ahiahi",
#         "email" : "ahiahi@example.com",
#         "hashed_password" : "hello",
#         "disabled" : False,
#     },
# }

# information_append(example)