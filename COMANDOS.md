BUILD
docker build -t pfastapi .

RUN - Completo
docker run -d --name pfastapi -p 8000:8000 pfastapi

RUN - Resumido
docker run -p 8000:8000 pfastapi

Apagar containers em lote
docker rm $(docker ps -a -q)

Apagar images em lote
docker rmi $(docker images -a -q)

