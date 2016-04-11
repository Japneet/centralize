FROM python:3.5

ENV PYTHONUNBUFFERED 1


RUN mkdir /virtualenv
COPY virtualenv/ /app/

ENV APPLICATION_ROOT /app
ENV PYTHONPATH $APPLICATION_ROOT/lib/$PYTHON_PATH

CMD source $APPLICATION_ROOT/bin/activate
WORKDIR $APPLICATION_ROOT/centralize/
ADD . $APPLICATION_ROOT/centralize/
CMD	python manage.py runserver 0.0.0.0:8000