FROM python:3.9-bullseye

RUN apt update -y && apt upgrade -y && apt install -y \
  libgl1-mesa-dev

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
