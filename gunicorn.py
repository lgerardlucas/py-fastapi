'''
File - Configuration gunicorn
'''
import os
from decouple import config

# Diretório do sistema
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))

chdir = BASEDIR
debug=config('DEBUG')
bind=config('BIND')
workers=config('WORKERS')
keepalive=config('KEEPALIVE')
worker_connections=config('WORKER_CONNECTIONS')
