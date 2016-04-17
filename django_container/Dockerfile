FROM python:3.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
COPY virtualenv/centralize /app/
WORKDIR /app
EXPOSE 8000
CMD ["/bin/bash"]
#RUN pip install -r requirements.txt
