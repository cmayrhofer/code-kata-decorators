FROM ubuntu:20.04 AS devbox

RUN apt-get -qq -y update && apt-get install -qq -y \
  python3.8 \
  python3-pip && \
  apt-get -y autoclean && \
  apt-get -y autoremove && \
  rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

COPY ./requirements-test.txt /requirements-test.txt
RUN pip3 install -r /requirements-test.txt

ENV PYTHONPATH="$PYTHONPATH:/app"

ENTRYPOINT [ "/app/docker/entrypoints/entrypoint.sh" ]
