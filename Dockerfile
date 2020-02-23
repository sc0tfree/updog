FROM python:3


RUN pip install updog
ADD serve /serve

EXPOSE 9090

CMD  updog -d serve