"""
Module - Router -> ACCOUNT
"""
from typing import Any, List
from fastapi import APIRouter, HTTPException, status, Depends
from ..account.models import Account
from ..db.db import DBConnect
from ..db.querys import SQLQuery
from ..security import criar_token_jwt, verify_password


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


@router.get("/api/v1/accounts",
            description="Lista de todos os usuários",
            summary="Lista de usuários",
            response_model=List[Account],
            response_description='Lista de usuários retornadas com sucesso!'
            )
async def get_accounts(data_base: Any = Depends(conect_db)):
    '''
    GET - Record list from database
    '''
    query: SQLQuery = SQLQuery(0, 'account')
    query_result: Account = data_base.query(query.query_search())

    if len(query_result) != 0:
        return query_result
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Registro não encontrado!')

@router.post("/api/v1/account",
             status_code=status.HTTP_201_CREATED,
             description="Salva o novo usuário",
             summary="Salvar usuário",
             response_model=Account,
             response_description='Usuário gravado com sucesso!'
             )
async def post_paroquia(account: Account, data_base: Any = Depends(conect_db)):
    '''
    POST - Save register new in database
    '''
    if account:
        query: SQLQuery = SQLQuery(0, 'account')
        ret: bool = data_base.manipulate(query.insert(
            username=account.username,
            email=account.email,
            password=account.password)
        )

    if ret:
        return account
    else:
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED,
            detail='Registro não incluído!')

@router.get("/api/v1/login")
async def login(username: str, password: str,
                data_base: Any = Depends(conect_db)):
    '''
    Function - teste do teste
    '''
    query: SQLQuery = SQLQuery(1, 'account')
    user: Account = data_base.query(query.query_search())

    if not user or not verify_password(password, user[0]['hashed_password']):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Email {username} ou nome de usuário incorretos"
                           )
    return {
        "access_token": criar_token_jwt(user[0]['email']),
        "token_type": "bearer",
    }