#Dockerfile, Image, Container
FROM ubuntu:latest
FROM python:3.10-slim

RUN apt update
RUN apt install python3 -y

RUN python3 -m venv pythonshacl
RUN python3 -m pip install pyshacl datetime

WORKDIR /usr/app/src


COPY pyshacl_shacl.py ./
COPY instance_data instance_data/
COPY shapes_graphs shapes_graphs/
COPY validation_reports validation_reports/

CMD ["python3", "./pyshacl_shacl.py"]