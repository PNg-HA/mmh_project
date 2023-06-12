FROM mysql:8.0.33

# RUN chown -R mysql:root /var/lib/mysql

ENV MYSQL_ROOT_PASSWORD=root

COPY ./newn.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
