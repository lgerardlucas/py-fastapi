'''
Module - OAuth Autentication Module
'''
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from ..security import SECRET_KEY, JWT_ALGORITHM
from ..account.models import Account
from ..db.db import DBConnect
from ..db.querys import SQLQuery

router = APIRouter()


def conect_db():
    '''
    Function - Connect/Disconect database
    '''
    cur = DBConnect()
    try:
        yield cur
    finally:
        cur.close()
