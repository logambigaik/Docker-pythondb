FROM postgres:latest
ENV POSTGRES_PASSWORD=password1
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=postgres
COPY /docker-entrypoint-initdb.db/sql1.sql docker-entrypoint-initdb.d/sql1.sql
