### Build and install packages
FROM python:3.8 as build-python

RUN apt-get -y update \
  # Cleanup apt cache
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*


RUN mkdir /app
WORKDIR /app

ENV PYTHONUNBUFFERED 1

# Install Python dependencies
COPY ./requirements.txt ./
COPY ./manage.py ./

RUN pip install -r requirements.txt
RUN chmod +x ./manage.py


COPY ./scripts/docker-entrypoint.sh ./scripts/docker-entrypoint.sh
RUN chmod 775 ./scripts/docker-entrypoint.sh 
RUN chmod +x ./scripts/docker-entrypoint.sh
RUN chmod 775 ./scripts/docker-entrypoint.sh \
  && ln -s ./scripts/docker-entrypoint.sh /

COPY . ./

ENV PROCESSES 4

