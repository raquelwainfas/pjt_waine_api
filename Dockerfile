FROM python:3.9.3-buster
USER root

RUN mkdir -p /app
COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000/tcp
CMD python3 -m flask run --host=0.0.0.0 --port=5000