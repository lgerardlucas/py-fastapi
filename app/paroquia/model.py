from typing import Union, Optional
from urllib import request
from pydantic import BaseModel, validator


class Paroquia(BaseModel):
    id: Optional[int]
    name: str
    street: Union[str, None] = None
    district: Union[str, None] = None
    city: Union[str, None] = None
    
    @validator('name')
    def validator_name(cls, value: str):
        word = value.split(' ')
        if len(word) < 3:
            raise ValueError('Nome deve conter pelo menos 3 palavras')
        
        return value

    @validator('street')
    def validator_street(cls, value: str):
        if value:
            definition = ['RUA', 'AVENIDA', 'BR']
            for i in range(len(definition)):
                street_definition = True if definition[i] in value.upper() else False
                if street_definition:
                    break
                
            if not street_definition:
                raise ValueError('Defina o tipo de endereço (Rua, Avenida ou BR)')

        return value

    class Config:
        orm_mode = True
