FROM python:3.5.2-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
CMD gunicorn -b :8000 shinigami.wsgi
