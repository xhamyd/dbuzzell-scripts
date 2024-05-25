# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.12

# Starting with a base Python image, Python 3.8+ required
FROM python:${PYTHON_VERSION}

# Set the timezone based on the host machine
ENV TZ='America/Los_Angeles'

# Copy over the needed files
WORKDIR /home/docker-user/python-scripts
COPY ics_cal_viewer.py ics_cal_viewer.py
COPY requirements.txt requirements.txt

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt --root-user-action=ignore

CMD ["python", "./ics_cal_viewer.py", "-f", "ics_files/"]
