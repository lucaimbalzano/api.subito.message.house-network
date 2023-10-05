FROM postgres:15.1-alpine

LABEL author="Luca Imbalzano"
LABEL description="Postgres Image mainly for house, messages, machine-state"
LABEL version="1.0"


USER postgres

COPY ./docker/sql/*.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

CMD ["postgres"]
