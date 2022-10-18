'''
MODELS - Class model to ACCOUNT
'''
from typing import Union
from pydantic import BaseModel, EmailStr


class Account(BaseModel):
    '''
    Class - Model Account
    '''
    username: Union[str, None] = None
    email: Union[EmailStr, None] = None
    password: Union[str, None] = None

    class Config:
        '''
        Class - Config ORM
        '''
        orm_mode = True
