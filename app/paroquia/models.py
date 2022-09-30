'''
MODELS - Class model to PARÓQUIA
'''
from typing import Union, Optional
from pydantic import BaseModel, Field


class Paroquia(BaseModel):
    '''
    Class - Model Paróquina
    '''
    id: Optional[int]
    name: str =  Field(None, max_length=200)
    street: Union[str, None] = None
    district: Union[str, None] = None
    city: Union[str, None] = None

    class Config:
        '''
        Class - Config ORM
        '''
        orm_mode = True
