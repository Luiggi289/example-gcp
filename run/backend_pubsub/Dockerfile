# [START cloudrun_helloworld_dockerfile]
# [START run_helloworld_dockerfile]

# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Permitir que las declaraciones y los mensajes de registro aparezcan inmediatamente en los registros
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt



CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app

# [END dockerfile]
