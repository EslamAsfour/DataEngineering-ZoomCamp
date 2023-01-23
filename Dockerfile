FROM python:3.9

RUN pip install pandas
WORKDIR /app

COPY pipeline.py pipeline.py
ENTRYPOINT [ "python" , "pipeline.py" ]


services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    volumes:
      - postgres-db-volume:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "airflow"]
      interval: 5s
      retries: 5


docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v d:/DE_ZoomCamp/1.Docker-Terraform/ny_taxi_postgres_data:/var/lib/postgresql/data -p 5432 postgres:13 