from typing import List

from pydantic import BaseModel


class rankingUser(BaseModel):
    username:str
    caloryOfDay:int
    differenceOfCalory:int
    dispersionOfCalory:float

class ranking(BaseModel):
    rankingArray:List[rankingUser]
