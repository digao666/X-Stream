FROM mysql:5.7.15

ENV MYSQL_DATABASE=assets \
    MYSQL_ROOT_PASSWORD=root

ADD init.sql /docker-entrypoint-initdb.d

EXPOSE 3306

WORKDIR /
RUN mkdir -p /metadata

