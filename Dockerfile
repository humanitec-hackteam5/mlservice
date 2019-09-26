FROM python:3.6

WORKDIR /code

RUN apt-get update
RUN apt-get install --assume-yes git python3-dev gcc musl-dev libffi-dev make libstdc++6 netcat

COPY ./requirements/base.txt requirements/base.txt
COPY ./requirements/production.txt requirements/production.txt
RUN pip install --upgrade pip && pip install -r requirements/production.txt --no-cache-dir

ADD . /code

# Collecting static files
RUN ./scripts/run-collectstatic.sh

EXPOSE 8080
ENTRYPOINT ["bash", "/code/docker-entrypoint.sh"]
