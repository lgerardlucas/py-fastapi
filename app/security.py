'''
Module - Security
'''
import os
from datetime import datetime, timedelta
from typing import Any, Union, Optional
from .settings import configuration as settings

from passlib.context import CryptContext
from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from pydantic import BaseModel

from .db.db import DBConnect
from .db.querys import SQLQuery
from .account.models import Account

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

SECRET_KEY = settings.SECRET_KEY
JWT_ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_HOURS = settings.ACCESS_TOKEN_EXPIRE_HOURS

def conect_db():
    '''
    Function - Connect/Disconect database
    '''
    cur = DBConnect()
    try:
        yield cur
    finally:
        cur.close()


reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/api/v1/login",
    scheme_name="JWT"
)


def criar_token_jwt(subject: Union[str, Any]) -> str:
    '''
    Function - Create token
    '''

    expire = datetime.utcnow() + timedelta(
        hours=int(ACCESS_TOKEN_EXPIRE_HOURS)
    )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS512")
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    '''
    Function - Verify hashed password vs password simple
    '''

    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    '''
    Function - Generate hash password to user new or old
    '''

    return pwd_context.hash(password)


class TokenPayload(BaseModel):
    '''
    Class - Classe serialize token
    '''

    exp: Optional[int] = None
    sub: Optional[str] = None


def get_current_user(token: str = Depends(reuseable_oauth),
        data_base: Any = Depends(conect_db)) -> Account:
    '''
    Function - Validate user logged
    '''

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])

        token_data = TokenPayload(**payload)
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token vencido! "+
                        str(datetime.fromtimestamp(token_data.exp))+
                        str(datetime.now()),
                headers={"WWW-Authenticate": "Bearer"},
            )
    except jwt.ExpiredSignatureError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Autorização token expirada!",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc

    except jwt.JWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Não foi possível validar as credenciais do usuário! \
                Favor entrar com um token válido.",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc

    query: SQLQuery = SQLQuery(token_data.sub, 'account', 'email')
    user: Account = data_base.query(query.query_search())

    if len(user) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado!",
        )

    return user
