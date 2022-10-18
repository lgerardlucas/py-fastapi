'''
File - Configuration gunicorn
'''
import os
from dotenv import load_dotenv

# Carregando arquivo .ini
load_dotenv()

# Diretório do sistema
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
chdir = BASEDIR

# Debug
debug=os.getenv('DEBUG')

# IP e Porta 
bind=os.getenv('BIND')

# Nº de processos por CPU
workers=3 #os.getenv('WORKERS')

#worker_class='uvicorn.workers.UvicornWorker'

keepalive=60 #os.getenv('KEEPALIVE')

worker_connections=1000 #os.getenv('WORKER_CONNECTIONS')

#pidfile=os.path.join(chdir, 'gunicorn.pid')
