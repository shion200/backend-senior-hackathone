from pydantic import BaseModel


class dateOfDay(BaseModel):
    date:int
    calorie:int

class caloKUSA(BaseModel):
    detailOfDate:dateOfDay
    calorieAverage:int
    calorieSum:int

class inputCalorie(BaseModel):
    token:str
    calorie:int
    date:int

class userCalorie(BaseModel):
    token:str
    goalCalorie:int
