FROM python:3.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code


# Install dependencies
#COPY Pipfile Pipfile.lock /code/
COPY Pipfile /code/
# RUN pip install pipenv &&pipenv install --system
RUN apt-get update 
RUN pip install pipenv 
# RUN apt-get install postgresql
# RUN apt-get install python-psycopg2
# RUN apt-get remove libpq5
# RUN pipenv install psycopg2-binary
# RUN apt-get install -y libpq-dev
RUN pipenv install 
RUN pipenv install --system
# RUN apt-get update && apt-get install -y gettext libgettextpo-dev
RUN apt-get install -y gettext libgettextpo-dev

COPY . /code/
