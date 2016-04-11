FROM python:3.5

ENV PYTHONUNBUFFERED 1

RUN pip install virtualenv
RUN virtualenv app
CMD source app/bin/activate

COPY virtualenv/centralize /app/centralize
WORKDIR /app/centralize
ADD . /app/centralize

RUN pip install -r requirements.txt
RUN	python manage.py migrate
CMD	python manage.py runserver 0.0.0.0:8000