FROM python:3.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
COPY virtualenv/centralize /app/
WORKDIR /app
RUN pip install -r requirements.txt
