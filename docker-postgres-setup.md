
https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/

# Docker file for Postgres image:
  ==============================
Dockerfile:

    FROM postgres:latest
    ENV POSTGRES_PASSWORD=password1
    ENV POSTGRES_USER=postgres
    ENV POSTGRES_DB=postgres
    COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql


docker-entrypoint-initb.d:
=========================
    docker-entrypoint-initb.d

    CREATE TABLE IF NOT EXISTS numbers (
          number    BIGINT,
          firstname VARCHAR(20),
          lastname  VARCHAR(20),
          timestamp BIGINT
    );


# Reference:

      postgresql://{username}:{password}@localhost:5432/{database}'.format(
                  username='postgres',
                  password='password1',
                  database='postgres'
         )
         
#requirements.txt

      flask
      sqlalchemy
      psycopg2


#Python dockerfile:

           FROM python:latest
           WORKDIR /code
           ADD requirements.txt requirements.txt
           RUN pip install -r requirements.txt
           COPY app.py app.py
           CMD ["python", "dockerpostgresapp.py"]



#Docker compose:


        version: "3.8"
        services:
        app :
            build: ./app/
        db:
            build: ./database/
