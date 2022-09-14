from typing import Union
from pydantic import BaseModel

class Paroquia(BaseModel):
    name: str
    street: Union[str, None] = None
    district: Union[str, None] = None
    city: Union[str, None] = None

    class Config:
        orm_mode = True
