FROM python:3.12.3-alpine3.19

WORKDIR /back_drf
COPY . .

COPY requirements.txt ./

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libc-dev build-base

RUN pip install -r requirements.txt


CMD ["sh", "-c", "cd lily_api/ && \
    python manage.py collectstatic --noinput && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    gunicorn --workers 3 --bind 0.0.0.0:8000 lily_api.wsgi:application"]
