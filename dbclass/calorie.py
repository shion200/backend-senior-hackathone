from typing import List

from pydantic import BaseModel


class dateOfDay(BaseModel):
    date:int
    calorie:int

class caloKUSA(BaseModel):
    detailOfDate:List[dateOfDay]
    calorieAverage:int
    calorieSum:int

class inputCalorie(BaseModel):
    token:str
    calorie:int
    date:int

class userCalorie(BaseModel):
    token:str
    goalCalorie:int

class foodCalorie(BaseModel):
    food:str
    calorie:int

class food(BaseModel):
    food:str
