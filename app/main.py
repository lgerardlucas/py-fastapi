'''
MAIN - Sistema FastAPI
'''
from functools import lru_cache
from .settings import configuration as settings

from fastapi import FastAPI
from .paroquia.router import router as router_paroquia
from .account.router import router as router_account

app = FastAPI(
    title = settings.APP_NAME,
    version = settings.VERSION,
    description = settings.DESCRIPTION
    )

app.include_router(router_paroquia, tags=['API - Paróquias'])
app.include_router(router_account, tags=['API - Usuários'])

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", log_level="info",
                debug=settings.DEBUG, reload=settings.RELOAD)
