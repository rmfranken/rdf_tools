#Dockerfile, Image, Container
FROM ubuntu:latest
#FROM python:3.10-slim

# Install OpenJDK-17

RUN apt-get update
RUN apt-get install -y openjdk-17-jdk
RUN apt-get install -y ant
RUN apt-get clean;

# Fix certificate issues
RUN apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

## Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

# for shacl

RUN echo $PATH
RUN export SHACLROOT=/shacl-142/bin
RUN export PATH=$SHACLROOT:$PATH
#RUN export PATH="$PATH:/etc/profile"; echo $PATH
#RUN echo $PATH

RUN apt install python3 -y
RUN apt install python3.10-venv -y
RUN apt-get -y install python3-pip
RUN python3 -m venv pythonshacl
RUN python3 -m pip install pyshacl datetime configparser

WORKDIR /usr/app/src

COPY shacl-142 ./shacl-142
COPY topbraid_shacl.py ./
COPY pyshacl_shacl.py ./
COPY instance_data ./instance_data
COPY shapes_graphs ./shapes_graphs
COPY config.ini ./
COPY validation_reports ./validation_reports


CMD ["python3", "./topbraid_shacl.py"]
#CMD ["python3", "./pyshacl_shacl.py"]