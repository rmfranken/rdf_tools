#Dockerfile, Image, Container

# Create layer from python 3.10 Docker image
FROM python:3.10-slim

# Add metadata to Dockerfile
LABEL org.opencontainers.image.base.name="python:3.10"
LABEL org.opencontainers.image.title="rdf-tools"
LABEL org.opencontainers.image.url="https://github.com/rmfranken/rdf_tools"

# Install python3
RUN apt update
RUN apt install python3 -y

# Create virtual environment with pyshacl installed
RUN python3 -m venv pythonshacl
RUN python3 -m pip install pyshacl datetime

WORKDIR /usr/app/src

# We add files from this directory to the Docker container
COPY pyshacl_shacl.py ./
COPY instance_data instance_data/
COPY shapes_graphs shapes_graphs/
COPY validation_reports validation_reports/

# Commands to run with the container
CMD ["python3", "./pyshacl_shacl.py"]