import datetime

import save_data

def date():
    dt = datetime.datetime.now()
    return dt.day

calorieSum = save_data.mouth_calorie_sum()
calorieAverage = save_data.mouth_calorie_sum()/date()
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