from multiprocessing.connection import wait
from typing import Any, List
from http.client import HTTPException
from app.db.db import DBConnect
from fastapi import (
    APIRouter, HTTPException, status, Response, Path, Depends
)
from app.paroquia.model import Paroquia
from starlette.requests import Request

router = APIRouter()
 
def conect_db():
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
async def get_paroquias(db: Any = Depends(conect_db)):
    paroquias = db.query('select * from paroquia')

    if len(paroquias) != 0:
        return paroquias
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Registro não encontrado!')


@router.get("/api/v1/paroquia/{id}", 
        description="Retorna Paróquia pesquisada", 
        summary="Retorna Paróquia",
        response_model=List[Paroquia],
        response_description='Paróquia retornada com sucesso!'
        )
async def get_paroquia(id: int = Path(default=None, title="ID da Paróquina", description="Informe o ID da Paróquia"), 
            db: Any = Depends(conect_db)):
    paroquia = db.query('{}{}'.format(
        'select * from paroquia where id = ', id))
    
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
async def post_paroquia(paroquia: Paroquia, db: Any = Depends(conect_db)):
    if paroquia:
        ret = db.manipulate("Insert Into paroquia(name, street, district, city) Values('{}','{}','{}','{}')".format(
            paroquia.name, paroquia.street, paroquia.district, paroquia.city))
    
    if ret:
        return paroquia
    else:
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED,
            detail='Registro não incluído!')


@router.put("/api/v1/paroquia/{id}", 
        description="Atualiza campos da tabela de Paróquias", 
        summary="Atualiza Paróquia",
        response_model=Paroquia,
        response_description='Paróquias atualizada com sucesso!'
        )
async def put_paroquia(id: int, paroquia: Paroquia, db: Any = Depends(conect_db)):
    if paroquia and id:
        ret = db.manipulate("Update paroquia Set name='{}', street='{}', district='{}', city='{}' Where id={}".format(
            paroquia.name, paroquia.street, paroquia.district, paroquia.city, id))
    if ret:
        return paroquia
    else:
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED,
            detail='Registro não incluído!')

@router.delete("/api/v1/paroquia/{id}", 
        status_code=status.HTTP_200_OK,
        response_model=List[Paroquia],
        response_description='Paróquia deletada com sucesso!'
        )
async def del_paroquia(id: int = Path(default=None, title="ID da Paróquina", description="Informe o ID da Paróquia"), db: Any = Depends(conect_db)):    
    paroquia = db.query('{}{}'.format(
        'select * from paroquia where id = ', id))
    if len(paroquia) != 0:
        db.manipulate('{}{}'.format(
            'Delete from paroquia where id = ', id))
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Registro não encontrado!')
