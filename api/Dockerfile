FROM python:3.9-alpine
RUN apk add --virtual .build-dependencies \
            --no-cache \
            python3-dev \
            postgresql-libs \ 
            musl-dev \
            linux-headers

WORKDIR /app
COPY . /app

RUN apk --no-cache add build-base
RUN apk --no-cache add postgresql-dev
RUN python3 -m pip install psycopg2

RUN pip install -r /app/req.txt
RUN apk del .build-dependencies && rm -rf /var/cache/apk/*

CMD ["uwsgi", "/app/wsgi.ini"]
