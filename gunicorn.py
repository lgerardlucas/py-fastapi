import os

# Debug 
debug=False

# Diretório do sistema
chdir='{}'.format(os.path.dirname(os.path.dirname(os.path.abspath('__file__'))))

# IP e Porta 
bind='0.0.0.0:8000'

# Nº de processos por CPU
workers=4

worker_class='uvicorn.workers.UvicornWorker'

keepalive=60

worker_connections=1000

pidfile='{}{}'.format(chdir,'gunicorn.pid')
