'''
MAIN - Sistema FastAPI
'''
from fastapi import FastAPI
from .paroquia.router import router as router_paroquia
from .account.router import router as router_account
from .oauth.oauth2 import router as router_oauth

app = FastAPI(
    title="Igreja - Dízimo",
    version='0.0.1',
    description="Sistema de Dízimo - Paróquia"
    )


app.include_router(router_paroquia, tags=['API - Paróquias'])
app.include_router(router_account, tags=['API - Usuários'])
app.include_router(router_oauth, tags=['API - OAuth2'])

if __name__ == '__main__':
    import uvicorn
    import os
    from dotenv import load_dotenv

    load_dotenv()

    uvicorn.run("main:app", log_level="info",
                debug=os.getenv('DEBUG'), reload=os.getenv('RELOAD'))
