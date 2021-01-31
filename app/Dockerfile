FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY dockerpostgresapp.py app.py
CMD ["python", "app.py"]
