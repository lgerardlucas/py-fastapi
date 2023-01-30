BUILD
docker build -t pfastapi .

RUN - Completo
docker run -d --rm --name pfastapi -p 8000:8000 pfastapi

RUN - Resumido
docker run --rm -p 8000:8000 pfastapi

Apagar containers em lote
docker rm $(docker ps -a -q)

Apagar images em lote
docker rmi $(docker images -a -q)

Acessar o container quando ele é o único ativo 
docker exec -it $(docker ps -q) /bin/bash

Rodar o sistema
gunicorn -c gunicorn.py app.main:app

Documentação
http://127.0.0.1:8000/docs