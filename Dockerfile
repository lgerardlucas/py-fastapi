FROM python:3.9.4-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \ 
    && apt-get -y install cron vim \
    && python -m pip install --upgrade pip \
    && apt-get install -y libaio1 \
    && apt-get install -y locales locales-all

ENV LC_ALL pt_BR.UTF8
ENV LANG pt_BR.UTF8
ENV LANGUAGE pt_BR.UTF8
ENV HOST 192.168.0.106
ENV DB pgmape
ENV ROLE postgres
ENV PASSWORD postgres
ENV SECRET_KEY 'z$_gn6&^&u1yv7!a+4rt3749#suj+-gzewikjy$=wqxewp)7bo'
ENV JWT_ALGORITHM 'HS512'
ENV ACCESS_TOKEN_EXPIRE_HOURS 24

WORKDIR /app

COPY . .

RUN python3 -m venv myvenv \
&& myvenv/bin/pip install --upgrade pip \
&& . myvenv/bin/activate \
&& pip install -r requirements.txt

RUN groupadd -r user && useradd -r -g user user
USER user


EXPOSE 8000:8000

CMD ["/app/myvenv/bin/gunicorn", "-c", "gunicorn.py", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]
#CMD ["/app/myvenv/bin/gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "3", "-b", "0.0.0.0:8000", "app.main:app"]