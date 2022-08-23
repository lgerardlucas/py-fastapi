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


WORKDIR /src

COPY . /src
RUN pip install -r /src/requirements.txt

EXPOSE 8000:8000

CMD ["gunicorn", "-c", "gunicorn.py", "app.main:app"]
