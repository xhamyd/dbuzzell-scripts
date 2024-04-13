# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.12

# Starting with a base Python image, Python 3.8+ required
FROM python:${PYTHON_VERSION}

RUN mkdir -p /home/docker-user/python-scripts
WORKDIR /home/docker-user/python-scripts

# Copy over the needed files
COPY ics_cal_viewer.py ics_cal_viewer.py
COPY requirements.txt requirements.txt

# Set the timezone based on the host machine
ENV TZ='America/Los_Angeles'

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt --root-user-action=ignore

# Set the command to run in the container
CMD ["python", "ics_cal_viewer.py", "-f", "ics_files/"]
