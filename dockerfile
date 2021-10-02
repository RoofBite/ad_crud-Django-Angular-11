# Python and Linux Version 
FROM python:3.8-slim-buster
ARG DJANGO_SUPERUSER_USERNAME=admin
ARG DJANGO_SUPERUSER_PASSWORD=admin
ARG DJANGO_SUPERUSER_EMAIL=admin@example.com

RUN apt-get update && apt-get install -y git
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get install nodejs npm -y \
&& apt-get clean 


COPY requirements.txt /app/requirements.txt

# Configure server
RUN set -ex \
    && pip install --upgrade pip \  
    && pip install --no-cache-dir -r /app/requirements.txt 


# Working directory
WORKDIR /app

ADD . .
RUN cd frontend && npm --no-package-lock install && npm run build


RUN python manage.py collectstatic --noinput \
&& python manage.py makemigrations \
&& python manage.py migrate \
&& python manage.py createsuperuser --noinput


EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "ad_crud_project.wsgi:application"]
