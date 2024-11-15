FROM python:3.9.20-alpine3.19

# Add requirements to the image.
ADD requirements.txt requirements.txt

# Asign work directory.
WORKDIR /mateovergara_app/mateovergara_app

# Install requirements
# The next command is because docker could not
# find the requirements.txt file
RUN pip freeze > requirements.txt
RUN pip install --upgrade pip; \
  pip install -r requirements.txt

# Create user without privilegies.
RUN adduser --disabled-password --gecos '' app

ENV HOME /home/app
