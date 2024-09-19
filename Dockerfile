FROM python:3.11.9-alpine

RUN apk update && apk add --no-cache \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev

WORKDIR /consumer

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "--config", "gunicorn_config.py", "--log-level", "debug", "consumer.wsgi:application"]