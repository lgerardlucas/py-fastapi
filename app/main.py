from fastapi import FastAPI

from app.paroquia.router import router

app = FastAPI(
    title="Igreja - Dízimo",
    version='0.0.1',
    description="Sistema de Dízimo - Paróquia"
    )

app.include_router(router, tags=['API - Paróquias'])

if __name__ == '__main__':
    import uvicorn
    import os
    from dotenv import load_dotenv

    load_dotenv()

    uvicorn.run("main:app", log_level="info",
                debug=os.getenv('DEBUG'), reload=os.getenv('RELOAD'))
