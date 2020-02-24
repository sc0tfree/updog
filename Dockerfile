FROM python:3.8-alpine

WORKDIR /uploads
VOLUME /uploads

RUN apk add gcc musl-dev libffi-dev openssl-dev

RUN pip install updog

EXPOSE 9090

CMD ["updog"]

