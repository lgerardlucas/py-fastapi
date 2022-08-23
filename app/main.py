from fastapi import FastAPI

app = FastAPI(title="MAP-e - FastAPI")

from app.db.db import DBConnect

@app.get("/")
async def get_all():
    cur = DBConnect()
    cliente = cur.query('select * from cliente')
    return cliente[10]
