FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install libicu-dev

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app
