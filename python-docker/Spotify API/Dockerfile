# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.12

# Starting with a base Python image, Python 3.8+ required
FROM python:${PYTHON_VERSION}

# Set the timezone based on the host machine
ENV TZ='America/Los_Angeles'

# Install Python packages
WORKDIR /home/docker-user
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt --root-user-action=ignore

# Copy the Python source files
COPY src/ python-scripts/
WORKDIR /home/docker-user/python-scripts
CMD ["python", "./spotify_api.py"]
