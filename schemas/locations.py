from pydantic import BaseModel
from typing import Optional, Union
class Location(BaseModel):
    id : Optional[int]
    latitude : Union[float,int]
    longitude: Union[float,int]
    name : str
    Address: str
    
    class Config:
        orm_mode = True
