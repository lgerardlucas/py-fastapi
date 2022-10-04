'''
MODELS - Class model to ACCOUNT
'''
from typing import Union, Optional
from pydantic import BaseModel


class Account(BaseModel):
    '''
    Class - Model Account
    '''
    id: Optional[int]
    username: Union[str, None] = None
    email: Union[str, None] = None
    password: Union[str, None] = None
    hashed_password: Union[str, None] = None


    class Config:
        '''
        Class - Config ORM
        '''
        orm_mode = True
