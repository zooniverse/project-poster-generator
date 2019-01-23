FROM python:2.7

WORKDIR /usr/src/

COPY requirements.txt /usr/src/

RUN pip install -r requirements.txt

COPY . /usr/src/
