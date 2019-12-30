FROM python:3.7-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code


# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system
RUN apt-get update && apt-get install -y gettext libgettextpo-dev

COPY . /code/

ADD ./requirements.txt ./
RUN python3 -m pip install -r requirements.txt 