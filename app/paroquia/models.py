'''
MODELS - Class model to PARÓQUIA
'''
from typing import Union, Optional
from pydantic import BaseModel, Field


class Paroquia(BaseModel):
    '''
    Class - Model Paróquia
    '''
    id: Optional[int]
    name: str =  Field(None, max_length=200)
    street: Optional[str]
    district: Optional[str]
    city: Optional[str]

    class Config:
        '''
        Class - Config ORM
        '''
        orm_mode = True
