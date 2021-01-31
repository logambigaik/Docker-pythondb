FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY dockerpostgressapp.py app.py
CMD ["python", "app.py"]
