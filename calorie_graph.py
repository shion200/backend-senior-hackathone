import save_data

calorieSum = save_data.mouth_calorie_sum()
calorieAverage = save_data.mouth_calorie_sum()/save_data.date()

# print(calorieSum)
# print(calorieAverage)

def calorie_num():
    data = {
        "detailOfDate" : {"date" : save_data.date(),
                          "calorie" : save_data.day_calorie_sum()},
        "calorieAverage" : calorieAverage,
        "calorieSum" : calorieSum
    }
    return data

# print(calorie_num())
# print(date())
# type detailOfDate = {
#     "date" : number,
#     "calorie" : number
# }
# type data = {
#     "detailOfDate" : detailOfDate[]
#     "calorieAverage" : number,
#     "calorieSum" : number
# }