from decouple import config
from pydantic import BaseSettings


class Settings(BaseSettings):
    '''
    Configuration - APP
    '''
    #APP
    APP_NAME: str = "Igreja - Dízimo"
    ADMIN_EMAIL: str = "lgerardlucas@gmail.com"
    VERSION: str = 'v.0.1'
    DESCRIPTION: str = "Sistema de Dízimo - Paróquia"

    #SECURITY
    SECRET_KEY: str = config('SECRET_KEY')
    JWT_ALGORITHM: str = config('JWT_ALGORITHM')
    ACCESS_TOKEN_EXPIRE_HOURS: int = config('ACCESS_TOKEN_EXPIRE_HOURS')

    #CONFIGURATIOIN
    RELOAD: bool = config('RELOAD', cast=bool)
    DEBUG: bool = config('DEBUG', cast=bool)

settings = Settings()