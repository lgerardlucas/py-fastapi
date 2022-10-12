from datetime import datetime, timedelta
import os
from re import A
from symbol import break_stmt
from typing import Any, Union
from passlib.context import CryptContext
from passlib.hash import sha256_crypt
from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from app.account.models import Account

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

SECRET_KEY = os.getenv('SECRET_KEY')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
ACCESS_TOKEN_EXPIRE_HOURS = int(os.getenv('ACCESS_TOKEN_EXPIRE_HOURS'))

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)


def criar_token_jwt(subject: Union[str, Any]) -> str:
    '''
    Function - Cria token
    '''
    expire = datetime.utcnow() + timedelta(
        hours=ACCESS_TOKEN_EXPIRE_HOURS
    )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS512")
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    '''
    Function - Pega a senha simples e compara com a hash 
               gerada da mesma no ato de gravar o cliente
    '''
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    '''
    Function - Gera a hash da senha do usuário a ser gravada
    '''
    return pwd_context.hash(password)

def get_current_user(token: str = Depends(reuseable_oauth)) -> Account:
    terminar esta parte
    https://www-freecodecamp-org.translate.goog/news/how-to-add-jwt-authentication-in-fastapi/?_x_tr_sl=auto&_x_tr_tl=pt&_x_tr_hl=pt-BR
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)
        
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    user: Union[dict[str, Any], None] = db.get(token_data.sub, None)
    
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    
    return SystemUser(**user)
