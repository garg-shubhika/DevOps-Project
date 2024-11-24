FROM postgres:17

# Set environment variables
ENV POSTGRES_DB=fleet_db
ENV POSTGRES_USER=fleet_user
ENV POSTGRES_PASSWORD=fleet_pwd

COPY ./init-scripts/ /docker-entrypoint-initdb.d/

EXPOSE 5432