### ENTORNO DEV ###

# pull official base image
FROM python:3.10.7

# set work directory
WORKDIR /plaza_web_paradigma/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
# RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
#RUN pip install psycopg2-binary
COPY requeriments.txt .
RUN pip install -r requeriments.txt

# copy project

COPY . .
