FROM python:3.9-bullseye

RUN apt update -y && apt upgrade -y && apt install -y \
  libgl1-mesa-dev \
  imagemagick

RUN grep -v '<policy domain="path" rights="none" pattern="@\*"/>' /etc/ImageMagick-6/policy.xml > /tmp/imagemagick && \
  cp /tmp/imagemagick /etc/ImageMagick-6/policy.xml

COPY . /src/spcconverter
WORKDIR /src/spcconverter
RUN pip install --upgrade pip && pip install -e .
