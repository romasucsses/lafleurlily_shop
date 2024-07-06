FROM python:3.12.3-alpine3.19

WORKDIR /back_drf
COPY . .

COPY requirements.txt ./

RUN apk update && apk add --no-cache mariadb-dev build-base

RUN pip install -r requirements.txt

CMD ["sh", "-c", "cd lily_api/ && python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
