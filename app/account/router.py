"""
Module - Router -> ACCOUNT
"""
from typing import Any, List
from fastapi import APIRouter, HTTPException, status, Depends
from ..account.models import Account
from ..db.db import DBConnect
from ..db.querys import SQLQuery
from ..security import criar_token_jwt, verify_password, get_password_hash, get_current_user


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
async def get_accounts(data_base: Any = Depends(conect_db),
        get_user_loged: Account = Depends(get_current_user)):
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
async def post_account(account: Account, 
        data_base: Any = Depends(conect_db)):
    '''
    POST - Add user new
    '''
    if account:
        query: SQLQuery = SQLQuery(account.email, 'account', 'email')
        query_result: Account = data_base.query(query.query_search())

        if len(query_result) > 0:
            raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED,
            detail='Registro já existente na base de dados!')

        query: SQLQuery = SQLQuery(0, 'account')
        query_result: bool = data_base.manipulate(query.insert(
            username=account.username,
            email=account.email,
            password=account.password,
            hashed_password=get_password_hash(account.password))
        )

    if query_result:
        return account
    else:
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED,
            detail='Registro não incluído!')

@router.get("/api/v1/login")
async def login(username: str, password: str,
        data_base: Any = Depends(conect_db)):
    '''
    GET - Valida o login e retorna o token
    '''
    query: SQLQuery = SQLQuery(username, 'account', 'email')
    query_result: Account = data_base.query(query.query_search())

    if not query_result:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Email {username} não cadastrado!"
        )
    if not verify_password(password, query_result[0]['hashed_password']):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Email {username} do usuário está incorreto!"
        )
    return {
        "access_token": criar_token_jwt(query_result[0]['email']),
        "token_type": "bearer",
    }
