from fastapi import FastAPI

app = FastAPI(title="MAP-e - FastAPI")

from app.db.db import DBConnect

@app.get("/")
async def get_paroquias():
    cur = DBConnect()
    paroquias = cur.query('select * from paroquia')
    return paroquias


if __name__ == '__main__':
    import uvicorn
    import os
    from dotenv import load_dotenv

    load_dotenv() 

    uvicorn.run("main:app", log_level="info", 
        debug=os.getenv('DEBUG'), reload=os.getenv('RELOAD'))