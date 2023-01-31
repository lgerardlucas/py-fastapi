'''
MAIN - Sistema FastAPI
'''
from functools import lru_cache
from . import config

from fastapi import FastAPI
from .paroquia.router import router as router_paroquia
from .account.router import router as router_account

app = FastAPI(
    title = config.settings.APP_NAME,
    version = config.settings.VERSION,
    description = config.settings.DESCRIPTION
    )

app.include_router(router_paroquia, tags=['API - Paróquias'])
app.include_router(router_account, tags=['API - Usuários'])

if __name__ == '__main__':
    import uvicorn
    from dotenv import load_dotenv
    load_dotenv()

    uvicorn.run("main:app", log_level="info",
                debug=config.settings.DEBUG, reload=config.settings.RELOAD)
