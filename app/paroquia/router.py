"""
Module - Router -> PARÓQUIA
"""
from typing import Any, List
from fastapi import APIRouter, HTTPException, status, Path, Depends
from fastapi.security import OAuth2PasswordBearer
from ..paroquia.models import Paroquia
from ..db.db import DBConnect
from ..db.querys import SQLQuery


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def conect_db():
    '''
    Function - Connect/Disconect database
    '''
    cur = DBConnect()
    try:
        yield cur
    finally:
        cur.close()


@router.get("/api/v1/paroquias",
            description="Lista de todas as Paróquias ativas",
            summary="Lista de Paróquias",
            response_model=List[Paroquia],
            response_description='Lista de Paróquias retornadas com sucesso!'
            )
async def get_paroquias(data_base: Any = Depends(conect_db)):
    '''
    GET - Record list from database
    '''
    query: SQLQuery = SQLQuery(0, 'Paroquia')
    paroquias: Paroquia = data_base.query(query.query_search())

    if len(paroquias) != 0:
        return paroquias
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Registro não encontrado!')


@router.get("/api/v1/paroquia/{id_num}",
            description="Retorna Paróquia pesquisada",
            summary="Retorna Paróquia",
            response_model=List[Paroquia],
            response_description='Paróquia retornada com sucesso!'
            )
async def get_paroquia(id_num: int = Path(default=None,
            title="ID da Paróquina",
            description="Informe o ID da Paróquia"),
            dat_base: Any = Depends(conect_db)):
    '''
    GET - Return one register from database
    '''
    query: SQLQuery = SQLQuery(id_num, 'Paroquia')
    paroquia: Paroquia = dat_base.query(query.query_search())

    if len(paroquia) != 0:
        return paroquia
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Registro não encontrado!')


@router.post("/api/v1/paroquia",
             status_code=status.HTTP_201_CREATED,
             description="Salva a nova Paróquia",
             summary="Salvar Paróquia",
             response_model=Paroquia,
             response_description='Paróquia gravada com sucesso!'
             )
async def post_paroquia(paroquia: Paroquia, data_base: Any = Depends(conect_db)):
    '''
    POST - Save register new in database
    '''
    if paroquia:
        query: SQLQuery = SQLQuery(0, 'Paroquia')
        ret: bool = data_base.manipulate(query.insert(
            name=paroquia.name,
            street=paroquia.street,
            district=paroquia.district,
            city=paroquia.city)
        )

    if ret:
        return paroquia
    else:
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED,
            detail='Registro não incluído!')


@router.put("/api/v1/paroquia/{id_num}",
            description="Atualiza campos da tabela de Paróquias",
            summary="Atualiza Paróquia",
            response_model=Paroquia,
            response_description='Paróquias atualizada com sucesso!'
            )
async def put_paroquia(id_num: int, 
        paroquia: Paroquia, 
        data_base: Any = Depends(conect_db)):
    '''
    PUT - Update one register in dababase
    '''
    ret: bool = False
    query: SQLQuery = SQLQuery(id_num, 'Paroquia')
    paroquia_update: Paroquia = data_base.query(query.query_search())
    if not paroquia_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Registro não localizado para atualização!')

    if paroquia and paroquia_update and id:
        ret = data_base.manipulate(query.update(name=paroquia.name,
            street=paroquia.street,
            district=paroquia.district,
            city=paroquia.city)
        )

    if ret:
        return paroquia
    else:
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED,
            detail='Registro não incluído!')


@router.delete("/api/v1/paroquia/{id_num}",
               status_code=status.HTTP_200_OK,
               response_description='Paróquia deletada com sucesso!'
               )
async def del_paroquia(id_num: int = Path(default=None, 
        title="ID da Paróquina",
        description="Informe o ID da Paróquia"),
        data_base: Any = Depends(conect_db)):
    '''
    DELETE - Delete one register in database
    '''
    query:SQLQuery = SQLQuery(id_num, 'Paroquia')
    paroquia_delete: Paroquia = data_base.query(query.query_search())
    if not paroquia_delete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Registro não localizado para exclusão!')

    if paroquia_delete and id_num:
        data_base.manipulate(query.delete())
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Registro não encontrado!')

    return {"detail": 'Registro excluído com sucesso!'}
