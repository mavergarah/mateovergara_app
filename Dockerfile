FROM python:3.6.5
ARG DJANGO_ENV

# Add requirements to the image.
ADD requirements.txt /app/requirements.txt

# Asign work directory.
WORKDIR /app/

# Install Python requirements.
RUN pip install --upgrade pip; \
        pip install -r requirements.txt

# Create user without privilegies.
RUN adduser --disabled-password --gecos '' app

ENV HOME /home/app
