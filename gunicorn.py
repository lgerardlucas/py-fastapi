import os

# Diretório do sistema
chdir = '{}'.format(os.path.dirname(os.path.dirname(os.path.abspath('__file__'))))

bind='0.0.0.0:8000'

workers=2

worker_class = 'uvicorn.workers.UvicornWorker'

keepalive = 60

worker_connections = 1000

pidfile = '{}{}'.format(chdir,'gunicorn.pi')
