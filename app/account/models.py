'''
MODELS - Class model to ACCOUNT
'''
from typing import Optional
from pydantic import BaseModel, EmailStr


class Account(BaseModel):
    '''
    Class - Model Account
    '''
    id: Optional[int]
    username: str
    email: EmailStr
    password = str
    hashed_password: str


    class Config:
        '''
        Class - Config ORM
        '''
        orm_mode = True
