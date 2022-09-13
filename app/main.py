from typing import Any
from email.policy import HTTP
from app.db.db import DBConnect
from http.client import HTTPException
from fastapi import (
    FastAPI, HTTPException, status, Response, Path, Depends
)
from app.paroquia.model import Paroquia

def conect_db():
    cur = DBConnect()
    try:
        yield cur
    finally:
        cur.close()
    

app = FastAPI(
    title="Igreja - Dízimo",
    version='0.0.1',
    description="Sistema de Dízimo - Paroquiano"
    )

@app.get("/paroquias", 
         description="Lista de todas as Paróquias ativas", 
         summary="Lista de Paróquias",
         response_model=Paroquia
         )
async def get_paroquias(db: Any = Depends(conect_db)):
    paroquias = db.query('select * from paroquia')

    if len(paroquias) != 0:
        return paroquias
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Registro não encontrado!')


@app.get("/paroquia/{id}", 
         description="Retorna Paróquia pesquisada", 
         summary="Retorna Paróquia",
         response_model=Paroquia
         )
async def get_paroquia(id: int = Path(default=None, title="ID da Paróquina", description="Informe o ID da Paróquia"), db: Any = Depends(conect_db)):
    paroquia = db.query('{}{}'.format(
        'select * from paroquia where id = ', id))
    
    if len(paroquia) != 0:
        return paroquia
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Registro não encontrado!')


@app.post("/paroquia", 
        status_code=status.HTTP_201_CREATED, 
        description="Salva a nova Paróquia", 
        summary="Salvar Paróquia",
        response_model=Paroquia
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


@app.put("/paroquia/{id}", 
         description="Atualiza campos da tabela de Paróquias", 
         summary="Atualiza Paróquia",
         response_model=Paroquia
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

@app.delete("/paroquia/{id}", 
            status_code=status.HTTP_200_OK,
            response_model=Paroquia
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

if __name__ == '__main__':
    import uvicorn
    import os
    from dotenv import load_dotenv

    load_dotenv()

    uvicorn.run("main:app", log_level="info",
                debug=os.getenv('DEBUG'), reload=os.getenv('RELOAD'))
