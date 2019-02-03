FROM python:3.4-alpine
ADD . /code
WORKDIR /code
RUN apk add --virtual build-deps gcc python-dev musl-dev
RUN apk add postgresql-dev
RUN pip install -r requirements.txt
CMD ["python", "wsgi.py"]