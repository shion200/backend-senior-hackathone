import save_data
# type rankingUser = {
#     "userName" : string,
#     "calorie" : number,
# }
# type ranking = {
#     "users" : rankingUser[],
# }

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

print(ranking())