import os
from dotenv import load_dotenv

# Carregando arquivo .ini
load_dotenv() 

# Diretório do sistema
chdir='{}'.format(os.path.dirname(os.path.dirname(os.path.abspath('__file__'))))

# Debug 
debug=os.getenv('DEBUG')

# IP e Porta 
bind=os.getenv('BIND')

# Nº de processos por CPU
workers=os.getenv('WORKERS')

worker_class='uvicorn.workers.UvicornWorker'

keepalive=os.getenv('KEEPALIVE')

worker_connections=os.getenv('WORKER_CONNECTIONS')

pidfile=os.path.join(chdir, 'py-fastapi', 'gunicorn.pid')
