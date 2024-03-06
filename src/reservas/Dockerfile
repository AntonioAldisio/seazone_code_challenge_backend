FROM python:3.10.11-slim-bullseye

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./start.sh /usr/bin/start.sh
COPY . .


ENV MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
ENV MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient"



RUN apt-get update && \
    apt-get install python3-dev default-libmysqlclient-dev build-essential -y && \
    pip3 install --no-cache-dir --upgrade -r /app/requirements.txt && \
    mkdir -p /usr/bin/

RUN chmod +x /usr/bin/start.sh

EXPOSE 8000

ENTRYPOINT [ "start.sh" ]