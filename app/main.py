'''
MAIN - Sistema FastAPI
'''
from fastapi import FastAPI
from .paroquia.router import router as router_paroquia

app = FastAPI(
    title="Igreja - Dízimo",
    version='0.0.1',
    description="Sistema de Dízimo - Paróquia"
    )


app.include_router(router_paroquia, tags=['API - Paróquias'])

if __name__ == '__main__':
    import uvicorn
    import os
    from dotenv import load_dotenv

    load_dotenv()

    uvicorn.run("main:app", log_level="info",
                debug=os.getenv('DEBUG'), reload=os.getenv('RELOAD'))
