# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile.txt reference guide at
# https://docs.docker.com/engine/reference/builder/

ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# NGINX
RUN apt-get -y update
RUN apt-get -y install gcc
RUN python -m pip install uWSGI==2.0.23
COPY nginx/uwsgi.ini .

COPY data/cancer/*.pickle data/cancer/
COPY data/house/*.pickle data/house/
COPY data/mnist/*.pickle data/mnist/
COPY api.py .
COPY sklearn_service.py .

# Expose the port that the application listens on.
EXPOSE 80

CMD uwsgi --ini uwsgi.ini