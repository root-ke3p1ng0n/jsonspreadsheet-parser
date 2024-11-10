FROM python:3.11-slim


WORKDIR /app


RUN apt-get update && apt-get install -y \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*


COPY ./requirements.txt .


RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPY ./app /app/app