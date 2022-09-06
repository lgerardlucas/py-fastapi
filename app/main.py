from email.policy import HTTP
from typing import AnyStr
from app.db.db import DBConnect
from http.client import HTTPException
from fastapi import (
    FastAPI, HTTPException, status
)
from app.paroquia.model import Paroquia

app = FastAPI(title="Igreja - Dízimo")

@app.get("/paroquias")
async def get_paroquias():
    try:
        cur = DBConnect()
        paroquias = cur.query('select * from paroquia')
        return paroquias
    except KeyError:
        breakpoint()
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Registro não encontrado!'
        )


@app.get("/paroquia/{id}")
async def get_paroquia(id: int):
    try:
        cur = DBConnect()
        paroquia = cur.query('{}{}'.format(
            'select * from paroquia where id = ', id))
        return paroquia
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Registro não encontrado!'
        )


@app.post("/paroquia", status_code=status.HTTP_201_CREATED)
async def post_paroquia(paroquia: Paroquia):
    if paroquia:
        cur = DBConnect()
        cur.manipulate("Insert Into paroquia(name, street, district, city) Values('{}','{}','{}','{}')".format(
            paroquia.name, paroquia.street, paroquia.district, paroquia.city))
    return paroquia


@app.put("/paroquia/{id}")
async def put_paroquia(id: int, paroquia: Paroquia):
    if paroquia and id:
        cur = DBConnect()
        cur.manipulate("Update paroquia Set name='{}', street='{}', district='{}', city='{}' Where id={}".format(
            paroquia.name, paroquia.street, paroquia.district, paroquia.city, id))
    return paroquia


if __name__ == '__main__':
    import uvicorn
    import os
    from dotenv import load_dotenv

    load_dotenv()

    uvicorn.run("main:app", log_level="info",
                debug=os.getenv('DEBUG'), reload=os.getenv('RELOAD'))
